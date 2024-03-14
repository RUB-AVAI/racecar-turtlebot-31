import cv2
import rclpy
import os
import numpy as np
import argparse

# ROS2 imports
from rclpy.node import Node
from avai_messages.msg import BoundingBox, YoloOutput
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy


# YOLO model imports
import yolov5.models.common


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--fps", help="number of yolo predictions per second. When not set it will default to 2", default=6, type=int)
parser.add_argument("-b", "--bb", help="number of images with overlayed bounding boxes published per second. When not set it will not publish any", type=int)
args = parser.parse_args()


# Global Variables
TOPIC = "/cone_classification"
QUEUE_SIZE = 10

if args.fps < 1:
    raise ValueError("Argument has to be greater or equal 1")

PUBLISH = (args.fps is not None)
SAVE_IMAGE_RAW = False
SAVE_IMAGE_WITH_BOUNDING_BOXES = False
PUBLISH_IMAGE_WITH_BOUNDING_BOXES = (args.bb is not None)

    

FPS_PUBLISH = args.fps #seconds
FPS_IMAGE_SAVING_RAW = 0.2
FPS_IMAGE_SAVING_BOUNDING_BOXES = FPS_IMAGE_SAVING_RAW
FPS_IMAGE_PUBLISH_BB = args.bb

IMSAVE_PATH_RAW = os.path.dirname(os.path.realpath(__file__)) + "/../../visualisations/camera_image_raw.png"
IMSAVE_PATH_BOUNDING_BOXES = os.path.dirname(os.path.realpath(__file__)) + "/../../visualisations/camera_image_with_bounding_boxes.png"
MODEL_PATH = "/home/ubuntu/turtlebot-avai/src/group31_pkg/src/model/small_best-int8_edgetpu.tflite"



class CamImageProcessingNode(Node):
    def __init__(self, capture):
        super().__init__("CamImageProcessingNode")

        if SAVE_IMAGE_WITH_BOUNDING_BOXES and not PUBLISH:
            self.get_logger().error("cannot save images with bounding boxes without publishing")
            exit()


        self.capture = capture
        self.i = 0
        self.camera_frame = None
        self.camera_frame_stamp = None
        self.bridge = CvBridge()

        self.current_yolo_frame = None
        self.current_yolo_output = None

        #YOLO model
        if PUBLISH:
            self.interpreter = yolov5.models.common.DetectMultiBackend(MODEL_PATH)
            self.interpreter = yolov5.models.common.AutoShape(self.interpreter)
        
        # initialize publisher
        self.publisher_ = self.create_publisher(YoloOutput, TOPIC, qos_profile=rclpy.qos.qos_profile_sensor_data)
        self.publisher_image_bb = self.create_publisher(Image, "/bb_images", qos_profile=rclpy.qos.qos_profile_services_default)
        
        if PUBLISH:
            # initialize publisher callback
            self.publish_callback = self.create_timer(1.0 / FPS_PUBLISH, self.publish)

        if SAVE_IMAGE_RAW:
            # initialize image save callback
            self.image_save_callback = self.create_timer(1.0 / FPS_IMAGE_SAVING_RAW, self.save_image_raw)
        
        if SAVE_IMAGE_WITH_BOUNDING_BOXES:
            self.image_save_bb_callback = self.create_timer(1.0 / FPS_IMAGE_SAVING_BOUNDING_BOXES, self.save_image_with_bounding_boxes)
        
        if PUBLISH_IMAGE_WITH_BOUNDING_BOXES:
            self.image_pub_bb_callback = self.create_timer(1.0 / FPS_IMAGE_PUBLISH_BB, self.publish_image_with_bounding_boxes)

        
        
    def capture_image(self):
        if self.capture.isOpened():
            # read image data
            ret, frame = self.capture.read()

            # save image to variable
            if ret:
                self.camera_frame = frame
                self.camera_frame_stamp = self.get_clock().now()
            else:
                print("capture_image(): no image read")
        else:
            print("No stream opened")
            
    
    def publish(self):
        # publish yolo output
        self.capture_image()
        if self.camera_frame is not None:
            yolo_output = self.yolo(self.camera_frame, self.camera_frame_stamp)
            self.publisher_.publish(yolo_output)
            self.get_logger().info('%d Yolo Predictions Published' % self.i)
            self.i += 1 # image counter increment
        else:
            self.get_logger().warning("Found no frame to publish")


    def publish_image_with_bounding_boxes(self):
        # lay the bounding boxes over the camera image and save it to the visualisations folder
        image = self.current_yolo_frame
        detections = self.current_yolo_output
        if image is not None:
            for det in detections:
                class_id = det.cone
                confidence = det.confidence
                
                # Draw rectangle
                cv2.rectangle(image, (int(det.min_x), int(det.min_y)), (int(det.max_x), int(det.max_y)), (0, 255, 0), 2)
                
                # Draw label (if class_labels is provided)
                class_labels = ["blue", "orange", "yellow"]
                if class_labels and class_id < len(class_labels):
                    label = f"{class_labels[class_id]}: {confidence:.2f}"
                    cv2.putText(image, label, (int(det.min_x), int(det.min_y) - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
            
            msg = self.bridge.cv2_to_imgmsg(image, "bgr8")
            self.publisher_image_bb.publish(msg)
            self.get_logger().info("Published Image with bounding boxes")
            

        else:
            self.get_logger().warning("Found no yolo frame to publish")

    def save_image_raw(self):
        # save the raw image from the camera to the visualisations folder
        frame = self.camera_frame
        frame = self.add_vertical_lines(frame)
        if frame is not None:
            cv2.imwrite(IMSAVE_PATH_RAW, frame)
        else:
            self.get_logger().warning("Found no frame to save")

    def save_image_with_bounding_boxes(self):
        # lay the bounding boxes over the camera image and save it to the visualisations folder
        image = self.current_yolo_frame
        detections = self.current_yolo_output
        if image is not None:
            for det in detections:
                class_id = det.cone
                confidence = det.confidence
                
                # Draw rectangle
                cv2.rectangle(image, (int(det.min_x), int(det.min_y)), (int(det.max_x), int(det.max_y)), (0, 255, 0), 2)
                
                # Draw label (if class_labels is provided)
                class_labels = ["blue", "orange", "yellow"]
                if class_labels and class_id < len(class_labels):
                    label = f"{class_labels[class_id]}: {confidence:.2f}"
                    cv2.putText(image, label, (int(det.min_x), int(det.min_y) - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
            
            cv2.imwrite(IMSAVE_PATH_BOUNDING_BOXES, image)
            

        else:
            self.get_logger().warning("Found no yolo frame to save")

    def yolo(self, input_img:np.ndarray, timestamp):
        raw_img = cv2.resize(input_img, (640, 640))
        raw_img_bgb = cv2.cvtColor(raw_img, cv2.COLOR_BGR2RGB)
        
        detect = self.interpreter(raw_img_bgb)

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

        # save frame and output to display/ save image for debugging purposes
        self.current_yolo_output = output_boxes
        self.current_yolo_frame = raw_img        

        # create object to publish
        output = YoloOutput()
        output.header.stamp = timestamp.to_msg()
        output.header.frame_id = f"{self.i}"
        output.bounding_boxes = output_boxes
        return output
    
    def add_vertical_lines(self, img, num_lines = 61, classifications = None):
        # adds vertical lines to an image 
        if classifications is None:
            classifications = [-1] * num_lines
        
        colors = [(0, 0, 255), (255,140,0), (255, 255, 0), (0, 0, 0)] # blue orange yellow green

        height, width = img.shape[:2]
        
        # Calculate the spacing between lines
        spacing = width / (num_lines + 1)
        
        # Draw the lines
        for i in range(num_lines):
            x = int((i + 1) * spacing)
            cv2.line(img, (x, 0), (x, height), colors[classifications[i]], 1)  # Red line

        
        return img

def main(args=None):
    # create video capture object
    capture = cv2.VideoCapture(0)

    # init node
    rclpy.init(args=args)

    cam_image_processing_node = CamImageProcessingNode(capture)
    rclpy.spin(cam_image_processing_node)

    # shut down node and releases everything
    cam_image_processing_node.destroy_node()
    rclpy.shutdown()
    capture.release()


if __name__ == "__main__":
    main()