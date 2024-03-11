import rclpy
from rclpy.node import Node
from avai_messages.msg import Motors, Motor
import matplotlib.pyplot as plt
import time
import math
# ros2 topic pub /motor_velocity avai_messages/Motors "{motors: [{position: 100, velocity: 0}, {position: 150, velocity: 0}]}"
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
        '''
        self.velocity_commands = [((50.0, 50.0), 7),  # (velocity, duration)
                                  ((20, -20), 4),
                                  ((-40.0, -40.0), 5)]
        '''
        self.velocity_commands = [((50.0, 50.0), 7),  # (velocity, duration)
                                  ((50.0, -50.0), 4),
                                  ((-50.0, -50.0), 7)]
        self.command_index = 0
        self.start_time = time.time()
        self.path = {'x': [], 'y': []}

        # Timer for periodic updates
        timer_period = 2  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def listener_callback(self, msg):
        self.get_logger().info('Received motors: "%s"' % msg)
        self.last_received_motors = msg

    def timer_callback(self):
        current_time = self.get_clock().now()
        dt = (current_time - self.last_time).nanoseconds / 1e9  # Convert to seconds
        self.last_time = current_time

        # Update odometry
        left_wheel_vel = self.last_received_motors.motors[0].velocity
        right_wheel_vel = self.last_received_motors.motors[1].velocity
        wheel_base = 0.14  # distance between wheels, adjust as necessary 14cm, wheel diameter 5.5cm, before 0.5

        # Calculate change in position
        delta_s = (right_wheel_vel + left_wheel_vel) / 2.0 * dt
        delta_theta = (right_wheel_vel - left_wheel_vel) / wheel_base * dt

        # Update pose
        self.x += delta_s * math.cos(self.theta)
        self.y += delta_s * math.sin(self.theta)
        self.theta += delta_theta

        if time.time() - self.start_time > self.velocity_commands[self.command_index][1]:
            self.command_index += 1
            #self.set_heading(90)
            if self.command_index >= len(self.velocity_commands):
                plt.plot(self.path['x'], self.path['y'])
                plt.xlabel('X Position')
                plt.ylabel('Y Position')
                plt.title('Robot Path')
                plt.grid(True)
                plt.savefig('path.png')
                new_motors = [Motor(position=0, velocity=int(0)),
                      Motor(position=0, velocity=int(0))]
                new_msg = Motors(motors=new_motors)
                self.publisher_.publish(new_msg)
                rclpy.shutdown()
            self.start_time = time.time()

        # Set motor velocities according to the current command
        current_velocities = self.velocity_commands[self.command_index][0]
        new_motors = [Motor(position=0, velocity=int(current_velocities[0])),
                      Motor(position=0, velocity=int(current_velocities[1]))]
        new_msg = Motors(motors=new_motors)
        self.publisher_.publish(new_msg)

        # Record the current position
        self.path['x'].append(self.x)
        self.path['y'].append(self.y)

    def set_heading(self, desired_heading):
        # PD controller constants
        Kp = 5  # Proportional gain
        Kd = 0.3  # Derivative gain

        desired_heading = math.radians(desired_heading)

        Kp = 0.5  # Proportional gain, adjust as necessary
        Kd = 0.1  # Derivative gain, adjust as necessary

        wheel_base = 0.14  # The distance between the wheels in meters

        previous_error = 0.0
        loop_rate = 0.1  # Time interval for each iteration in seconds

        max_speed = 80
        while rclpy.ok():
            current_time = self.get_clock().now()
            dt = (current_time - self.last_time).nanoseconds / 1e9  # Convert to seconds
            self.last_time = current_time

            # Calculate the heading error
            error = desired_heading - self.theta
            error = math.atan2(math.sin(error), math.cos(error))  # Normalize error to [-pi, pi]

            # PD control for heading correction
            derivative = (error - previous_error) / dt
            control = Kp * error + Kd * derivative

            # Limit the control to the maximum speed
            control = max(min(control, max_speed), -max_speed)

            # Calculate wheel velocities for turning
            left_wheel_vel = control
            right_wheel_vel = -control

            # Update the motor velocities
            new_motors = [Motor(position=0, velocity=int(left_wheel_vel)),
                          Motor(position=0, velocity=int(right_wheel_vel))]
            new_msg = Motors(motors=new_motors)
            self.publisher_.publish(new_msg)

            # Update heading
            angular_velocity = (right_wheel_vel - left_wheel_vel) / wheel_base
            self.theta += angular_velocity * dt  # Update theta based on angular velocity and time elapsed
            self.theta = math.atan2(math.sin(self.theta), math.cos(self.theta))  # Normalize theta to [-pi, pi]

            previous_error = error

            # Check if the heading is close to the desired heading
            if abs(error) < 0.05:  # tolerance in radians
                print("good")
                break

            # Sleep for a bit before next iteration
            #time.sleep(0.1)

def main(args=None):
    rclpy.init(args=args)
    motor_controller = MotorController()
    rclpy.spin(motor_controller)

    motor_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()