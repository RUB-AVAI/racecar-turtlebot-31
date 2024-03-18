import os
from utils import *
import rclpy
import numpy as np
import matplotlib.pyplot as plt
from rclpy.node import Node
from avai_messages.msg import YoloOutput, BoundingBox, ClusteredLidarData, Position, Target
import argparse
from time import time

#camera fov:
FOV = (145, 215)
assert (180 - FOV[0] == FOV[1] - 180)

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--offset", help="allowed offset between fused messages", default=0.15, type=float)
args = parser.parse_args()


MIN_HISTORY = 2
CLUSTER = 0
POSITION = 1
YOLO = 2
LOG_INFO = False
TARGET_UPDATES_PER_SECOND = 10
VISUALISATION = True


class DataFusionNode(Node):
    def __init__(self):
        super().__init__('data_fusion_node')

        self.clustered_lidar_subscription = self.create_subscription(ClusteredLidarData, "/clusterered_lidar_data", self.clustered_lidar_listener_callback, rclpy.qos.qos_profile_sensor_data)
        self.yolo_output_subscription = self.create_subscription(YoloOutput, "/cone_classification", self.yolo_output_listener_callback, rclpy.qos.qos_profile_sensor_data)
        self.pos_subscription = self.create_subscription(Position, "/position", self.position_listener_callback, rclpy.qos.qos_profile_sensor_data)
        self.target_publisher = self.create_publisher(Target, "/target_position", qos_profile=rclpy.qos.qos_profile_services_default)
        # self.target_updater = self.create_timer(1 / TARGET_UPDATES_PER_SECOND, self.update_target)
        
        self.map = Map(size=25000, min_hist=MIN_HISTORY, epsilon=10)
        
        self.init_time = time()
        
        self.buffer_size = 20
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
        
        self.round = 0
        
        
    

    def clustered_lidar_listener_callback(self, msg):
        if self.round == 1:
            return
        if LOG_INFO:
            self.get_logger().info("Clustered Lidar Data Received")
        self.cluster_msgs_idx += 1
        self.cluster_msgs[self.cluster_msgs_idx % self.buffer_size] = msg
        

    def yolo_output_listener_callback(self, msg):
        if self.round == 1:
            return
        if LOG_INFO:
            self.get_logger().info("Yolo Output Received")
        # for box in msg.bounding_boxes:
        #     delta_x = np.abs(box.min_x - box.max_x)
        #     delta_y = np.abs(box.min_y - box.max_y)
        #     print(f"ratio for {box.cone}: {delta_y / delta_x}")
            
        # msg = preprocess_bounding_boxes(msg, log_to_console=True)
        self.yolo_msgs_idx += 1
        self.yolo_msgs[self.yolo_msgs_idx % self.buffer_size] = msg
        
        if self.round == 0:
        
            self.update_map(msg)
            
            current_pos = self.pos_msgs[self.pos_msgs_idx % self.buffer_size]
            if current_pos is None:
                current_pos = self.default_position
            
            if VISUALISATION:    
                self.map.save_plot(current_pos.x_position, current_pos.y_position, all_targets=(self.round == 1))
            


    def position_listener_callback(self, msg):
        if self.round == 1:
            self.map.save_plot(msg.x_position, msg.y_position, all_targets=True)
        if LOG_INFO:
            self.get_logger().info("Position Received")
        self.pos_msgs_idx += 1
        msg.facing_direction = -msg.facing_direction % 360
        self.pos_msgs[self.pos_msgs_idx % self.buffer_size] = msg
    
    
    def update_target(self):
        if self.round == 1:
            return
        pos = self.pos_msgs[self.pos_msgs_idx % self.buffer_size]
        if pos is None:
            pos = self.default_position
        x,y,angle = self.map.estimate_new_target(pos.x_position, pos.y_position)
        # print(f"angle: {angle}, x: {x}, y: {y}")
        if x is None and y is None and angle is None:
            return
        target = Target()
        target.header.stamp = self.get_clock().now().to_msg()
        target.round = 0
        
        if angle:
            target.turn_angle = float(angle)
            target.x_position = [0.0]
            target.y_position = [0.0]
        else:
            target.turn_angle = 0.0
            target.x_position = [float(x)]
            target.y_position = [float(y)]
        
        
        self.target_publisher.publish(target)
    
    
    def match_message(self, main_message, type, max_offset=args.offset):
        """Because of the inference of the yolo model, the yolo messages arrive later than the other messages. Therefore this function  
         searches the buffer for a message with the corresponding timestamp.
         The type argument specifies to look for cluster or position

        Returns:
            Cluster: Returns the matching Cluster message or None if no matching message was found
        """
        
        if type != CLUSTER and type != POSITION and type != YOLO:
            raise KeyError()
            
        # because of the inference of the yolo model, we search the other messages for the appropriate timestamp
        main_timestamp = get_timestamp_as_float(main_message)

        # find nearest message
        prev_distance = np.inf
        for i in range(self.buffer_size):
             if type==  CLUSTER:
                 msg = self.cluster_msgs[(self.cluster_msgs_idx - i) % self.buffer_size]
             elif type==POSITION:
                 msg = self.pos_msgs[(self.pos_msgs_idx - i) % self.buffer_size]
             elif type==YOLO:
                 msg = self.yolo_msgs[(self.yolo_msgs_idx - i) % self.buffer_size]
             if msg is None:
                 break
             timestamp = get_timestamp_as_float(msg)
             
             
             distance = np.abs(timestamp - main_timestamp)
             if distance < max_offset:
                 return msg
             if(i>0):
                 if distance > prev_distance:
                     return None
                 else:
                     prev_distance = distance
    
    
    def update_map(self, yolo_msg):
        
        # find the yolo message and position messages from the buffer that fit the yolo message best
        cluster_msg = self.match_message(yolo_msg, CLUSTER)
        position_msg = self.match_message(yolo_msg, POSITION)
        
        # when no navigation node is running, the position is not published. therefore we assume the turtlebot is at position (0,0)
        if position_msg is None:
            position_msg = self.default_position
        
        if cluster_msg is None or position_msg is None:
            self.get_logger().warning("Found no message to match to yolo message timestamp")
            return
        
        labeled_clusters = self.fuse_data(yolo_msg, cluster_msg)
        
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
        
        self.update_target()
        
        # check if in finish zone
        if time() - self.init_time > 20: # let some time pass before checking, because we also start in finish zone
            
            n_orange_cones = len(self.map.orange_cones)
            # print(f"number of orange cones seen: {n_orange_cones}")
        
            if n_orange_cones >= 4:
                self.target_zone()
                
            
        
    def target_zone(self):
        self.map.filter_orange_cones()
        
        if self.round == 2: return
            
        
        if len(self.map.orange_cones) >= 4:
            min_distance = np.inf
            pos = self.pos_msgs[self.pos_msgs_idx % self.buffer_size]
            if pos is None:
                pos = self.default_position
            
            for (x,y) in self.map.orange_cones:
                x *= self.map.discretization_steps
                y *= self.map.discretization_steps
                x -= self.map.size / 2
                y -= self.map.size / 2
                dist = distance(x, y, pos.x_position, pos.y_position)
                if dist < min_distance:
                    min_distance = dist
            
            if min_distance > 1500:
                return
            
            self.init_time = time()        
            print("round 1 started")
            # np.save(f"data/map{time()}", self.map)
        
            target = Target()
            target.header.stamp = self.get_clock().now().to_msg()
            target.round = 0
            
            self.map.last_target = (float(self.map.last_target[0] - 2000), float(self.map.last_target[1]))
            
            target.x_position = [float(self.map.last_target[0] - 2000)]
            target.y_position = [float(self.map.last_target[1])]
            target.turn_angle = 0.0
            
            
            self.target_publisher.publish(target)
        
    
    def fuse_data(self, yolo_msg, cluster_msg):
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
        epsilon = 200#mm
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
    

def main(args=None):
    rclpy.init(args=args)
    data_fusion_node = DataFusionNode()
    rclpy.spin(data_fusion_node)

    data_fusion_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()