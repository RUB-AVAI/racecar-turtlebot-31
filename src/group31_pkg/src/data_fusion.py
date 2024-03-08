import os
from utils import get_timestamp_as_float, is_range_in_range, Map, estimate_cone_position, center_of_range, preprocess_bounding_boxes
import rclpy
import numpy as np
import matplotlib.pyplot as plt
from rclpy.node import Node
from avai_messages.msg import YoloOutput, BoundingBox, ClusteredLidarData, Position

#camera fov:
FOV = (148, 212)
CLUSTER = 0
POSITION = 1

class DataFusionNode(Node):
    def __init__(self):
        super().__init__('data_fusion_node')

        self.clustered_lidar_subscription = self.create_subscription(ClusteredLidarData, "/clusterered_lidar_data", self.clustered_lidar_listener_callback, rclpy.qos.qos_profile_sensor_data)
        self.yolo_output_subscription = self.create_subscription(YoloOutput, "/cone_classification", self.yolo_output_listener_callback, rclpy.qos.qos_profile_sensor_data)
        self.pos_subscription = self.create_subscription(Position, "/position", self.position_listener_callback, rclpy.qos.qos_profile_sensor_data)
        
        self.map = Map()
        
        self.buffer_size = 100
        self.yolo_msgs = [None] * self.buffer_size
        self.yolo_msgs_idx = 0
        self.cluster_msgs = [None] * self.buffer_size
        self.cluster_msgs_idx = -1
        self.pos_msgs = [None] * self.buffer_size
        self.pos_msgs_idx = -1
        
        self.default_position = Position()
        self.default_position.x_position=0.0 # in mm
        self.default_position.y_position=0.0 # in mm
        self.default_position.facing_direction=0.0 # in degrees
    

    def clustered_lidar_listener_callback(self, msg):
        self.get_logger().info("Clustered Lidar Data Received")
        self.cluster_msgs_idx += 1
        self.cluster_msgs[self.cluster_msgs_idx % self.buffer_size] = msg
        

    def yolo_output_listener_callback(self, msg):
        self.get_logger().info("Yolo Output Received")
        # for box in msg.bounding_boxes:
        #     delta_x = np.abs(box.min_x - box.max_x)
        #     delta_y = np.abs(box.min_y - box.max_y)
        #     print(f"ratio for {box.cone}: {delta_y / delta_x}")
        msg = preprocess_bounding_boxes(msg, log_to_console=True)
        self.yolo_msgs_idx += 1
        self.yolo_msgs[self.yolo_msgs_idx % self.buffer_size] = msg
        
        
        
    
        self.update_map(msg)
        
        current_pos = self.pos_msgs[self.pos_msgs_idx % self.buffer_size]
        if current_pos is None:
            current_pos = self.default_position
            
        self.map.save_plot(current_pos.x_position, current_pos.y_position)


    def position_listener_callback(self, msg):
            self.get_logger().info("Position Received")
            self.pos_msgs_idx += 1
            msg.facing_direction = -msg.facing_direction % 360
            self.pos_msgs[self.pos_msgs_idx % self.buffer_size] = msg
    
    
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
    
    
    def update_map(self, yolo_msg = None):
        if yolo_msg is None:
            yolo_msg = self.yolo_msgs[self.yolo_msgs_idx]
        
        
        # find the cluster message and position messages from the buffer that fit the yolo message best
        cluster_msg = self.match_message(yolo_msg, CLUSTER)
        position_msg = self.match_message(yolo_msg, POSITION)
        
        # when no navigation node is running, the position is not published. therefore we assume the turtlebot is at position (0,0)
        if position_msg is None:
            position_msg = self.default_position
        
        if cluster_msg is None or position_msg is None:
            self.get_logger().warning("Found no message to match to yolo message timestamp")
            return
        
        labeled_clusters = self.fuse_data(yolo_msg, cluster_msg)
        
        for cluster, label in labeled_clusters:
            # compute x and y position of cluster
            cone_x_pos, cone_y_pos = estimate_cone_position(cluster)
            
            
            self.map.set(position_msg.x_position, position_msg.y_position, position_msg.facing_direction, 
                         cone_x_pos, cone_y_pos, label)
            
    def fuse_data(self, yolo_msg, cluster_msg):
        """This function fuses the information of the clusters and the output of the yolo model. It tries to match the clusters found by the lidar
        to the bounding boxes generated by the yolo model.

        Args:
            yolo_msg (_type_): yolo message object received by Subscriber
            cluster_msg (_type_): cluster message object received by Subsriber

        Returns:
            list: returns a list with all found matches. One entry of the list is a tupel of a Cluster object and the label of the matched bounding box (0, 1 or 2)
        """
        
        # rule out clusters which are not in fov
        clusters_in_fov = []
        for cluster in cluster_msg.clusters:
             if (FOV[0] <= cluster.angles[0] and cluster.angles[0] <= FOV[1]) or (FOV[0] <= cluster.angles[-1] and cluster.angles[-1] <= FOV[1]):
                  clusters_in_fov.append(cluster)
        
        labeled_clusters = []
        for box in yolo_msg.bounding_boxes:
            box_left = (box.min_x - 320) / 320
            box_right = (box.max_x - 320) / 320
            range_box = (box_left, box_right)
            
            best_fitting_cluster = None
            range_best_fitting_cluster = None
            
            possible_clusters = []
            
            for cluster in clusters_in_fov:
                cluster_left = (-(cluster.angles[-1] - 180) / (0.5 * (FOV[1] - FOV[0])))
                cluster_right = (-(cluster.angles[0] - 180) / (0.5 * (FOV[1] - FOV[0])))
                range_cluster = (max(cluster_left, -1), min(1, cluster_right))
                
                # check if cluster is in bounding box
                if is_range_in_range(range_cluster, range_box):
                    possible_clusters.append(f"cluster:{range_cluster}, angles: {cluster.angles}, box:{range_box}, label: {box.cone}")
                    if best_fitting_cluster is None:
                        best_fitting_cluster = cluster
                        range_best_fitting_cluster = range_cluster
                    else:
                        # check if the center of the cluster is closer to the center of the box than the current best cluster
                        if np.abs(center_of_range(range_cluster) - center_of_range(range_box)) < np.abs(center_of_range(range_best_fitting_cluster) - center_of_range(range_box)):
                            best_fitting_cluster = cluster
                            range_best_fitting_cluster = range_cluster

                        # delta = np.abs(range_cluster[1] - range_cluster[0])
                        
                        # if delta > np.abs(range_best_fitting_cluster[0] - range_best_fitting_cluster[1]):
                        #     best_fitting_cluster = cluster
                        #     range_best_fitting_cluster = range_cluster
            
            if best_fitting_cluster:
                if len(possible_clusters) > 1:
                    print(possible_clusters)
                labeled_clusters.append((best_fitting_cluster, box.cone))
            else:
                self.get_logger().warning("Found no cluster to match to bounding box")
        return labeled_clusters
                       
        


def main(args=None):
    rclpy.init(args=args)
    data_fusion_node = DataFusionNode()
    rclpy.spin(data_fusion_node)

    data_fusion_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()