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

PUBLISH = False

SAVE_IMAGE_RAW = True
SAVE_IMAGE_WITH_BOUNDING_BOXES = False

    

FPS_PUBLISH = 1.0 #seconds
FPS_IMAGE_CAPTURE = 2
FPS_IMAGE_SAVING_RAW = 0.2
FPS_IMAGE_SAVING_BOUNDING_BOXES = FPS_IMAGE_SAVING_RAW

IMSAVE_PATH_RAW = os.path.dirname(os.path.realpath(__file__)) + "/../../visualisations/camera_image_raw.png"
IMSAVE_PATH_BOUNDING_BOXES = os.path.dirname(os.path.realpath(__file__)) + "/../../visualisations/camera_image_with_bounding_boxes.png"
MODEL_PATH = "/home/ubuntu/turtlebot-avai/src/group31_pkg/src/model/best-int8_edgetpu.tflite"



class CameraPublisher(Node):
    """
    Camera Publisher Class.

    This class contains all methods to publish camera data and info in ROS 2 
    topic in sensor_msgs.msg/Image format. 
    """

    def __init__(self, capture):
        super().__init__("cone_publisher")

        if SAVE_IMAGE_WITH_BOUNDING_BOXES and not PUBLISH:
            self.get_logger().error("cannot save images with bounding boxes without publishing")
            exit()


        self.capture = capture
        self.i = 0
        self.camera_frame = None

        self.current_yolo_frame = None
        self.current_yolo_output = None

        #YOLO model
        if PUBLISH:
            self.interpreter = yolov5.models.common.DetectMultiBackend(MODEL_PATH)
            self.interpreter = yolov5.models.common.AutoShape(self.interpreter)
        
        # initialize publisher
        self.publisher_ = self.create_publisher(YoloOutput, TOPIC, QUEUE_SIZE)

        # initialize image capture callback
        self.image_capture_callback = self.create_timer(1.0 / FPS_IMAGE_CAPTURE, self.capture_image)
        
        if PUBLISH:
            # initialize publisher callback
            self.publish_callback = self.create_timer(1.0 / FPS_PUBLISH, self.publish)

        if SAVE_IMAGE_RAW:
            # initialize image save callback
            self.image_save_callback = self.create_timer(1.0 / FPS_IMAGE_SAVING_RAW, self.save_image_raw)
        
        if SAVE_IMAGE_WITH_BOUNDING_BOXES:
            self.image_save_bb_callback = self.create_timer(1.0 / FPS_IMAGE_SAVING_BOUNDING_BOXES, self.save_image_with_bounding_boxes)

        
        
    def capture_image(self):
        if self.capture.isOpened():
            # read image data
            ret, frame = self.capture.read()

            # save image to variable
            if ret:
                self.camera_frame = frame
            
    
    def publish(self):
        if self.camera_frame is not None:
            boxes = self.yolo(self.camera_frame)
            self.publisher_.publish(boxes)
            self.get_logger().info('%d Images Published' % self.i)
            self.i += 1 # image counter increment
        else:
            self.get_logger().warning("Found no frame to publish")


    def save_image_raw(self):
        frame = self.camera_frame
        frame = self.add_vertical_lines(frame)
        if frame is not None:
            cv2.imwrite(IMSAVE_PATH_RAW, frame)
        else:
            self.get_logger().warning("Found no frame to save")


    def save_image_with_bounding_boxes(self):
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


    def yolo(self, input_img:np.ndarray):
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
        output.header.stamp = self.get_clock().now().to_msg()
        output.header.frame_id = f"{self.i}"
        output.bounding_boxes = output_boxes
        return output
    
    def add_vertical_lines(self, img, num_lines = 61, classifications = None):

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

    camera_publisher = CameraPublisher(capture)
    rclpy.spin(camera_publisher)

    # shut down node and releases everything
    camera_publisher.destroy_node()
    rclpy.shutdown()
    capture.release()


if __name__ == "__main__":
    main()