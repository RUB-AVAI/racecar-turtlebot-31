import os
from utils import get_timestamp_as_float
import rclpy
import numpy as np
import matplotlib.pyplot as plt
from rclpy.node import Node
from avai_messages.msg import YoloOutput, BoundingBox, ClusteredLidarData

#camera fov:
FOV = (150, 210)

class DataFusionNode(Node):
    def __init__(self):
        super().__init__('data_fusion_node')

        self.clustered_lidar_subscription = self.create_subscription(ClusteredLidarData, "/clusterered_lidar_data", self.clustered_lidar_listener_callback, rclpy.qos.qos_profile_sensor_data)
        self.yolo_output_subscription = self.create_subscription(YoloOutput, "/cone_classification", self.yolo_output_listener_callback, rclpy.qos.qos_profile_sensor_data)


        self.buffer_size = 100
        self.yolo_msgs = [None] * self.buffer_size
        self.yolo_msgs_idx = 0
        self.cluster_msgs = [None] * self.buffer_size
        self.cluster_msgs_idx = -1
        self.pos_msgs = [None] * self.buffer_size
        self.pos_msgs_idx = -1
    

    def clustered_lidar_listener_callback(self, msg):
        self.get_logger().info("Clustered Lidar Data Received")
        self.cluster_msgs_idx += 1
        self.cluster_msgs[self.cluster_msgs_idx % self.buffer_size] = msg
        

    def yolo_output_listener_callback(self, msg):
        self.get_logger().info("Yolo Output Received")
        self.yolo_msgs_idx += 1
        self.yolo_msgs[self.yolo_msgs_idx % self.buffer_size] = msg

        y, c = self.merge_by_timestamp()
        if y is not None:
            fused_msgs = self.fuse_data(y, c)
            for f in fused_msgs:
                 print(f[0].cone, f[1])
            exit()


    def position_listener_callback(self, msg):
            self.get_logger().info("Position Received")
            self.pos_msgs_idx += 1
            self.pos_msgs[self.pos_msgs_idx % self.buffer_size] = msg
    
    def merge_by_timestamp(self):
        yolo_msg = self.yolo_msgs[self.yolo_msgs_idx]
        # because of the inference of the yolo model, we search the other messages for the appropriate timestamp
        epsilon = 1 #TODO: make more precise
        yolo_timestamp = get_timestamp_as_float(yolo_msg)

        # find nearest cluster message
        for i in range(self.buffer_size):
             msg = self.cluster_msgs[(self.cluster_msgs_idx - i) % self.buffer_size]
             if msg is None:
                  return None, None
             timestamp = get_timestamp_as_float(msg)
             if timestamp <= yolo_timestamp:
                return yolo_msg, msg
        
        return None, None
    
    def fuse_data(self, yolo_msg, cluster_msg):
        clusters_in_fov = []
        for cluster in cluster_msg.clusters:
             if (150 <= cluster.angles[0] and cluster.angles[0] <= 210) or (150 <= cluster.angles[-1] and cluster.angles[-1] <= 210):
                  clusters_in_fov.append(cluster)
        
        fused_msgs = []
        for box in yolo_msg.bounding_boxes:
             for cluster in clusters_in_fov:
                  print(cluster.angles)
                  cluster_left = (cluster.angles[-1] - 180) / 30
                  cluster_right = (cluster.angles[0] - 180) / 30
                  box_left = (box.min_x - 320) / 640
                  box_right = (box.max_x - 320) / 640

                  print(cluster_left, cluster_right, box_left, box_right)
                #   if(box.min_x <= cluster_center_y and cluster_center_y  <= box.max_x):
                #        fused_msgs.append((box, cluster))
             exit()
        return fused_msgs
                       
        
        
        




def main(args=None):
    rclpy.init(args=args)
    data_fusion_node = DataFusionNode()
    rclpy.spin(data_fusion_node)

    data_fusion_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()