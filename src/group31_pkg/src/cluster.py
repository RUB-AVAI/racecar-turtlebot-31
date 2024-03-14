import rclpy
import numpy as np
import matplotlib.pyplot as plt
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from avai_messages.msg import ClusteredLidarData, Cluster
import os
from sklearn.cluster import DBSCAN
from copy import copy



#global variables
IMSAVE_PATH = os.path.dirname(os.path.realpath(__file__)) + "/../../visualisations/lidar_map"
CLUSTER = True
SAVE_VISUALISATION = False

TOPIC = "/clusterered_lidar_data"
QUEUE_SIZE = 1

class LidarProcessingNode(Node):

    def __init__(self):
        super().__init__('lidar_processing_node')

        self.lidar_subscription = self.create_subscription(LaserScan, "/scan", self.lidar_listener_callback, rclpy.qos.qos_profile_sensor_data)
        self.lidar_subscription  # prevent unused variable warning

        self.publisher_ = self.create_publisher(ClusteredLidarData, TOPIC, rclpy.qos.qos_profile_sensor_data)
        self.i = 0

        # cluster parameters
        self.eps = 0.15 * 1000 # in millimeters
        self.min_samples = 1 # try 4 or 8
        if CLUSTER:
            self.dbscan = DBSCAN(eps=self.eps, min_samples=self.min_samples)

        if SAVE_VISUALISATION:
            # figure 
            self.fig, self.ax = plt.subplots()
            plt.axis("equal")

        self.ranges = np.zeros(360)
        self.timestamp = None
        
        # lidar data: starts at the back and then rotates counter clockwise
        # front: 180
        # back: 0
        # right: 90
        # left: 270
        # range min: 0.12 m
        # range max: 3.5 m



    def process_data(self):
        # updates the scatter plot and saves it at the specified location
        X = []
        Y = []
        A_unclustered = []
        R_unclustered = []
        
        ranges = copy(self.ranges)
        timestamp = copy(self.timestamp)

        # convert ranges into cartesian coordinates
        for angle, range in enumerate(ranges):
            if range != 0:
                radiant = angle / 360 * 2 * np.pi
                x = np.cos(radiant) * range
                y = np.sin(radiant) * range
                X.append(x)
                Y.append(y)
                A_unclustered.append(angle)
                R_unclustered.append(range)
        
        if SAVE_VISUALISATION:
            # prepare plot 
            self.ax.clear()

            blindspot = plt.Circle((0, 0), 90, color="red", fill=False)
            self.ax.add_patch(blindspot)
            
        if CLUSTER:
            # convert the points into np array of shape (N, 2)
            lidar_points = np.asarray([X, Y]).transpose()

            # cluster
            if len(lidar_points) > 0:
                clusters = self.dbscan.fit_predict(lidar_points)
            else:
                clusters = []
             # Extract the cluster labels
            unique_labels = np.unique(clusters)

            # Create a list to store the clustered points
            clustered_points = []

            # Iterate through clusters and filter out noise points (label -1)
            for label in unique_labels:
                if label != -1:  # Skip noise points
                    X = []
                    Y = []
                    A = []
                    R = []
                    for i, cluster_label in enumerate(clusters):
                        if cluster_label == label:
                            X.append(lidar_points[i, 0])
                            Y.append(lidar_points[i, 1])
                            A.append(A_unclustered[i])
                            R.append(R_unclustered[i])
                    clustered_points.append((X, Y, A, R))
            

            clusters = []
            for cluster in clustered_points:
                X, Y, A, R = cluster
                if SAVE_VISUALISATION:
                    # scatter each cluster individually so they get different colors
                    self.ax.scatter(X, Y, marker=".")

                # create a Cluster object for the publisher
                clusters.append(Cluster(x_positions=X, y_positions=Y, angles=A, ranges=R))
            
            # create and publish message
            msg = ClusteredLidarData()
            msg.clusters = clusters
            msg.header.stamp = timestamp
            msg.header.frame_id = f"{self.i}"
            self.i += 1
            self.publisher_.publish(msg)
            self.get_logger().info('%d Clusterered Lidar Data Published' % self.i)         
        elif SAVE_VISUALISATION:
            self.ax.scatter(X, Y, marker=".")

        if SAVE_VISUALISATION:    
            limit = 5000 # mm
            self.ax.set_xlim([-limit, limit])
            self.ax.set_ylim([-limit, limit])
            self.ax.set_box_aspect(1)


    def save_map(self):
        self.fig.tight_layout()
        self.fig.savefig(IMSAVE_PATH)


    def lidar_listener_callback(self, msg):
        self.get_logger().info("Lidar Data Received")
        self.ranges = np.array(msg.ranges) * 1000 #convert ranges from meters to millimeters
        self.timestamp = msg.header.stamp
        self.process_data()
        if SAVE_VISUALISATION:
            self.save_map()


def main(args=None):
    rclpy.init(args=args)
    lidar_processing_node = LidarProcessingNode()
    rclpy.spin(lidar_processing_node)


    lidar_processing_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()