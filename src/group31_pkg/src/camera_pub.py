import cv2
import rclpy
import os
import numpy as np

# ROS2 imports
from rclpy.node import Node
from avai_messages.msg import BoundingBox, YoloOutput

# YOLO model imports
import yolov5.models.common


# Global Variables
TOPIC = "/cone_classification"
QUEUE_SIZE = 1
PERIOD = 1.0/10 #seconds
SAVE_IMAGE = True
IMSAVE_FPS = 5
IMSAVE_PATH = os.path.dirname(os.path.realpath(__file__)) + "/../../visualisations/camera_image.png"
MODEL_PATH = "/home/ubuntu/turtlebot-avai/src/group31_pkg/src/model/best-int8_edgetpu.tflite"

 
class CameraPublisher(Node):
    """
    Camera Publisher Class.

    This class contains all methods to publish camera data and info in ROS 2 
    topic in sensor_msgs.msg/Image format. 
    """

    def __init__(self, capture):
        super().__init__("cone_publisher")
        
        # initialize publisher
        self.publisher_ = self.create_publisher(YoloOutput, TOPIC, QUEUE_SIZE)
        self.timer = self.create_timer(PERIOD, self.timer_callback)

        if SAVE_IMAGE:
            self.timer = self.create_timer(1.0 / IMSAVE_FPS, self.image_save_callback)

        self.capture = capture
        self.i = 0
        
        #YOLO model
        self.interpreter = yolov5.models.common.DetectMultiBackend(MODEL_PATH)
        self.interpreter = yolov5.models.common.AutoShape(self.interpreter)
        
        
    def yolo(self, input_img:np.ndarray):
        raw_img = cv2.resize(input_img, (640, 640))
        raw_img = cv2.cvtColor(raw_img, cv2.COLOR_BGR2RGB)
        detect = self.interpreter(raw_img)

        # xmin, ymin, xmax, ymax, confidence, class, name
        boxes = detect.pandas().xyxy[0].to_numpy()
        boxes = boxes[:, 0:6]
        
        output_boxes = []
        for box in boxes:
            output_boxes.append(
                BoundingBox( 
                    min_x=box[0],
                    min_y=box[1],
                    max_x=box[2],
                    max_y=box[3],
                    confidence=box[4],
                    cone=box[5]
                )
            )
        
        output = YoloOutput()
        output.header.stamp = self.get_clock().now().to_msg()
        output.header.frame_id = f"{self.i}"
        output.bounding_boxes = output_boxes
        return output
    
    def timer_callback(self):
        if self.capture.isOpened():
            # read image data
            ret, frame = self.capture.read()
            boxes = self.yolo(frame)  

            if ret:
                self.publisher_.publish(boxes)
                self.get_logger().info('%d Images Published' % self.i)
        
        self.i += 1 # image counter increment

    
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