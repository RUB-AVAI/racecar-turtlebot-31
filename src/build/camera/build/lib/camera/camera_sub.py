
import rclpy
from rclpy.node import Node

from std_msgs.msg import Image

import cv2
from cv_bridge import CvBridge
from rcl_interfaces.msg import SetParametersResult

import message_filters

class CameraNodeSub(Node):

    def __init__(self):
        super().__init__('camera_sub')
        self.subscription = self.create_subscription(
            Image,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.bridge = CvBridge()

        self.synchronizer = message_filters.ApproximateTimeSynchronizer([self.image_subscriber, self.bbox_subscriber], 10, 1)
        self.synchronizer.registerCallback(self.synchronized_callback)
        cv2.namedWindow('frame', cv2.WINDOW_NORMAL)

        print("Image Display Node started!")

    def synchronized_callback(self, msg_image):
        self.get_logger().info('Receiving video frame and bounding boxes')
        self.image_display(self.bridge.compressed_imgmsg_to_cv2(msg_image, 'bgr8'))

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)

    def image_display(self, image):
        # annotating image with detected bounding boxes

        annotated_image = cv2.resize(image, (640, 480))
        cv2.imshow('frame', image)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = CameraNodeSub()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
