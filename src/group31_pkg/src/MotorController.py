import rclpy
from rclpy.node import Node
from avai_messages.msg import Motors, Motor
import time
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
        timer_period = 2  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.last_received_motors = Motors(motors= [Motor(position=0, velocity=0), Motor(position=0, velocity=0)])
        #self.last_received_motors = Non
        self.velocity_commands = [((1.0, 1.0), 5),  # (velocity, duration)
                                  ((0.5, -0.5), 3),
                                  ((-1.0, -1.0), 2)]
        self.command_index = 0
        self.start_time = time.time()
        self.path = {'x': [], 'y': []}
    def listener_callback(self, msg):
        self.get_logger().info('Received motors: "%s"' % msg)
        self.last_received_motors = msg

    def timer_callback(self):
        if self.last_received_motors is not None:
            # Example: Increase the velocity by a certain amount or implement your logic
            new_motors = []
            speed = [0,0]
            for motor in self.last_received_motors.motors:
                new_motor = Motor(position=motor.position,velocity=speed.pop())
                new_motors.append(new_motor)
             
                new_msg = Motors(motors=new_motors)
            #new_msg.motors = new_motors
            self.publisher_.publish(new_msg)
            self.get_logger().info('Publishing: "%s"' % new_msg)

def main(args=None):
    rclpy.init(args=args)
    motor_controller = MotorController()
    rclpy.spin(motor_controller)
    motor_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

