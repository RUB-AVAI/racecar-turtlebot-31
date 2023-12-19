import rclpy
from rclpy.node import Node
from avai_messages.msg import Motors, Motor

class MotorPublisher(Node):
    def __init__(self):
        super().__init__('motor_publisher')
        self.publisher_ = self.create_publisher(Motors, '/motor_velocity', 10)
        timer_period = 2  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Motors()
        msg.motors = [Motor(position=100, velocity=1), Motor(position=150, velocity=-1)]
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg)

def main(args=None):
    rclpy.init(args=args)
    motor_publisher = MotorPublisher()
    rclpy.spin(motor_publisher)
    motor_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

