import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from rclpy.qos import ReliabilityPolicy, QoSProfile, DurabilityPolicy, HistoryPolicy


#global variables
TOPIC = "/scan"
QUEUE_SIZE = 10

class LidarSubscriber(Node):

    def __init__(self):
        super().__init__('lidar_subscriber')

        qos_profile = QoSProfile(reliability=ReliabilityPolicy.BEST_EFFORT, depth=QUEUE_SIZE)

        self.subscription = self.create_subscription(LaserScan, TOPIC, self.listener_callback, rclpy.qos.qos_profile_sensor_data)
        self.subscription  # prevent unused variable warning



    def listener_callback(self, msg):
    
        self.get_logger().info("Data Received")
        # print(msg.data)



def main(args=None):
    rclpy.init(args=args)
    lidar_subscriber = LidarSubscriber()
    rclpy.spin(lidar_subscriber)


    lidar_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()