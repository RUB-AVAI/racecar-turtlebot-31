import cv2
import rclpy
import os
import numpy as np
from cv_bridge import CvBridge

# ROS2 imports
from rclpy.node import Node
from sensor_msgs.msg import Image

# YOLO model imports
import yolov5.models.common


# Global Variables
TOPIC = "/camera"
QUEUE_SIZE = 1
PERIOD = 1.0/10 #seconds


SAVE_IMAGE = True
IMSAVE_FPS = 5
IMSAVE_PATH = os.path.dirname(os.path.realpath(__file__)) + "/../../visualisations/camera_image.png"
MODEL_PATH = "/home/ubuntu/turtlebot-avai/src/group31_pkg/src/model/best-int8_edgetpu.tflite"
LABEL_PATH = "/home/ubuntu/turtlebot-avai/src/group31_pkg/src/model/labels.yaml"


def do_overlap(box1, box2):
    """Check if two boxes overlap."""
    if box1[0] > box2[2] or box2[0] > box1[2]:
        return False
    if box1[3] < box2[1] or box2[3] < box1[1]:
        return False
    return True

def merge_boxes(box1, box2):
    """Merge two bounding boxes."""
    xmin = min(box1[0], box2[0])
    ymin = min(box1[1], box2[1])
    xmax = max(box1[2], box2[2])
    ymax = max(box1[3], box2[3])
    # Assuming the confidence of the merged box is the max of the two
    confidence = max(box1[4], box2[4])
    return [xmin, ymin, xmax, ymax, confidence, box1[5], box1[6]]


 
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
        self.threshhold = 0.9
        
        #YOLO model
        self.interpreter = yolov5.models.common.DetectMultiBackend(MODEL_PATH, data=LABEL_PATH)
        self.interpreter = yolov5.models.common.AutoShape(self.interpreter)
        
        
        
    def yolo(self, img:np.ndarray):
        img = cv2.resize(img, (640, 640))
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        detect = self.interpreter(img)

        # xmin, ymin, xmax, ymax, confidence, class, name
        boxes = detect.pandas().xyxy[0].to_numpy()
        boxes = boxes[boxes[:,4]>self.threshhold]
        boxes = boxes[:, 0:5]

        merged_boxes = []
        skip_indices = set()

        for i, box1 in enumerate(boxes):
            if i in skip_indices:
                continue

            merge_needed = False
            for j, box2 in enumerate(boxes):
                if i != j and do_overlap(box1, box2):
                    merged_box = merge_boxes(box1, box2)
                    merge_needed = True
                    skip_indices.add(j)
                    box1 = merged_box  # Update box1 to the merged box for further merging

            if merge_needed:
                merged_boxes.append(box1)

        return merged_boxes
    
    def timer_callback(self):
        if self.capture.isOpened():
            # read image data
            ret, frame = self.capture.read()
            boxes = self.yolo(frame)  

            if ret:
                #msg = self.bridge.cv2_to_imgmsg(frame)
                #self.publisher_.publish(msg)
                self.publisher_.publish(boxes)
            
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