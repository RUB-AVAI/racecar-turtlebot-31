import os
from utils import *
import time
import rclpy
import numpy as np
import matplotlib.pyplot as plt
from rclpy.node import Node
from avai_messages.msg import YoloOutput, BoundingBox, ClusteredLidarData, Position, Targets

LOG_INFO = False
CLUSTER = 0
POSITION = 1
NAME = "data/data-2"

class CalibrationNode(Node):
    def __init__(self):
        super().__init__("calibration_node")
        self.clustered_lidar_subscription = self.create_subscription(ClusteredLidarData, "/clusterered_lidar_data", self.clustered_lidar_listener_callback, rclpy.qos.qos_profile_sensor_data)
        self.yolo_output_subscription = self.create_subscription(YoloOutput, "/cone_classification", self.yolo_output_listener_callback, rclpy.qos.qos_profile_sensor_data)
        # self.create_timer(1, self.close_and_save)
        
        self.counter = 0
        
        self.buffer_size = 100
        self.yolo_msgs = [None] * self.buffer_size
        self.yolo_msgs_idx = 0
        self.cluster_msgs = [None] * self.buffer_size
        self.cluster_msgs_idx = -1
        
        self.data = []
        
    def close_and_save(self):
        try:
            np_data = np.load(NAME + ".npy")
            np_data = np.concatenate((np_data, np.array(self.data)))
        except OSError:
            np_data = np.array(self.data)
        np.save(NAME, np_data)
        self.destroy_node()
    
    
        
    def clustered_lidar_listener_callback(self, msg):
        if LOG_INFO:
            self.get_logger().info("Clustered Lidar Data Received")
            
        FOV = (140, 220)
        clusters_in_fov = []
        for cluster in msg.clusters:
             if (FOV[0] <= cluster.angles[0] and cluster.angles[0] <= FOV[1]) or (FOV[0] <= cluster.angles[-1] and cluster.angles[-1] <= FOV[1]):
                  clusters_in_fov.append(cluster)
        
        msg.clusters = clusters_in_fov
                
            
            
        self.cluster_msgs_idx += 1
        self.cluster_msgs[self.cluster_msgs_idx % self.buffer_size] = msg
        

    def yolo_output_listener_callback(self, msg):
        if LOG_INFO:
            self.get_logger().info("Yolo Output Received")
        self.yolo_msgs_idx += 1
        self.yolo_msgs[self.yolo_msgs_idx % self.buffer_size] = msg
        
        
        cluster_msg = self.match_message(msg, CLUSTER)
        if cluster_msg is None:
            return
        
        
        boxes = np.array(msg.bounding_boxes)
        clusters = np.array(cluster_msg.clusters)
        
        plot_clusters(clusters)
        
        
        if len(boxes) != len(clusters):
            print(f"number of boxes {len(boxes)} does not match number of clusters ({len(clusters)})")
            return
        
        
        # sort boxes from right to left
        x_coordinates = []
        for box in boxes:
            x_coordinates.append(box.min_x)
        
        boxes = boxes[np.flip(np.argsort(x_coordinates))]
        
        for i, (cluster, box) in enumerate(zip(clusters, boxes)):
            print(f"range: {round(np.mean(cluster.ranges))}, label: {box.cone}")
            self.data.append([np.mean(cluster.ranges), np.mean(cluster.angles), box.min_x, box.max_x, box.min_y, box.max_y])
            
        self.counter += 1
        if self.counter == 3:
            self.close_and_save() 
        
        
    def match_message(self, yolo_msg, type):
        """Because of the inference of the yolo model, the yolo messages arrive later than the other messages. Therefore this function  
         searches the buffer for a message with the corresponding timestamp.
         The type argument specifies to look for cluster or position

        Returns:
            Cluster: Returns the matching Cluster message or None if no matching message was found
        """
        
        if type != CLUSTER and type != POSITION:
            raise KeyError()
            
        # because of the inference of the yolo model, we search the other messages for the appropriate timestamp
        yolo_timestamp = get_timestamp_as_float(yolo_msg)

        # find nearest cluster message
        prev_distance = np.inf
        prev_msg = None
        for i in range(self.buffer_size):
             if type==  CLUSTER:
                 msg = self.cluster_msgs[(self.cluster_msgs_idx - i) % self.buffer_size]
             elif type==POSITION:
                 msg = self.pos_msgs[(self.pos_msgs_idx - i) % self.buffer_size]
             if msg is None:
                 break
             timestamp = get_timestamp_as_float(msg)
             
             distance = np.abs(timestamp - yolo_timestamp)
             if(i>0):
                 if distance > prev_distance:
                     return prev_msg
                 else:
                     prev_distance = distance
                     prev_msg = msg
        return prev_msg
    
def main(args=None):
    rclpy.init(args=args)
    data_fusion_node = CalibrationNode()
    rclpy.spin(data_fusion_node)

    data_fusion_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
        