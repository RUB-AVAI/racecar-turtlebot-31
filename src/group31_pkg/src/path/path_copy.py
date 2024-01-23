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

        # Publisher and Subscriber
        self.publisher_ = self.create_publisher(Motors, '/motor_velocity', 10)
        self.subscription = self.create_subscription(
            Motors, '/motor_velocity', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning

        # Robot specific parameters
        self.wheel_distance = 0.14  # distance between wheels in meters
        self.wheel_radius = 0.0275  # radius of the wheels in meters
        self.last_received_motors = Motors(motors=[Motor(position=0, velocity=0), Motor(position=0, velocity=0)])
        # Initialize odometry variables
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0
        self.last_time = self.get_clock().now()

        # Initialize path for plotting
        self.path = {'x': [0], 'y': [0]}

        # Velocity command sequence (example: [(left_vel, right_vel), ...])
        self.velocity_sequence = [
        (50, 50), (50, 50),(50, 50),(50, 50),(50, -50),
        (50, -50),(50, 50),(50, 50), (50, 50),(50, 50),
        (-50, 50),(-50, 50),(50, 50),
        (50, 50),(50, 50),(50, 50)
        ]  # velocities in meters per second
        self.current_command_index = 0

        # Timer for periodic updates
        timer_period = 2  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def listener_callback(self, msg):
        self.get_logger().info('Received motors: "%s"' % msg)
        self.last_received_motors = msg

    def timer_callback(self):
        # If all commands are executed, stop
        if self.current_command_index >= len(self.velocity_sequence):
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
            plt.figure()
            plt.plot(rotated_path['x'], rotated_path['y'])
            plt.xlabel('X Position')
            plt.ylabel('Y Position')
            plt.title('Robot Path (Rotated View)')
            plt.grid(True)
            plt.savefig('rotated_path.png')
            plt.close()  # Close the figure to prevent it from showing in non-interactive environments
            new_motors = [Motor(position=0, velocity=int(0)),
                    Motor(position=0, velocity=int(0))]
            new_msg = Motors(motors=new_motors)
            self.publisher_.publish(new_msg)
            rclpy.shutdown()
            return

        # Get current velocity command
        left_vel, right_vel = self.velocity_sequence[self.current_command_index]

        # Publish velocity command
        new_motor_command = Motors()
        new_motor_command.motors = [Motor(position=0, velocity=int(left_vel)), Motor(position=0, velocity=int(right_vel))]
        self.publisher_.publish(new_motor_command)

        # Update the index for the next command
        self.current_command_index += 1

        # Log command
        self.get_logger().info(f'Published velocities: Left = {left_vel}, Right = {right_vel}')

        # Odometry Calculation
        current_time = self.get_clock().now()
        dt = (current_time - self.last_time).nanoseconds / 1e9
        self.last_time = current_time

        # Calculate the linear velocity and angular velocity of the robot
        v = (left_vel + right_vel) / 2
        omega = (right_vel - left_vel) / self.wheel_distance

        # Update robot pose
        self.x += v * math.cos(self.theta) * dt
        self.y += v * math.sin(self.theta) * dt
        self.theta += omega * dt

        # Normalize theta
        self.theta = self.theta % (2 * math.pi)

        # Update path
        self.path['x'].append(self.x)
        self.path['y'].append(self.y)

def main(args=None):
    rclpy.init(args=args)
    motor_controller = MotorController()
    rclpy.spin(motor_controller)

    # Clean up
    motor_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
