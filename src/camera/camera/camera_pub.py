import cv2
import rclpy
import numpy as np
from cv_bridge import CvBridge

# ROS2 imports
from rclpy.node import Node
from sensor_msgs.msg import Image

# YOLO model imports
from pycoral.utils import edgetpu
from pycoral.adapters import common, classify, detect


# Global Variables
TOPIC = "/camera"
QUEUE_SIZE = 1
PERIOD = 1.0/10 #seconds
 
class CameraPublisher(Node):
    """
    Camera Publisher Class.

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
        
        #YOLO model
        self.model = edgetpu.make_interpreter("model/cone-detector_float32.tflite")
        self.model.allocate_tensors()
        
        # Get input and output tensors.
        input_details = self.model.get_input_details()
        output_details = self.model.get_output_details()

        # Test the model on random input data.
        input_shape = input_details[0]['shape']
        input_data = np.array(np.random.random_sample(input_shape), dtype=np.float32)
        self.model.set_tensor(input_details[0]['index'], input_data)

        self.model.invoke()

        # The function `get_tensor()` returns a copy of the tensor data.
        # Use `tensor()` in order to get a pointer to the tensor.
        output_data = self.model.get_tensor(output_details[0]['index'])
        print(output_data)
        print(output_data.shape)
        exit()
        
        
    def yolo(self, img:np.ndarray):
        top_padding = 80  # You can adjust this as needed
        bottom_padding = 160 - top_padding
        img = np.pad(img, ((top_padding, bottom_padding), (0, 0), (0, 0)), 'constant')
        
        common.set_input(self.model, img)
        self.model.invoke()
        classes = detect.get_objects(self.model)
        print(classes)
        
        return classes
    
    def timer_callback(self):
        if self.capture.isOpened():
            # read image data
            ret, frame = self.capture.read()

            # potentially add boxes with yolo
            # TODO:
            boxes = self.yolo(frame)
            exit()


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