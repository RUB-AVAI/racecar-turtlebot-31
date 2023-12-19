import rclpy
from rclpy.node import Node
from avai_messages.msg import Motors, Motor
import matplotlib.pyplot as plt
import time
import math

class MotorController(Node):
    def __init__(self):
        super().__init__('motor_controller')
        self.publisher_ = self.create_publisher(Motors, '/motor_velocity', 10)
        self.subscription = self.create_subscription(
            Motors,
            '/motor_velocity',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        # Initialize odometry variables
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0
        self.last_received_motors = Motors(motors=[Motor(position=0, velocity=0), Motor(position=0, velocity=0)])
        self.last_time = self.get_clock().now()
        
        # Velocity commands and path recording
        self.velocity_commands = [((1.0, 1.0), 5),  # (velocity, duration)
                                  ((0.5, -0.5), 3),
                                  ((-1.0, -1.0), 2)]
        self.command_index = 0
        self.start_time = time.time()
        self.path = {'x': [], 'y': []}

        # Flag to indicate when to stop the node
        self.should_stop = False

        # Timer for periodic updates
        timer_period = 2  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def listener_callback(self, msg):
        #self.get_logger().info('Received motors: "%s"' % msg)
        self.last_received_motors = msg

    def timer_callback(self):
        current_time = self.get_clock().now()
        dt = (current_time - self.last_time).nanoseconds / 1e9  # Convert to seconds
        self.last_time = current_time

        # Update odometry
        left_wheel_vel = self.last_received_motors.motors[0].velocity
        right_wheel_vel = self.last_received_motors.motors[1].velocity
        wheel_base = 0.5  # distance between wheels, adjust as necessary

        # Calculate change in position
        delta_s = (right_wheel_vel + left_wheel_vel) / 2.0 * dt
        delta_theta = (right_wheel_vel - left_wheel_vel) / wheel_base * dt

        # Update pose
        self.x += delta_s * math.cos(self.theta)
        self.y += delta_s * math.sin(self.theta)
        self.theta += delta_theta

        # Check if the current command is completed
        if self.command_index < len(self.velocity_commands):
            if time.time() - self.start_time > self.velocity_commands[self.command_index][1]:
          
                self.command_index += 1
                self.start_time = time.time()
        elif self.command_index >= len(self.velocity_commands):
            self.should_stop = True  # Set the flag to stop the node
            new_motors = [Motor(position=0, velocity=int(0)),
                              Motor(position=0, velocity=int(0))]
            new_msg = Motors(motors=new_motors)
            self.publisher_.publish(new_msg)
            plt.plot(motor_controller.path['x'], motor_controller.path['y'])
            plt.xlabel('X Position')
            plt.ylabel('Y Position')
            plt.title('Robot Path')
            plt.grid(True)
            plt.savefig('path.png')
            plt.show()
            motor_controller.destroy_node()
            rclpy.shutdown()
            print("stop")
            return  # Exit the callback
            
        # Set motor velocities according to the current command
        if not self.should_stop:
            print(self.command_index)
            current_velocities = self.velocity_commands[self.command_index][0]
            new_motors = [Motor(position=0, velocity=int(current_velocities[0])),
                        Motor(position=0, velocity=int(current_velocities[1]))]
            new_msg = Motors(motors=new_motors)
            self.publisher_.publish(new_msg)
            # Record the current position
            self.path['x'].append(self.x)
            self.path['y'].append(self.y)
        
def main(args=None):
    rclpy.init(args=args)
    motor_controller = MotorController()
    rclpy.spin(motor_controller)

   

    motor_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

