import numpy as np
import cv2
from cv_bridge import CvBridge
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image


#global variables
TOPIC = "/camera"
QUEUE_SIZE = 1
SHOW_IMAGE = False

class ImageSubscriber(Node):

    def __init__(self):
        super().__init__('image_subscriber')
        self.subscription = self.create_subscription(Image, TOPIC, self.listener_callback, QUEUE_SIZE)
        self.subscription  # prevent unused variable warning
        self.bridge = CvBridge()



    def listener_callback(self, msg):
    
        self.get_logger().info("Image Received")

        if SHOW_IMAGE:
            frame = self.bridge.imgmsg_to_cv2(msg)
            cv2.imshow(TOPIC, frame)
            key = cv2.waitKey(20)
            if key == 27: # exit on ESC
                exit()


def main(args=None):
    cv2.namedWindow(TOPIC)
    rclpy.init(args=args)
    image_subscriber = ImageSubscriber()
    rclpy.spin(image_subscriber)

    cv2.destroyWindow(TOPIC)
    image_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
