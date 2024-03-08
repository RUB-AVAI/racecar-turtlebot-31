import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import os

IMSAVE_PATH_BOUNDING_BOXES = os.path.dirname(os.path.realpath(__file__)) + "/../../visualisations/camera_image_with_bounding_boxes.png"


class ImageReceiverNode(Node):
    def __init__(self):
        super().__init__("image_receiving_node")
        self.bridge = CvBridge()
        self.subscriber = self.create_subscription(Image, "/bb_images", self.callback, qos_profile=rclpy.qos.qos_profile_services_default)
    
    
    def callback(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        cv2.imwrite(IMSAVE_PATH_BOUNDING_BOXES, cv_image)
        self.get_logger().info("Received and saved image")
        

def main(args=None):
    rclpy.init(args=args)
    lidar_processing_node = ImageReceiverNode()
    rclpy.spin(lidar_processing_node)


    lidar_processing_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()