import rclpy
import random
from rclpy.node import Node
from geometry_msgs.msg import Twist
from avai_messages.msg import Motors
from avai_messages.msg import Motor
from avai_messages.msg import VehicleLights
class control_pub(Node):
    def __init__(self):
        super().__init__('control_pub')
        #rospy.init_node('control_sub', anonymous=False)
        self.publisher_ = self.create_publisher(VehicleLights,"/vehicle_led", 10)
        self.timer_period = 1  # seconds
        self.timer = self.create_timer(self.timer_period, self.timer_callback)
        self.linear_velocity = 0.0
        self.max_velocity = 200.0  # maximum velocity, adjust as needed

    def timer_callback(self):
        msg = VehicleLights()
        self.linear_velocity += 10  # increase linear velocity
        if self.linear_velocity > self.max_velocity:
            self.linear_velocity = self.max_velocity
        
        #msg.velocity = int(self.linear_velocity)
        #msg.linear.x = self.linear_velocity
        #msg.angular.z = self.linear_velocitys
        #mot.velocity = int(self.linear_velocity)
        msg.left_motor = bool(random.getrandbits(1))
        msg.right_motor = bool(random.getrandbits(1))
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg)

def main(args=None):
    rclpy.init(args=args)
    velocity_publisher = control_pub()
    rclpy.spin(velocity_publisher)
    velocity_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

