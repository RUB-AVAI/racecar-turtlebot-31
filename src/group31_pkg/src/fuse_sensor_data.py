import os
from utils import *
import rclpy
import numpy as np
import matplotlib.pyplot as plt
from rclpy.node import Node
from avai_messages.msg import YoloOutput, BoundingBox, ClusteredLidarData, Position, Target
import argparse

#camera fov:
FOV = (145, 215)
assert (180 - FOV[0] == FOV[1] - 180)

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--offset", help="allowed offset between fused messages", default=0.1, type=float)
args = parser.parse_args()


MIN_HISTORY = 2
CLUSTER = 0
POSITION = 1
LOG_INFO = False
TARGET_UPDATES_PER_SECOND = 0.5
VISUALISATION = False

class DataFusionNode(Node):
    def __init__(self):
        super().__init__('data_fusion_node')

        self.clustered_lidar_subscription = self.create_subscription(ClusteredLidarData, "/clusterered_lidar_data", self.clustered_lidar_listener_callback, rclpy.qos.qos_profile_sensor_data)
        self.yolo_output_subscription = self.create_subscription(YoloOutput, "/cone_classification", self.yolo_output_listener_callback, rclpy.qos.qos_profile_sensor_data)
        self.pos_subscription = self.create_subscription(Position, "/position", self.position_listener_callback, rclpy.qos.qos_profile_sensor_data)
        self.target_publisher = self.create_publisher(Target, "/target_position", qos_profile=rclpy.qos.qos_profile_services_default)
        self.target_updater = self.create_timer(1 / TARGET_UPDATES_PER_SECOND, self.update_target)
        
        self.map = Map(size=25000, min_hist=MIN_HISTORY)
        
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
        if LOG_INFO:
            self.get_logger().info("Clustered Lidar Data Received")
        self.cluster_msgs_idx += 1
        self.cluster_msgs[self.cluster_msgs_idx % self.buffer_size] = msg
        

    def yolo_output_listener_callback(self, msg):
        if LOG_INFO:
            self.get_logger().info("Yolo Output Received")
        # for box in msg.bounding_boxes:
        #     delta_x = np.abs(box.min_x - box.max_x)
        #     delta_y = np.abs(box.min_y - box.max_y)
        #     print(f"ratio for {box.cone}: {delta_y / delta_x}")
            
        # msg = preprocess_bounding_boxes(msg, log_to_console=True)
        self.yolo_msgs_idx += 1
        self.yolo_msgs[self.yolo_msgs_idx % self.buffer_size] = msg
        
        
    
        self.update_map(msg)
        
        current_pos = self.pos_msgs[self.pos_msgs_idx % self.buffer_size]
        if current_pos is None:
            current_pos = self.default_position
        
        if VISUALISATION:    
            self.map.save_plot(current_pos.x_position, current_pos.y_position)


    def position_listener_callback(self, msg):
            if LOG_INFO:
                self.get_logger().info("Position Received")
            self.pos_msgs_idx += 1
            msg.facing_direction = -msg.facing_direction % 360
            self.pos_msgs[self.pos_msgs_idx % self.buffer_size] = msg
    
    
    def update_target(self):
        pos = self.pos_msgs[self.pos_msgs_idx % self.buffer_size]
        if pos is None:
            pos = self.default_position
        x,y,angle = self.map.estimate_new_target(pos.x_position, pos.y_position)
        print(f"angle: {angle}, x: {x}, y: {y}")
        if x is None and y is None and angle is None:
            return
        target = Target()
        target.header.stamp = self.get_clock().now().to_msg()
        target.round = 0
        
        if angle:
            target.turn_angle = float(angle)
            target.x_position = 0.0
            target.y_position = 0.0
        else:
            target.turn_angle = 0.0
            target.x_position = float(x)
            target.y_position = float(y)
        
        
        self.target_publisher.publish(target)
    
    
    def match_message(self, yolo_msg, type, max_offset=args.offset):
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
        print(f"yolo_timestamp: {yolo_timestamp}")

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
             print(f"cluster_timestamp: {timestamp}")
             
             
             distance = np.abs(timestamp - yolo_timestamp)
             if distance < max_offset:
                 return msg
             if(i>0):
                 if distance > prev_distance:
                     return None
                 else:
                     prev_distance = distance
    
    
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
        
        labeled_clusters = self.fuse_data3(yolo_msg, cluster_msg)
        
        if(len(labeled_clusters)) == 0:
            return
        
        # order the clusters from close to far
        # labeled_clusters = np.array(labeled_clusters)
        # calc_distance = lambda x1, y1, x2, y2: np.linalg.norm((x1-x2, y1-y2))
        
        
        
        # distances = [calc_distance(position_msg.x_position, position_msg.y_position, average_cluster_position(cluster)[0], average_cluster_position(cluster)[1]) for cluster in labeled_clusters[:, 0]]
        # labeled_clusters = labeled_clusters[np.argsort(distances)]
        
        for cluster, label in labeled_clusters:
            # compute x and y position of cluster
            cone_x_pos, cone_y_pos = average_cluster_position(cluster)
            
            
            self.map.set(position_msg.x_position, position_msg.y_position, position_msg.facing_direction, 
                         cone_x_pos, cone_y_pos, label)
    
    
    def fuse_data3(self, yolo_msg, cluster_msg):
        # rule out clusters which are not in fov
        clusters_in_fov = []
        for cluster in cluster_msg.clusters:
            if (FOV[0] <= cluster.angles[0] and cluster.angles[0] <= FOV[1]) or (FOV[0] <= cluster.angles[-1] and cluster.angles[-1] <= FOV[1]):
                clusters_in_fov.append(cluster)
        
        # rule out clusters that are definitly not cones
        filtered_clusters = []
        for cluster in clusters_in_fov:
            if could_be_cone(cluster):
                filtered_clusters.append(cluster)
        
        
        estimated_cone_positions = []
        labels = []
        
        for box in yolo_msg.bounding_boxes:
            if box.confidence < 0.7:
                continue
            estimated_position = estimate_cone_position(box)
            if estimated_position is not None:
                estimated_cone_positions.append(estimated_position)
                labels.append(box.cone)
        
        if VISUALISATION:
            plot_clusters_and_cones(filtered_clusters, estimated_cone_positions, labels)
        
        # fuse
        epsilon = 150#mm
        labeled_clusters = []
        for cluster in filtered_clusters:
            cluster_position = average_cluster_position(cluster)
            # look for closest cone estimation
            min_distance = np.inf
            closest_cone_idx = None
            for i, cone_position in enumerate(estimated_cone_positions):
                distance = np.linalg.norm((cluster_position[0] - cone_position[0], cluster_position[1] - cone_position[1]))
                if distance < min_distance:
                    closest_cone_idx = i
                    min_distance = distance
            
            # print(f"distance: {min_distance}, cluster position: {average_cluster_position(cluster)}, cone position: {estimated_cone_positions[closest_cone_idx]}")
            if min_distance < epsilon:
                labeled_clusters.append((cluster, labels[closest_cone_idx]))
        
        return labeled_clusters
    
    # def fuse_data2(self, yolo_msg, cluster_msg):
        
    #     labeled_clusters = []
        
        
        
    #     if cluster_msg:
    #         # rule out clusters which are not in fov
    #         clusters_in_fov = []
    #         for cluster in cluster_msg.clusters:
    #             if (FOV[0] <= cluster.angles[0] and cluster.angles[0] <= FOV[1]) or (FOV[0] <= cluster.angles[-1] and cluster.angles[-1] <= FOV[1]):
    #                 clusters_in_fov.append(cluster)
            
    #         # rule out clusters that are definitly not cones
    #         filtered_clusters = []
    #         for cluster in clusters_in_fov:
    #             if could_be_cone(cluster):
    #                 filtered_clusters.append(cluster)
            
    #         plot_clusters(filtered_clusters)
        
                
    #     # check the boundaries:
    #     # even if the boxes are at the boundaries, they might not have the coordinates set to 0 / 640
    #     if yolo_msg:
    #         buffer = 10 #px
    #         bounding_boxes = yolo_msg.bounding_boxes
    #         box_left_edge = []
    #         box_right_edge = []
    #         box_ = []
    #         for i, box in enumerate(bounding_boxes):
    #             if box.min_x < buffer:
    #                 box_left_edge.append(box)
    #                 bounding_boxes.remove(i)
                
    #             elif box.max_x > 640 - buffer:
    #                 box_right_edge.append(box)
    #                 bounding_boxes.remove(i)
    #         if box_left_edge:
    #             print(f"left: label: {box_left_edge.cone}, coordinates: {box_left_edge.min_x}, {box_left_edge.max_x}, ratio: {bb_ratio(box_left_edge)}")
    #         if box_right_edge:
    #             print(f"right: label: {box_right_edge.cone}, coordinates: {box_right_edge.min_x}, {box_right_edge.max_x}, ratio: {bb_ratio(box_right_edge)}")
        
    #     if len(box_left_edge) == 1:
    #         # check if there is a cluster that matches
    #         possible_cluster = filtered_clusters[-1]
            
    #     elif len(box_left_edge) > 1:
    #         print("found two boxes at left boundary")
            
    # def fuse_data(self, yolo_msg, cluster_msg):
    #     """This function fuses the information of the clusters and the output of the yolo model. It tries to match the clusters found by the lidar
    #     to the bounding boxes generated by the yolo model.

    #     Args:
    #         yolo_msg (_type_): yolo message object received by Subscriber
    #         cluster_msg (_type_): cluster message object received by Subsriber

    #     Returns:
    #         list: returns a list with all found matches. One entry of the list is a tupel of a Cluster object and the label of the matched bounding box (0, 1 or 2)
    #     """
        
    #     # rule out clusters which are not in fov
    #     clusters_in_fov = []
    #     for cluster in cluster_msg.clusters:
    #          if (FOV[0] <= cluster.angles[0] and cluster.angles[0] <= FOV[1]) or (FOV[0] <= cluster.angles[-1] and cluster.angles[-1] <= FOV[1]):
    #               clusters_in_fov.append(cluster)
        
    #     # rule out clusters that are definitly not cones
    #     filtered_clusters = []
    #     for cluster in clusters_in_fov:
    #         if could_be_cone(cluster):
    #             filtered_clusters.append(cluster)
    #     plot_clusters(filtered_clusters)
    #     labeled_clusters = []
        
        
    #     d_first_iter = True
    #     d_ranges_box = []
    #     d_ranges_cluster = []
        
        
    #     for box in yolo_msg.bounding_boxes:
    #         box_left = (box.min_x - 320) / 320
    #         box_right = (box.max_x - 320) / 320
    #         range_box = [box_left, box_right]
    #         d_ranges_box.append(range_box)
            
    #         best_fitting_cluster = None
    #         range_best_fitting_cluster = None
            
            
    #         for cluster in filtered_clusters:
    #             cluster_left = (-(cluster.angles[-1] - 180) / (0.5 * (FOV[1] - FOV[0])))
    #             cluster_right = (-(cluster.angles[0] - 180) / (0.5 * (FOV[1] - FOV[0])))
    #             range_cluster = [max(cluster_left, -1), min(1, cluster_right)]
    #             if d_first_iter:
    #                 d_ranges_cluster.append(range_cluster)
                
    #             # check if cluster is in bounding box
    #             if is_range_in_range(range_cluster, range_box):
    #                 if best_fitting_cluster is None:
    #                     best_fitting_cluster = cluster
    #                     range_best_fitting_cluster = range_cluster
    #                 else:
    #                     # check if the center of the cluster is closer to the center of the box than the current best cluster
    #                     if np.abs(center_of_range(range_cluster) - center_of_range(range_box)) < np.abs(center_of_range(range_best_fitting_cluster) - center_of_range(range_box)):
    #                         best_fitting_cluster = cluster
    #                         range_best_fitting_cluster = range_cluster
    #         d_first_iter = False
            
    #         if best_fitting_cluster:
    #             labeled_clusters.append((best_fitting_cluster, box.cone))
    #         else:
    #             pass
    #             # self.get_logger().warning("Found no cluster to match to bounding box")
    #     # d_ranges_box = np.array(d_ranges_box)
    #     # d_ranges_box = d_ranges_box[np.argsort(d_ranges_box[:, 0])]
    #     # if len(d_ranges_cluster) != 0:
    #     #     d_ranges_cluster=np.array(d_ranges_cluster)
    #     #     d_ranges_cluster = d_ranges_cluster[np.argsort(d_ranges_cluster[:, 0])]
    
    #     # print(f"boxes: {d_ranges_box}")
    #     # print(f"cluster: {d_ranges_cluster}")
    #     return labeled_clusters
                       
        


def main(args=None):
    rclpy.init(args=args)
    data_fusion_node = DataFusionNode()
    rclpy.spin(data_fusion_node)

    data_fusion_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()