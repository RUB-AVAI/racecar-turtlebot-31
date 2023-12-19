import cv2
import rclpy
import numpy as np
from cv_bridge import CvBridge

# ROS2 imports
from rclpy.node import Node
from sensor_msgs.msg import Image

# YOLO model imports
from pycoral.utils.edgetpu import make_interpreter, run_inference
from pycoral.adapters import common
from pycoral.adapters.detect import get_objects


import os
import time


# Global Variables
TOPIC = "/camera"
QUEUE_SIZE = 1
PERIOD = 1.0/10 #seconds


SAVE_IMAGE = True
IMSAVE_FPS = 5
IMSAVE_PATH = os.path.dirname(os.path.realpath(__file__)) + "/../../visualisations/camera_image.png"
 
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

        if SAVE_IMAGE:
            self.timer = self.create_timer(1.0 / IMSAVE_FPS, self.image_save_callback)


        self.capture = capture
        self.bridge = CvBridge()
        self.i = 0
        
        #YOLO model
        self.model = make_interpreter("model/cone-detector_full_integer_quant_edgetpu.tflite", device="usb")
        self.model.allocate_tensors()
        
        self.output_details = self.model.get_output_details()

        
        
        
    def yolo(self, img:np.ndarray):
        top_padding = 80
        bottom_padding = 160 - top_padding
        img = np.pad(img, ((top_padding, bottom_padding), (0, 0), (0, 0)), 'constant')
        img = img.astype(np.uint8)
        
        common.set_input(self.model, img)
        self.model.invoke()   

        output = self.model.get_tensor(self.output_details[0]['index'])
        output = np.squeeze(output)
        
        return output
    
    def timer_callback(self):
        if self.capture.isOpened():
            # read image data
            ret, frame = self.capture.read()

            # potentially add boxes with yolo
            # TODO:
            start_time = time.time() 
            boxes = self.yolo(frame)  
            print(boxes.shape)
            end_time = time.time() 
            execution_time = end_time - start_time  # Calculate the total execution time
            print("Execution time: ", execution_time, "seconds")  
            #exit()


            if ret:
                msg = self.bridge.cv2_to_imgmsg(frame)
                self.publisher_.publish(msg)
            
                self.get_logger().info('%d Images Published' % self.i)
        
        # image counter increment
        self.i += 1

    
    def image_save_callback(self):
        ret, frame = self.capture.read()
        cv2.imwrite(IMSAVE_PATH, frame)


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