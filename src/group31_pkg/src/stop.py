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
        # Timer for periodic updates
        timer_period = 2  # seconds
        self.timer_callback()
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        new_motor_command = Motors()
        new_motor_command.motors = [Motor(position = 1,velocity=int(0)), 
                Motor(position=1,velocity=int(0))]
        self.publisher_.publish(new_motor_command)


        # Log command
        self.get_logger().info(f'Published velocities: Left = {0}, Right = {0}')
        

def main(args=None):
    rclpy.init(args=args)
    motor_controller = MotorController()
    rclpy.spin(motor_controller)

    # Clean up
    motor_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()