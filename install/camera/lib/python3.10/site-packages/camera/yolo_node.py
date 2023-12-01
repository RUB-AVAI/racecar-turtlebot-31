import cv2
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from pycoral.utils import edgetpu

# Global Variables
TOPIC = "/yolo"
QUEUE_SIZE = 1
FREQUENCY = 30 # images read per second
 
class YoloNode(Node):
    """
    
    """
    def __init__(self, capture):
        super().__init__("yolo_node")

        # initialize publisher
        # self.publisher_ = self.create_publisher(Image, TOPIC, QUEUE_SIZE)
        self.timer = self.create_timer(1 / FREQUENCY, self.timer_callback)

        self.capture = capture
        self.bridge = CvBridge()
        self.i = 0
        
        #YOLO model
        self.model = edgetpu.make_interpreter("cone-detector_float32.tflite")
        self.model.allocate_tensors()
    
    def timer_callback(self):
        if self.capture.isOpened():
            # read image data
            ret, frame = self.capture.read()
            if ret:
                self.i += 1  # saves the number of frames that was processed in total
                result = self.model.predict(frame) 
                print(result)
                boxes = []
                for r in result:
                    # detection
                    boxes.append(r.boxes.xyxy) # box with xyxy format
                    boxes.append(r.boxes.cls) # (N, 4), cls, (N, 1)
                #self.publisher_.publish(boxes)

def main(args=None):
    # create video capture object
    capture = cv2.VideoCapture(0)

    # init node
    rclpy.init(args=args)

    camera_publisher = YoloNode(capture)
    rclpy.spin(camera_publisher)

    # shut down node and releases everything
    camera_publisher.destroy_node()
    rclpy.shutdown()
    capture.release()


if __name__ == "__main__":
    main()