import os
import rclpy
import numpy as np
import matplotlib.pyplot as plt
from rclpy.node import Node
from message_filters import ApproximateTimeSynchronizer, Subscriber
from avai_messages.msg import Motors, Motor, Position, Targets
from sensor_msgs.msg import LaserScan
from time import sleep



IMSAVE_PATH = os.path.dirname(os.path.realpath(__file__)) + "/../../visualisations/route.png"



class KalmanFilter:
    def __init__(self, initial_state, process_covariance, measurement_covariance, state_transition, identity_matrix_size):
        self.state = np.array(initial_state, dtype=float)
        self.state_estimate = self.state.copy()
        
        self.process_covariance = np.array(process_covariance, dtype=float)
        self.measurement_covariance = np.array(measurement_covariance, dtype=float)
        self.state_transition = np.array(state_transition, dtype=float)
        self.identity_matrix = np.identity(identity_matrix_size)


    def predict(self):
        # Predict the next state
        self.state = np.dot(self.state_transition, self.state)
        # Update the state covariance matrix
        self.process_covariance = np.dot(np.dot(self.state_transition, self.process_covariance),
                                         self.state_transition.T)


    def update(self, measurement):
        # Compute Kalman gain
        kalman_gain = np.dot(
            np.dot(self.process_covariance, self.identity_matrix.T), 
            np.linalg.inv(np.dot(np.dot(self.identity_matrix, self.process_covariance), self.identity_matrix.T) + self.measurement_covariance)
        )

        # Update the state estimate
        self.state_estimate = self.state + np.dot(kalman_gain, measurement - np.dot(self.identity_matrix, self.state))

        # Update the state covariance matrix
        self.process_covariance = np.dot((self.identity_matrix - np.dot(kalman_gain, self.identity_matrix)), self.process_covariance)



class NavigationNode(Node):
    def __init__(self):
        super().__init__('navigation_node')
        
        # Set if points from data fusion should be subscribed
        self.GET_TARGETS = False
        
        self.motor_subscription = Subscriber(self, Motors, '/motor_position')
        self.lidar_subscription = Subscriber(self, LaserScan, "/scan", qos_profile=rclpy.qos.qos_profile_sensor_data)
        self.ts = ApproximateTimeSynchronizer([self.motor_subscription, self.lidar_subscription], queue_size=10, slop=0.1)
        if not self.GET_TARGETS:
            self.ts.registerCallback(self.drive)
        
        self.motor_publisher = self.create_publisher(Motors, '/motor_velocity', 10)
        self.position_publisher = self.create_publisher(Position, '/position', qos_profile=rclpy.qos.qos_profile_sensor_data)
        
        # Robot parameter
        self.WHEEL_DISTANCE = 160 #mm
        self.RADIUS_ROBOT = 89 #mm
        self.WHEEL_RADIUS = 33 #mm
        self.NUM_TICKS = 4096
        
        # Positions of sensor entries starting from 180 to -179 with 180 being the back, 90 right, 1 front and -89 left
        #self.THETA = list(range(180, -180, -1))
        self.THETA = list(range(180, -180, -1))
        self.THETA = np.deg2rad(self.THETA)

        # Set if obstacle avoidance or velocity control should be used
        self.OBSTACLE_AVOIDANCE = True
        self.VELOCITY_CONTROL = True
        self.USE_KALMAN = False
        
        # Set if live visualization should be created
        self.VISUALIZATION = True
        
        # Target parameter (changed in future for subscriber of target points)
        self.TARGET_RADIUS = 25
        if not self.GET_TARGETS:
            self.TARGETS_X = [-1000] #[0, 1000, 1000, 0]
            self.TARGETS_Y = [0] #[1000, 1000, 0, 0]
            self.TARGET_X = self.TARGETS_X.pop(0)
            self.TARGET_Y = self.TARGETS_Y.pop(0)
        else:
            self.target_subscriber = self.create_subscription(Targets, "/target_position", self.target_callback, 1)
            self.TARGET_X = 0
            self.TARGET_Y = 0
            self.ROUND = 1
        
        # Start position
        self.x = 0
        self.y = 0
        self.phi = 0
        
        # Tracking
        self.x_all, self.y_all = [], []
        
        # Kalman Filter
        process_covariance = [[0, 0], [0, 0]]
        measurement_covariance = [[0, 0], [0, 0]]
        state_transition = [[0, 0], [0, 0]]
        
        if self.USE_KALMAN:
            self.filter = KalmanFilter(
                initial_state=[self.x, self.y],
                process_covariance=process_covariance,
                measurement_covariance=measurement_covariance,
                state_transition=state_transition,
                identity_matrix_size=2
            )
        
        # Counts number of callback calls
        self.counter = -1
        
        self.called = False
        
        self.params_round1()
        
        if self.VISUALIZATION:
            self.set_visualization()
        
        
    def params_round1(self):
        # Velocity parameter
        self.LAMBDA = 70
        self.LAMBDA_TAR = 2*np.pi
        self.MAX_VELOCITY = 255
        self.MIN_VELOCITY = 5
        
        self.delta_t = 10

        # Parameters for weighting of force-lets of obstacle avoidance
        self.beta_1 = 40
        self.beta_2 = 80
        
        # Parameters for weighting of force-lets for velocity control
        self.alpha_1 = 40
        self.alpha_2 = 300
        
        # Parameters for speed control
        self.c = 0.25
        self.c_u = 3.00
        self.sigma_obs = 25.0
        self.sigma_tar = 22.0
        self.v_obs = 80.0
        self.v_tar = 90.0
    
    
    def params_round2(self):
        self.called = True
        #TODO: Add parameter for the second round
        pass


    def set_visualization(self):
        layout = [
            ["traj", "traj", "f"],
            ["traj", "traj", "g"],
        ]
        
        self.fig = plt.figure(figsize=(15, 10))
        self.ax = self.fig.subplot_mosaic(layout)
        
        
        self.range = [0, 2*np.pi]

    
    def trajectory_visualization(self):
        self.ax["traj"].clear()
        
        self.ax["traj"].set_aspect('equal')
        self.ax["traj"].set_xlim(-1000, 1000)
        self.ax["traj"].set_ylim(-1000, 1000)
        
        self.ax["traj"].plot(self.x_all, self.y_all)
       
        
    def f_visualization(self):
        self.ax["f"].clear()
        
        self.ax["f"].set_ylim(-2*self.LAMBDA_TAR, 2*self.LAMBDA_TAR)
        
        self.ax["f"].scatter(self.phi, self.delta_phi, label="Heading direction", color="green")
        r = np.linspace(self.range[0], self.range[1], 100)
        self.ax["f"].plot(r, self.f_tar(r)+ self.f_obs, label="delta phi")
        self.ax["f"].plot(0)
       
    
    def g_visualization(self):
        self.ax["g"].clear()
        
        categories = ['v', 'g_tar', 'g_obs']
        values = [self.g_tar_value + self.g_obs_value, self.g_tar_value, self.g_obs_value]
        
        self.ax["g"].bar(categories, values, color=['blue', 'green', 'orange'])
       
       
    def visualize(self):
        self.trajectory_visualization()
        
        if self.OBSTACLE_AVOIDANCE:
            self.f_visualization()
        
        if self.VELOCITY_CONTROL:
            self.g_visualization()
        
        self.fig.tight_layout()
        self.fig.savefig(IMSAVE_PATH)
        

    def a_phi(self):
        return np.arctan(self.c * self.V())


    def V(self):
        """
        Calculates the obstacle contribution to the heading direction dynamics.
        
        :param phi: Current heading direction in radians.
        :param obstacles: A list or array of obstacles, each described by its angle and distance.
        :return: The integral value representing the summed influence of obstacles.
        """
        V_phi = 0
        for theta_i, range in zip(self.THETA, self.ranges):
            if range == 0.0:
                continue
            if np.abs(theta_i) > 1.55:
                continue
            range *= 1000
            lambda_i = self.lambda_vel(range)
            sigma_i = self.sigma(range)
            exp_arg = -((-theta_i)**2/(2*sigma_i**2))
            V_phi += lambda_i * sigma_i**2 * np.exp(exp_arg) - np.exp(-1/2)
        return np.clip(V_phi, -self.LAMBDA_TAR, self.LAMBDA_TAR)


    def g_obs(self):
        c_obs = self.c_u * (np.pi / 2 + self.a)
        #print(f"C_OBS: {c_obs}")
        self.g_obs_value = -c_obs * (self.LAMBDA - self.v_obs) * np.exp(-(self.LAMBDA - self.v_obs)**2 / (2 * self.sigma_obs**2))


    def g_tar(self):
        c_tar = self.c_u * (np.pi / 2 - self.a)
        #print(f"C_TAR: {c_tar}")
        self.g_tar_value = -c_tar * (self.LAMBDA - self.v_tar) * np.exp(-(self.LAMBDA - self.v_tar)**2 / (2 * self.sigma_tar**2))


    def control_velocity(self):
        self.a = self.a_phi()
        print(self.a)
        self.g_obs()
        self.g_tar()
        return self.g_obs_value + self.g_tar_value


    def getDeltaPhi(self):
        """
        Returns the new direction of robot
        """
        self.f_obs = 0
        
        if self.OBSTACLE_AVOIDANCE:
            for theta_i, range in zip(self.THETA, self.ranges):
                if range == 0.0:
                    continue
                if np.abs(theta_i) > 1.55:
                    continue
                range *= 1000 # from meter to millimeter
                self.f_obs += self.f_obs_i(theta_i, range)
            self.f_obs = np.clip(self.f_obs, -self.LAMBDA_TAR, self.LAMBDA_TAR)
        self.delta_phi = self.f_tar() + self.f_obs

    
    def f_tar(self, x=None):
        """
        Influence from target dynamics
        
        lam_tar: turning speed of the robot. Unit radians/s 
        phi: current direction in global coordinate system in radians
        psi_tar: direction of target in global coordinate system in radians
        
        returns influence of target to new phi
        """
        if x is None:
            x = self.phi
            
        return -self.LAMBDA_TAR * np.sin(x - self.psi)
    
    
    def f_obs_i(self, theta_obs, range):
        """
        Creates repellors at the locations of obstacles
        
        psi_obs_i: direction in radians
        lidar_data_i: distance
        
        Returns influence of psi_obs
        """
        lambda_i = self.lambda_obs(range)
        sigma = self.sigma(range)
        exp_arg = (-theta_obs**2)/(2*sigma**2)
        return lambda_i*(-theta_obs)*np.exp(-exp_arg)

    
    def lambda_obs(self, d):
        """
        weight function
        """
        return self.beta_1 * np.exp(-d/self.beta_2)
    
    
    def lambda_vel(self, d):
        return self.alpha_1 * np.exp(-d/self.alpha_2)
    
    
    def sigma(self, d):
        return np.arctan(np.tan(1/2) + (self.RADIUS_ROBOT / (self.RADIUS_ROBOT + d)))
    

    def getDirection(self): #same
        """
        Calculates the heading direction
        """
        self.psi = -np.arctan2(self.y-self.TARGET_Y, self.x-self.TARGET_X)
    
       
    def setVelocity(self):
        omega = int((self.delta_phi * (self.WHEEL_DISTANCE/2))/self.delta_t) # mm/ms
        
        if self.VELOCITY_CONTROL:
            v = self.control_velocity()
        else:
            v = self.LAMBDA
        print(v)
        self.v_l = int(np.clip(omega+v, self.MIN_VELOCITY, self.MAX_VELOCITY))
        self.v_r = int(np.clip(-omega+v, self.MIN_VELOCITY, self.MAX_VELOCITY))
        
        new_motor_command = Motors()
        new_motor_command.motors = [
            Motor(position=1, velocity=self.v_l), 
            Motor(position=1, velocity=self.v_r)
        ]
        #self.get_logger().info(f'Published velocities')
        self.motor_publisher.publish(new_motor_command)
        
        
    def stop(self):
        new_motor_command = Motors()
        new_motor_command.motors = [
            Motor(position=1, velocity=0), 
            Motor(position=1, velocity=0)
        ]
        #self.get_logger().info(f'Stopped')
        self.motor_publisher.publish(new_motor_command)


    def updateMovement(self):
        """
        Updates the movement
        """
        # Track the ticks that has been made since the last time step for the right wheel
        right_now_ticks = self.RIGHT_MOVED - self.TOTAL_RIGHT_MOVED
        self.TOTAL_RIGHT_MOVED = self.RIGHT_MOVED
        right_now_moved = right_now_ticks * ((2*np.pi*self.WHEEL_RADIUS)/self.NUM_TICKS)
        
        # Track the ticks that has been made since the last time step for the left wheel
        left_now_ticks = self.LEFT_MOVED - self.TOTAL_LEFT_MOVED
        self.TOTAL_LEFT_MOVED = self.LEFT_MOVED
        left_now_moved = left_now_ticks * ((2*np.pi*self.WHEEL_RADIUS)/self.NUM_TICKS)
        
        self.phi = (self.phi + (left_now_moved - right_now_moved) / self.WHEEL_DISTANCE) % (2*np.pi)
        
        c = (left_now_moved + right_now_moved) / 2
        self.x = self.x - c * np.cos(self.phi) # If + does not work try with -
        self.y = self.y + c * np.sin(self.phi)
        
        if self.USE_KALMAN:
            self.filter.predict()
            self.filter.update([self.x, self.y])
            self.x, self.y = self.filter.state_estimate
        
        #Publish the current position
        current_position = Position()
        current_position.header.stamp = self.get_clock().now().to_msg()
        current_position.x_position = self.x
        current_position.y_position = self.y
        current_position.facing_direction = np.rad2deg(self.phi) % 360
        
        #self.get_logger().info(f'Published position')
        self.position_publisher.publish(current_position)


    def drive(self, msg_motor, msg_lidar):
        #self.get_logger().info(f'Received messages')
        
        self.counter += 1
        if self.counter == 0:
            self.TOTAL_LEFT_MOVED, self.TOTAL_RIGHT_MOVED = msg_motor.motors[0].position, msg_motor.motors[1].position
            return        

        self.ranges = msg_lidar.ranges
        
        self.getDirection()
        self.getDeltaPhi()
        self.setVelocity()
        self.LEFT_MOVED, self.RIGHT_MOVED = msg_motor.motors[0].position, msg_motor.motors[1].position
        self.updateMovement()
        
        self.x_all.append(self.x)
        self.y_all.append(self.y)
        
        if self.VISUALIZATION:
            self.visualize()
        
        print(f"POSITION: ({self.x},{self.y}), HEADING: {self.phi}, TARGET: {self.psi}, V_L:{self.v_l}, V_R:{self.v_r}, TARGET: ({self.TARGET_X},{self.TARGET_Y})")
        
        if not self.GET_TARGETS:
            if np.abs(self.TARGET_X-self.x) < self.TARGET_RADIUS and np.abs(self.TARGET_Y-self.y) < self.TARGET_RADIUS:
                if not self.TARGETS_X:
                    self.stop()
                    sleep(3)
                    raise SystemExit
                else:
                    self.TARGET_X = self.TARGETS_X.pop(0)
                    self.TARGET_Y = self.TARGETS_Y.pop(0)
    
    
    def target_callback(self, msg):
        self.get_logger().info("Target Received")
        
        self.TARGET_X = msg.x_position
        self.TARGET_Y = msg.y_position
        self.ROUND = msg.round
        
        if self.counter == -1:
            self.ts.registerCallback(self.drive)
        
        if self.ROUND == 2 and self.called == False:
            self.params_round2()


def main(args=None): 
    rclpy.init(args=args)
    
    navigation = NavigationNode()
    rclpy.spin(navigation)
    
    navigation.destroy_node()
        
    rclpy.shutdown()



if __name__ == '__main__':
    main()
