import rclpy
from rclpy.node import Node
from avai_messages.msg import YoloOutput


#global variables
TOPIC = "/cone_classification"
QUEUE_SIZE = 1
SHOW_IMAGE = False


class ImageSubscriber(Node):
    def __init__(self):
        super().__init__('cone_subscriber')
        self.subscription = self.create_subscription(YoloOutput, TOPIC, self.listener_callback, QUEUE_SIZE)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info("Image Received")
        print(msg)


def main(args=None):
    rclpy.init(args=args)
    image_subscriber = ImageSubscriber()
    rclpy.spin(image_subscriber)

    image_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
