import rclpy
import numpy as np
import matplotlib.pyplot as plt
from rclpy.node import Node
from message_filters import ApproximateTimeSynchronizer, Subscriber
from avai_messages.msg import Motors, Motor
from sensor_msgs.msg import LaserScan


class NavigationNode(Node):
    def __init__(self):
        super().__init__('navigation_node')
        
        self.motor_subscription = Subscriber(self, Motors, '/motor_position')
        
        self.lidar_subscription = Subscriber(self, LaserScan, "/scan", qos_profile=rclpy.qos.qos_profile_sensor_data)
        
        ts = ApproximateTimeSynchronizer([self.motor_subscription, self.lidar_subscription], queue_size=10, slop=0.1)
        ts.registerCallback(self.drive)
        
        self.publisher_ = self.create_publisher(Motors, '/motor_velocity', 10)
        
        self.TOTAL_LEFT_MOVED, self.TOTAL_RIGHT_MOVED = 0, 0
        self.WHEEL_DISTANCE = 2048 #TODO: get wheel distance of turtle bot
        
        self.x = 0
        self.y = 0
        self.phi = 0
        self.LAMBDA = 0.5 # forward direction
        self.LAMBDA_TAR = 0.5 # Repelling force of obstacles
        
        self.all_x = []
        self.all_y = []
        
        self.MAX_VELOCITY = 1 #TODO: Get maximal velocity that should be assignend
        
        #TODO: get lidar data and make data on same scale
        self.PSI_OBS = np.deg2rad(range(-180, 180))

        
        self.beta_1 = 0
        self.beta_2 = 0
        self.sigma = 0
        
        self.counter = 0 # Counts number of callback calls


    def getDeltaPhi(self, lidar_data, lam, phi, psi):
        """
        Returns the new direction of robot
        """
        f_obs = 0
        for psi_obs_i, lidar_data_i in (self.PSI_OBS, lidar_data):
            f_obs += self.f_obs_i(psi_obs_i, lidar_data_i)
        return self.f_tar(lam, phi, psi) + f_obs

    
    def f_tar(lam_tar, phi, psi_tar):
        """
        Influence from target dynamics
        
        lam_tar: turning speed of the robot. Unit radians/s 
        phi: current direction in global coordinate system in radians
        psi_tar: direction of target in global coordinate system in radians
        
        returns influence of target to new phi
        """
        return -lam_tar * np.sin(phi - psi_tar)
    
    
    def f_obs_i(self, psi_obs, lidar_data_i):
        """
        Creates repellors at the locations of obstacles
        
        psi_obs_i: direction in radians
        lidar_data_i: distance
        
        Returns influence of psi_obs
        """
        lambda_ops_i = self.lambda_obs(lidar_data_i)
        exp_arg = (psi_obs**2)/(2*self.sigma**2)
        return lambda_ops_i*(psi_obs)*np.exp(-exp_arg)
    
    
    def lambda_obs(self, d):
        """
        weight function
        """
        return self.beta_1 * np.exp(-d/self.beta_2)
    

    def getDirection(self, x_start, y_start, x_end, y_end):
        """
        Calculates the heading direction
        """
        return -np.arctan2(y_start-y_end, x_start-x_end)
    
       
    def setVelocity(self, v_l, v_r):
        """
        sets the new velocity
        """
        new_motor_command = Motors()
        new_motor_command.motors = [
            Motor(position=1, velocity=int(v_l)), 
            Motor(position=1, velocity=int(v_r))
        ]
        self.publisher_.publish(new_motor_command)


    def updateMovement(self, now_x, now_y, old_phi):
        """
        Updates the movement
        """
        right_now_moved =  self.RIGHT_MOVED - self.TOTAL_RIGHT_MOVED
        self.TOTAL_RIGHT_MOVED = self.RIGHT_MOVED
        
        left_now_moved = self.LEFT_MOVED - self.TOTAL_LEFT_MOVED
        self.TOTAL_LEFT_MOVED = self.LEFT_MOVED
        
        new_phi = (old_phi + (right_now_moved - left_now_moved) / self.WHEEL_DISTANCE) % (2*np.pi)
        
        c = (left_now_moved + right_now_moved) / 2
        new_x = now_x - c * np.cos(new_phi)
        new_y = now_y + c * np.sin(new_phi)
        return new_x, new_y, new_phi

    def drive(self, msg_motor, msg_lidar):
        self.get_logger().info(f'Received synchronized messages')
        
        
        if self.counter == 0:
            self.TOTAL_LEFT_MOVED, self.TOTAL_RIGHT_MOVED = msg_motor.motors[0].position, msg_motor.motors[1].position
            
            self.LAST_TIMESTEP = float(str(msg_motor.header.stamp.sec) + '.' + str(msg_motor.header.stamp.nanosec))            
        else:
            self.LEFT_MOVED, self.RIGHT_MOVED = msg_motor.motors[0].position, msg_motor.motors[1].position
            self.x, self.y, self.phi = self.updateMovement(self.x, self.y, self.phi)
            
            TIMESTEP = float(str(msg_motor.header.stamp.sec) + '.' + str(msg_motor.header.stamp.nanosec))
            self.CURRENT_TIME_STEP = TIMESTEP - self.LAST_TIMESTEP
            self.LAST_TIMESTEP = TIMESTEP
            """
            MOTOR_LEFT, MOTOR_RIGHT = msg_motor.motors[0].position, msg_motor.motors[1].position
            self.CURRENT_MOTOR_LEFT, self.CURRENT_MOTOR_RIGHT = MOTOR_LEFT-self.LAST_MOTOR_LEFT, MOTOR_RIGHT-self.LAST_MOTOR_RIGHT
            self.LAST_MOTOR_LEFT, self.LAST_MOTOR_RIGHT = MOTOR_LEFT, MOTOR_RIGHT
            """
        
        
            self.setVelocity(50, 50)
            print(self.x, self.y, self.phi, self.CURRENT_TIME_STEP, self.counter)
            
            self.all_x.append(self.x)
            self.all_y.append(self.y)
        if self.counter == 100:
            plt.plot(self.all_x, self.all_y)
            file_path = 'test.png'
            plt.savefig(file_path)
            exit()
        
        self.counter += 1
        #print(msg_lidar)



def main(args=None):
    rclpy.init(args=args)
    navigation = NavigationNode()
    rclpy.spin(navigation)

    navigation.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()


"""
def drive(x, y, phi, end_x, end_y):
     X_ARR, Y_ARR = [], []
     while True:
        #robot.step(timestep)
        psi = getDirection(x, y, end_x, end_y)
        delta_phi = getDeltaPhi(LAMBDA_TAR, phi, psi)
        v = getVelocity(delta_phi)
        setVelocity(-v+LAMBDA, v+LAMBDA)
        x, y, phi = updateMovement(x, y, phi)
        X_ARR.append(x), Y_ARR.append(y)
"""