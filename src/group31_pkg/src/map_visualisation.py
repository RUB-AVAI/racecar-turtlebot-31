import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from avai_messages.msg import Cone, Cones, Position, Target
import cv2
import os
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import DBSCAN, MeanShift
from copy import copy

IMSAVE_PATH = os.path.dirname(os.path.realpath(__file__)) + "/../../visualisations/map.png"



class MapVisualisation_Node(Node):
    def __init__(self):
        super().__init__("map_visualisation_node")
        self.cone_subsciber = self.create_subscription(Cones, "/cone_visualisation", self.cone_callback, qos_profile=rclpy.qos.qos_profile_services_default)
        self.position_subsciber = self.create_subscription(Position, "/position", self.position_callback, qos_profile=rclpy.qos.qos_profile_sensor_data)
        self.target_subscriber = self.create_subscription(Target, "/target_position", self.target_callback, qos_profile=rclpy.qos.qos_profile_services_default)
        
        # self.create_timer(0.5, self.update_plot)
        
        self.all_cones = [[], [], []]
        self.colors = ["blue", "orange", "yellow"]
        self.target = None
        
        default_position = Position()
        default_position.x_position=0.0 # in mm
        default_position.y_position=0.0 # in mm
        default_position.facing_direction=0.0 # in degrees
        
        self.position = default_position
        
        self.fig, self.ax = plt.subplots()
        
        self.eps = 300 # in millimeters
        self.min_samples = 3 # try 4 or 8

        self.dbscan = DBSCAN(eps=self.eps, min_samples=self.min_samples)
    
    
    def cone_callback(self, msg):
        self.get_logger().info("Received Cones message")
        
        
        for cone in msg.cones:
            self.all_cones[cone.color].append([cone.x_position, cone.y_position])
        
        
            
    def position_callback(self, msg):
        self.get_logger().info("Received Position message")
        
        self.position = msg
        
        self.update_plot()
        
    
    def target_callback(self, msg):
        self.get_logger().info("Received Target message")
        
        self.target = msg
        
        
    
    def update_plot(self):
        self.ax.clear()
        map_size = 40000
        limit = map_size / 2
        self.ax.set_xlim([-limit, limit])
        self.ax.set_ylim([-limit, limit])
        
        # turtlebot
        turtlebot = plt.Circle((self.position.x_position, self.position.y_position), 100, color="red", fill=True)
        self.ax.add_patch(turtlebot)
        
        # target
        if self.target:
            target = plt.Circle((self.target.x_position[0], self.target.y_position[0]), 50, color="green", fill=True)
            self.ax.add_patch(target)
        
        all_cones = copy(self.all_cones)
        
        
        
        
        for color, cones_one_color in enumerate(all_cones):
            
            if len(cones_one_color) == 0:
                continue
            cones_one_color = np.array(cones_one_color)
            
            # self.ax.scatter(cones_one_color[:, 0], cones_one_color[:, 1], color = self.colors[color], marker=".")
            # continue
            
            labels = self.dbscan.fit_predict(cones_one_color)
            unique_labels = np.unique(labels)
            
            clusters_x_positions = [[] for _ in range(len(unique_labels))]
            clusters_y_positions = [[] for _ in range(len(unique_labels))]
            
            
            for i, cone in enumerate(cones_one_color):
                clusters_x_positions[labels[i]].append(cone[0])
                clusters_y_positions[labels[i]].append(cone[1])
            
            
            for label in unique_labels:
                if label == -1:
                    continue
                average_x = np.mean(clusters_x_positions[label])
                average_y = np.mean(clusters_y_positions[label])
                

                
                patch = plt.Circle((average_x, average_y), 100, color = self.colors[color], fill=True)
                self.ax.add_patch(patch)
            
            
        self.fig.savefig(IMSAVE_PATH)
            
                
        
        
        
            
        

def main(args=None):
    rclpy.init(args=args)
    node = MapVisualisation_Node()
    rclpy.spin(node)


    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()