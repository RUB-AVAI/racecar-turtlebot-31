import rclpy
import numpy as np
import matplotlib.pyplot as plt
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import os
from sklearn.cluster import DBSCAN



#global variables
IMSAVE_PATH = os.path.dirname(os.path.realpath(__file__)) + "/../../visualisations/lidar_map"
CLUSTER = False

class LidarSubscriber(Node):

    def __init__(self):
        super().__init__('lidar_subscriber')

        self.lidar_subscription = self.create_subscription(LaserScan, "/scan", self.lidar_listener_callback, rclpy.qos.qos_profile_sensor_data)
        self.lidar_subscription  # prevent unused variable warning

        # cluster parameters
        self.eps = 0.1
        self.min_samples = 2 # try 4 or 8
        if CLUSTER:
            self.dbscan = DBSCAN(eps=self.eps, min_samples=self.min_samples)


        # figure 
        self.fig, self.ax = plt.subplots()
        plt.axis("equal")
        self.ranges = np.zeros(360)
        
        # lidar data: starts at the back and then rotates counter clockwise
        # front: 180
        # back: 0
        # right: 90
        # left: 270



    def update_map(self):
        X = []
        Y = []
        
        for angle, range in enumerate(self.ranges):
            if range != 0:
                radiant = angle / 360 * 2 * np.pi
                x = np.cos(radiant) * range
                y = np.sin(radiant) * range
                X.append(x)
                Y.append(y)
        
        # prepare plot 
        self.ax.clear()

        blindspot = plt.Circle((0, 0), 0.09, color="red", fill=False)
        self.ax.add_patch(blindspot)
            
        if CLUSTER:
            lidar_points = np.asarray([X, Y]).transpose()
            clusters = self.dbscan.fit_predict(lidar_points)
             # Extract the cluster labels
            unique_labels = np.unique(clusters)

            # Create a list to store the clustered points
            clustered_points = []

            # Iterate through clusters and filter out noise points (label -1)
            for label in unique_labels:
                if label != -1:  # Skip noise points
                    X = []
                    Y = []
                    for i, cluster_label in enumerate(clusters):
                        if cluster_label == label:
                            X.append(lidar_points[i, 0])
                            Y.append(lidar_points[i, 1])
                    clustered_points.append((X, Y))
            
            for cluster in clustered_points:
                X, Y = cluster
                self.ax.scatter(X, Y, marker=".")
                
        else:
            self.ax.scatter(X, Y, marker=".")
            
        
        

        limit = 4
        self.ax.set_xlim([-limit, limit])
        self.ax.set_ylim([-limit, limit])
        self.get_logger().info("Updated Lidar Map")


    def save_map(self):
        self.fig.savefig(IMSAVE_PATH)
        self.get_logger().info("Saved Lidar Map")


    def lidar_listener_callback(self, msg):
        # range min: 0.12 m
        # range max: 3.5 m
        # the ranges start on the right side of the turtlebot and continue clockwise (entry 270 is the front)
    
        self.get_logger().info("Lidar Data Received")
        self.ranges = msg.ranges
        self.update_map()
        self.save_map()


def main(args=None):
    rclpy.init(args=args)
    lidar_subscriber = LidarSubscriber()
    rclpy.spin(lidar_subscriber)


    lidar_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()