import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
import numpy as np

class CameraNode(Node):

    def __init__(self):
        super().__init__('camera_node')
        self.publisher_ = self.create_publisher(Image, 'camera/image_raw', 10)
        self.timer_period = 0.1  # 10Hz
        self.timer = self.create_timer(self.timer_period, self.timer_callback)
        self.cap = cv2.VideoCapture(0)  # Open default camera, change index for other cameras

    def timer_callback(self):
        ret, frame = self.cap.read()
        if not ret:
            self.get_logger().warn('No frame captured from camera')
            return
        
        # Convert OpenCV image to ROS Image message
        image_msg = Image()
        image_msg.header.stamp = self.get_clock().now().to_msg()
        image_msg.height = frame.shape[0]
        image_msg.width = frame.shape[1]
        image_msg.encoding = 'bgr8'  # Assuming a standard BGR format for OpenCV capture
        image_msg.data = frame.tobytes()

        self.publisher_.publish(image_msg)

def main(args=None):
    rclpy.init(args=args)
    camera_node = CameraNode()
    rclpy.spin(camera_node)
    camera_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
