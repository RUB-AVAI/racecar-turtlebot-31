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
        self.model = make_interpreter("/home/ubuntu/turtlebot-avai/src/group31_pkg/src/model/best-int8_edgetpu.tflite", device="usb")
        self.model.allocate_tensors()
        
        self.output_details = self.model.get_output_details()
        self.threshhold = 110

        
        
        
    def yolo(self, img:np.ndarray):
        img = img.astype(np.uint8)
        img = np.pad(img, ((0, 160), (0, 0), (0, 0)), mode='constant')
    
        common.set_input(self.model, img)
        self.model.invoke()   

        output = self.model.get_tensor(self.output_details[0]['index'])
        output = np.squeeze(output)
        
        mask = np.any(output[:, -3:] > self.threshhold, axis=1)
        filtered_output = output[mask, :]
        print(np.min(output), np.max(output))
        if filtered_output.size == 0:
            return np.asarray([])
        
        class_indices = np.argmax(filtered_output[:, -3:], axis=1).reshape(-1,1)
        max_confidences = filtered_output[:, -3:].max(axis=1).reshape(-1,1)
        coordinates = filtered_output[:, :4]

        output = np.hstack((coordinates, class_indices, max_confidences))

        #print(f"OUTPUT {output}")
        return output
    
    def timer_callback(self):
        if self.capture.isOpened():
            # read image data
            ret, frame = self.capture.read()

            start_time = time.time() 
            boxes = self.yolo(frame)  
            end_time = time.time() 
            execution_time = end_time - start_time  # Calculate the total execution time
            print("Execution time: ", execution_time, "seconds")  


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