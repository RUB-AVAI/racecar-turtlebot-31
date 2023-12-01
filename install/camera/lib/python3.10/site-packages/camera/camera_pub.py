import cv2
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import numpy as np
from cv_bridge import CvBridge

# Global Variables
TOPIC = "/camera"
QUEUE_SIZE = 1
PERIOD = 1.0/10 #seconds
 
class CameraPublisher(Node):
    """Camera Publisher Class.

    This class contains all methods to publish camera data and info in ROS 2 
    topic in sensor_msgs.msg/Image format. 
    
    """

    def __init__(self, capture):
        super().__init__("camera_publisher")

        # initialize publisher
        self.publisher_ = self.create_publisher(Image, TOPIC, QUEUE_SIZE)
        self.timer = self.create_timer(PERIOD, self.timer_callback)

        self.capture = capture
        self.bridge = CvBridge()
        self.i = 0
    
    def timer_callback(self):
        if self.capture.isOpened():
            # read image data
            ret, frame = self.capture.read()

            # potentially add boxes with yolo
            # TODO:


            if ret:
                msg = self.bridge.cv2_to_imgmsg(frame)
                self.publisher_.publish(msg)
            
                self.get_logger().info('%d Images Published' % self.i)
        
        # image counter increment
        self.i += 1


def main(args=None):
    # create video capture object
    capture = cv2.VideoCapture(0)

    # init node
    rclpy.init(args=args)

    camera_publisher = CameraPublisher(capture)
    rclpy.spin(camera_publisher)

    # shut down node and releases everything
    camera_publisher.destroy_node()
    rclpy.shutdown()
    capture.release()


if __name__ == "__main__":
    main()