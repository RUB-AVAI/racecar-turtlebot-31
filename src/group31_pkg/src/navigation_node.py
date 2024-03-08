import os
import rclpy
import numpy as np
import matplotlib.pyplot as plt
from rclpy.node import Node
from message_filters import ApproximateTimeSynchronizer, Subscriber
from avai_messages.msg import Motors, Motor, Position
from sensor_msgs.msg import LaserScan



IMSAVE_PATH = os.path.dirname(os.path.realpath(__file__)) + "/../../visualisations/route.png"

class NavigationNode(Node):
    def __init__(self):
        super().__init__('navigation_node')
        
        self.motor_subscription = Subscriber(self, Motors, '/motor_position')
        self.lidar_subscription = Subscriber(self, LaserScan, "/scan", qos_profile=rclpy.qos.qos_profile_sensor_data)
        
        ts = ApproximateTimeSynchronizer([self.motor_subscription, self.lidar_subscription], queue_size=10, slop=0.1)
        ts.registerCallback(self.drive)
        
        self.motor_publisher = self.create_publisher(Motors, '/motor_velocity', 10)
        
        self.position_publisher = self.create_publisher(Position, '/position', qos_profile=rclpy.qos.qos_profile_sensor_data)
        
        self.WHEEL_DISTANCE = 160 #mm
        self.RADIUS_ROBOT = 89 #mm
        self.WHEEL_RADIUS = 33 #mm
        self.NUM_TICKS = 4096
        self.LAMBDA = 100
        self.LAMBDA_TAR = 60
        
        self.MAX_VELOCITY = 255
        self.TARGET_RADIUS = 25
        self.TARGET_X = 0
        self.TARGET_Y = 0
        
        #self.TARGETS_X = [0, 1000, 1000, 0]
        #self.TARGETS_Y = [1000, 1000, 0, 0]
        
        self.TARGETS_X = [-10000]
        self.TARGETS_Y = [0]
        
        
        self.TARGET_X = self.TARGETS_X.pop(0)
        self.TARGET_Y = self.TARGETS_Y.pop(0)
        
        self.x = 0
        self.y = 0
        self.phi = 0#2*np.pi
        
        self.x_all = []
        self.y_all = []
        
        
        #self.PSI_OBS = list(range(0, 180, 1)) + list(range(-180, 0, 1))
        self.PSI_OBS = list(range(180, 0, -1)) + list(range(0, -180, -1))
        self.PSI_OBS = np.deg2rad(self.PSI_OBS)

        
        self.beta_1 = 60
        self.beta_2 = 160

        
        self.counter = 0 # Counts number of callback calls


    def getDeltaPhi(self):
        """
        Returns the new direction of robot
        """
        f_obs = 0
        for psi_obs_i, range in zip(self.PSI_OBS, self.ranges):
            if range == 0.0:
                continue
            range *= 1000 # from meter to millimeter
            f_obs += self.f_obs_i(psi_obs_i, range)
            #print(f_obs, np.rad2deg(psi_obs_i), range)
        #exit()
        return self.f_tar() + f_obs

    
    def f_tar(self):
        """
        Influence from target dynamics
        
        lam_tar: turning speed of the robot. Unit radians/s 
        phi: current direction in global coordinate system in radians
        psi_tar: direction of target in global coordinate system in radians
        
        returns influence of target to new phi
        """
        return -self.LAMBDA_TAR * np.sin(self.phi - self.psi)
    
    
    def f_obs_i(self, psi_obs, range):
        """
        Creates repellors at the locations of obstacles
        
        psi_obs_i: direction in radians
        lidar_data_i: distance
        
        Returns influence of psi_obs
        """
        lambda_ops_i = self.lambda_obs(range)
        sigma = self.sigma(range)
        exp_arg = ((-psi_obs)**2)/(2*sigma**2)
        return lambda_ops_i*(-psi_obs)*np.exp(-exp_arg)

    
    
    def lambda_obs(self, d):
        """
        weight function
        """
        return self.beta_1 * np.exp(-(d/self.beta_2))
    
    
    def sigma(self, d):
        return np.arctan(np.tan(1/2) + (self.RADIUS_ROBOT / (self.RADIUS_ROBOT) + d))
    

    def getDirection(self):
        """
        Calculates the heading direction
        """
        self.psi = -np.arctan2(self.y-self.TARGET_Y, self.x-self.TARGET_X)
    
    
    def getVelocity(self, deltaPhi):
        velocity = int((deltaPhi * (self.WHEEL_DISTANCE/2))/50)
        
        if np.abs(self.LAMBDA) >= self.MAX_VELOCITY:
            print("The constant forward velocity self.LAMBDA can't be larger then the maxium_velocity self.MAX_VELOCITY!")
            exit()

        self.v_l = int(velocity+self.LAMBDA)
        self.v_l = max(self.v_l, 5)
        self.v_l = min(self.v_l, self.MAX_VELOCITY)
        
        self.v_r = int(-velocity+self.LAMBDA)
        self.v_r = max(self.v_r, 5)
        self.v_r = min( self.v_r, self.MAX_VELOCITY)
    
       
    def setVelocity(self, v_l, v_r):
        """
        sets the new velocity
        """
        new_motor_command = Motors()
        new_motor_command.motors = [
            Motor(position=1, velocity=v_l), 
            Motor(position=1, velocity=v_r)
        ]
        #self.get_logger().info(f'Published velocities')
        self.motor_publisher.publish(new_motor_command)


    def updateMovement(self):
        """
        Updates the movement
        """
        # Track the ticks that has been made since the last time step for the right wheel
        right_now_ticks =  self.RIGHT_MOVED - self.TOTAL_RIGHT_MOVED
        self.TOTAL_RIGHT_MOVED = self.RIGHT_MOVED
        right_now_moved = right_now_ticks * ((2*np.pi*self.WHEEL_RADIUS)/self.NUM_TICKS)
        
        # Track the ticks that has been made since the last time step for the left wheel
        left_now_ticks = self.LEFT_MOVED - self.TOTAL_LEFT_MOVED
        self.TOTAL_LEFT_MOVED = self.LEFT_MOVED
        left_now_moved = left_now_ticks * ((2*np.pi*self.WHEEL_RADIUS)/self.NUM_TICKS)
        
        self.phi = (self.phi + (left_now_moved - right_now_moved) / self.WHEEL_DISTANCE) % (2*np.pi)
        
        c = (left_now_moved + right_now_moved) / 2
        self.x = self.x - c * np.cos(self.phi)
        self.y = self.y + c * np.sin(self.phi)
        
        #Publish the current position
        current_position = Position()
        current_position.header.stamp = self.get_clock().now().to_msg()
        current_position.x_position = self.x
        current_position.y_position = self.y
        current_position.facing_direction = np.rad2deg(self.phi) % 360
        
        #self.get_logger().info(f'Published position')
        self.position_publisher.publish(current_position)


    def drive(self, msg_motor, msg_lidar):
        #self.get_logger().info(f'Received synchronized messages')
        
        if self.counter == 0:
            self.TOTAL_LEFT_MOVED, self.TOTAL_RIGHT_MOVED = msg_motor.motors[0].position, msg_motor.motors[1].position  
            self.LAST_TIMESTEP = float(str(msg_motor.header.stamp.sec) + '.' + str(msg_motor.header.stamp.nanosec))         
        else:
            TIMESTEP = float(str(msg_motor.header.stamp.sec) + '.' + str(msg_motor.header.stamp.nanosec))
            self.CURRENT_TIME_STEP = TIMESTEP - self.LAST_TIMESTEP
            self.LAST_TIMESTEP = TIMESTEP
            
            self.ranges = msg_lidar.ranges
            self.getDirection()
            delta_phi = self.getDeltaPhi()
            self.getVelocity(delta_phi)
            self.setVelocity(self.v_l, self.v_r)
            #self.setVelocity(0, 0)
            self.LEFT_MOVED, self.RIGHT_MOVED = msg_motor.motors[0].position, msg_motor.motors[1].position
            self.updateMovement()
            self.x_all.append(self.x)
            self.y_all.append(self.y)
            
            print(f"POSITION: {self.x}, {self.y}. HEADING: {self.phi}, TARGET: {self.psi}, V_L:{self.v_l}, V_R:{self.v_r}, TARGET: {self.TARGET_X}, {self.TARGET_Y}")
            if np.abs(self.TARGET_X-self.x) < self.TARGET_RADIUS and np.abs(self.TARGET_Y-self.y) < self.TARGET_RADIUS:
                if not self.TARGETS_X:
                    self.setVelocity(0, 0)
                    plt.plot(self.y_all, self.x_all)
                    plt.savefig(IMSAVE_PATH)
                    exit()
                else:
                    self.TARGET_X = self.TARGETS_X.pop(0)
                    self.TARGET_Y = self.TARGETS_Y.pop(0)
            
            
        
        self.counter += 1
    

def main(args=None): 
    rclpy.init(args=args)
    
    navigation = NavigationNode()
    rclpy.spin(navigation)
    
    navigation.destroy_node()
        
    rclpy.shutdown()

if __name__ == '__main__':
    main()
