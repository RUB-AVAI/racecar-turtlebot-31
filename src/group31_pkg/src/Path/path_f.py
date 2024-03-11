import rclpy
from rclpy.node import Node
from avai_messages.msg import Motors, Motor
import matplotlib.pyplot as plt
import time
import math
import numpy as np
class MotorController(Node):
    def __init__(self):
        super().__init__('motor_controller')
        self.subscription = self.create_subscription(
                Motors, '/motor_position', self.listener_callback, 50)
        # Publisher and Subscriber
        self.publisher_ = self.create_publisher(Motors, '/motor_velocity', 10)

        self.subscription  # prevent unused variable warning
        self.last_time = self.get_clock().now()

        # Robot specific parameters
        self.wheel_distance = 0.16  # distance between wheels in meters
        self.wheel_radius = 0.0275  # radius of the wheels in meters
        #self.last_received_motors = Motors(motors=[Motor(position=0, velocity=0), Motor(position=0, velocity=0)])
        self.last_received_motors = None
        # Initialize odometry variables
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0
        self.last_time = self.get_clock().now()

        # Initialize path for plotting
        self.path = {'x': [0], 'y': [0]}

        # Velocity command sequence (example: [(left_vel, right_vel), ...])
        """
        self.velocity_sequence = [
        (-50, 50), (-50, 50),(50, 50),(50, 50),(50, 50),
        (50, 50),(50, 50),(50, -50), (50, -50),(50, 50),
        (50, 50), (50, 50),(50, 50),(50, 50), (50, 50),
        ]  # velocities in meters per second
        """
        self.velocity_sequence = [
                (25, 25),(25, 25),(25, -25),(25, -25),(25, 25),(25, 25)
                ,(-25, 25),(-25, 25),(25, 25),(25, 25)
                ]  # velocities in meters per second
        self.current_command_index = 0

        # Timer for periodic updates
        timer_period = 2  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def listener_callback(self, msg):
        if self.last_received_motors == None:
            self.last_received_motors = msg
        if self.last_received_motors != None:
            if self.current_command_index < len(self.velocity_sequence):
                left_moved_mm = msg.motors[0].position
                left_now_mm = left_moved_mm - self.last_received_motors.motors[0].position

                right_moved_mm = msg.motors[1].position
                right_now_mm = right_moved_mm - self.last_received_motors.motors[1].position 

                C = (right_now_mm + left_now_mm) / 2
                delta_direction = (right_now_mm - left_now_mm) / self.wheel_distance
                #direction = direction % (2 * np.pi)
                
                new_direction = self.theta
                new_x = self.path['x'][-1] 
                new_y = self.path['y'][-1]

                if np.abs(left_now_mm - right_now_mm) < 5:
                    print("1")
                    new_x = self.path['x'][-1]  - C * np.cos(self.theta) 
                    new_y = self.path['y'][-1]  + C * np.sin(self.theta)
                    
                elif (right_now_mm < 0  and (np.abs(right_now_mm) - np.abs(left_now_mm)) < 5 ) or (left_now_mm < 0  and (np.abs(right_now_mm) - np.abs(left_now_mm)) < 5 ):
                    print("2")
                    new_direction = (self.theta + delta_direction) % (2 * np.pi)
            
                    
                elif (np.abs(left_now_mm) - np.abs(right_now_mm)) < 5:
                    print("3")
                    new_direction = self.theta + delta_direction
                    new_x = self.path['x'][-1] - C * np.cos(new_direction) 
                    new_y = self.path['y'][-1] + C * np.sin(new_direction)


                self.x = new_x
                self.y = new_y

                self.path['x'].append(self.x)
                self.path['y'].append(self.y)
                self.theta = new_direction

                
                self.last_received_motors = msg
        '''
        if self.current_command_index < len(self.velocity_sequence):
            current_time = self.get_clock().now()
            dt = (current_time - self.last_time).nanoseconds / 1e9  # Convert to seconds
            self.last_time = current_time

            left_vel, right_vel = self.velocity_sequence[self.current_command_index]

            v = (left_vel + right_vel) / 2
            omega = (right_vel - left_vel) / self.wheel_distance

            d_x = v * dt * np.cos(self.theta)
            d_y = v * dt * np.sin(self.theta)
            d_theta = omega * dt

            self.x = self.path['x'][-1] + d_x
            self.y = self.path['y'][-1] + d_y

            self.path['x'].append(self.x)
            self.path['y'].append(self.y)

            self.theta = self.theta + d_theta

            self.last_received_motors = msg

            plt.figure()
            plt.plot(self.path['y'], self.path['x'])
            plt.xlabel('X Position')
            plt.ylabel('Y Position')
            plt.title('Robot Path')
            plt.grid(True)
            plt.show()
            time.sleep(0.2)
            plt.close()
            '''
        #self.get_logger().info('Received motors: "%s"' % msg)

    def timer_callback(self):
        if self.last_received_motors != None:
            # If all commands are executed, stop
            if self.current_command_index >= len(self.velocity_sequence):
                '''
                # Calculate rotation matrix for the current orientation
                cos_theta = math.cos(self.theta)
                sin_theta = math.sin(self.theta)
                rotation_matrix = [[cos_theta, sin_theta], [-sin_theta, cos_theta]]

                # Apply rotation to the path
                rotated_path = {'x': [], 'y': []}
                for x, y in zip(self.path['x'], self.path['y']):
                    rotated_x, rotated_y = np.dot(rotation_matrix, [x - self.x, y - self.y])
                    rotated_path['x'].append(rotated_x)
                    rotated_path['y'].append(rotated_y)

                # Plot the rotated path
                    '''
                # Calculate rotation matrix for the current orientation
                cos_theta = math.cos(self.theta)
                sin_theta = math.sin(self.theta)
                rotation_matrix = [[cos_theta, sin_theta], [-sin_theta, cos_theta]]

                # Apply rotation to the path
                rotated_path = {'x': [], 'y': []}
                for x, y in zip(self.path['x'], self.path['y']):
                    rotated_x, rotated_y = np.dot(rotation_matrix, [x - self.x, y - self.y])
                    rotated_path['x'].append(rotated_x)
                    rotated_path['y'].append(rotated_y)

                plt.figure()
                plt.plot(self.path['y'], self.path['x'])
                plt.xlabel('X Position')
                plt.ylabel('Y Position')
                plt.title('Robot Path')
                plt.grid(True)
                plt.savefig('path_x_y.png')
                plt.close()

                plt.figure()
                plt.plot(rotated_path['y'], rotated_path['x'])
                plt.xlabel('X Position')
                plt.ylabel('Y Position')
                plt.title('Robot Path (rotated)')
                plt.grid(True)
                plt.savefig('path_x_y_rotated.png')
                plt.close()  

                print(len(rotated_path['y']))

                new_motors = [Motor(velocity=int(0)),
                        Motor(velocity=int(0))]
                new_msg = Motors(motors=new_motors)
                self.publisher_.publish(new_msg)
                rclpy.shutdown()
                return

            # Get current velocity command
            left_vel, right_vel = self.velocity_sequence[self.current_command_index]
            print(left_vel, right_vel)
            # Publish velocity command
            new_motor_command = Motors()
            new_motor_command.motors = [Motor(position = self.last_received_motors.motors[0].position,velocity=int(left_vel)), 
                    Motor(position=self.last_received_motors.motors[0].position,velocity=int(right_vel))]
            self.publisher_.publish(new_motor_command)

            # Update the index for the next command
            self.current_command_index += 1

            # Log command
            #self.get_logger().info(f'Published velocities: Left = {left_vel}, Right = {right_vel}')

def main(args=None):
    rclpy.init(args=args)
    motor_controller = MotorController()
    rclpy.spin(motor_controller)

    # Clean up
    motor_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()