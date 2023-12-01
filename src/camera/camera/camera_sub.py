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
SAVE_IMAGE = True
SAVING_FPS = 5


class ImageSubscriber(Node):

    def __init__(self):
        super().__init__('image_subscriber')
        self.subscription = self.create_subscription(Image, TOPIC, self.listener_callback, QUEUE_SIZE)
        self.timer = self.create_timer(1.0 / SAVING_FPS, self.image_save_callback)
        self.subscription  # prevent unused variable warning
        self.bridge = CvBridge()
        self.frame = None



    def listener_callback(self, msg):
    
        self.get_logger().info("Image Received")

        self.frame = self.bridge.imgmsg_to_cv2(msg)

        if SHOW_IMAGE:
            cv2.imshow(TOPIC, self.frame)
            key = cv2.waitKey(20)
            if key == 27: # exit on ESC
                exit()
    
    def image_save_callback(self):
        if self.frame:
            cv2.imwrite("camera.png", self.frame)



def main(args=None):
    # cv2.namedWindow(TOPIC)
    rclpy.init(args=args)
    image_subscriber = ImageSubscriber()
    rclpy.spin(image_subscriber)

    # cv2.destroyWindow(TOPIC)
    image_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
