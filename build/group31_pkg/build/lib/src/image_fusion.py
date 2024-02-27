import os
import rclpy
import numpy as np
import matplotlib.pyplot as plt
from rclpy.node import Node
from message_filters import ApproximateTimeSynchronizer, Subscriber
from avai_messages.msg import YoloOutput, BoundingBox
from sensor_msgs.msg import LaserScan
from sklearn.cluster import DBSCAN



#global variables
QUEUE_SIZE = 1
SHOW_IMAGE = False
IMSAVE_PATH = os.path.dirname(os.path.realpath(__file__)) + "/../../visualisations/lidar_map"

class imageFusion(Node):
    def __init__(self):
        super().__init__('lidar_subscriber')
        self.cone_subscription = Subscriber(self, YoloOutput, "/cone_classification")

        self.lidar_subscription = Subscriber(self, LaserScan, "/scan", qos_profile=rclpy.qos.qos_profile_sensor_data)

        ts = ApproximateTimeSynchronizer([self.cone_subscription, self.lidar_subscription], queue_size=10, slop=0.1)
        ts.registerCallback(self.callback)

        self.bounding_box_confidence_threshold = 0.85


        self.camera_range = 62 # range of camera in degree (see slides in moodle: 03-Perception Arcitecture): 62.2
        self.lidar_front = 270 # front entry of the lidar sensor (from 0 to 360)
        self.covering = [int(self.lidar_front-(self.camera_range/2)), int(self.lidar_front+(self.camera_range/2))] # array containing the min and max positions in the lidar map that the camera perceives
        self.buffer = [-0, 0]
        self.camera_fov = [self.covering[0]+self.buffer[0], self.covering[1]+self.buffer[1]]
        self.img_size_x = 640
        self.bin_size = self.img_size_x / self.camera_range
        self.bin_borders = [self.bin_size*i for i in range(self.camera_range)]
        
        self.bins = [[] for _ in range(self.camera_range)]
        self.coordinates = []

        # figure 
        self.fig, self.ax = plt.subplots()
        plt.axis("equal")
        self.ranges = np.zeros(360)

        # cluster parameters
        self.eps = 0.1
        self.min_samples = 2 # try 4 or 8

    def update_bins(self): #TODO: add missing bin an end
        """
        updates the attribute bins, so for each angle there is an array containing the labels 0, 1 and 2 if a 
        cone is detected at this angle
        """
        bins = [[] for _ in range(self.camera_range)]
        
        for box in self.bounding_boxes:
            if box.confidence >= self.bounding_box_confidence_threshold:
                bin_idx_left = int(np.floor(box.min_x / self.bin_size))
                bin_idx_right = int(np.floor(box.max_x / self.bin_size))
                
                for bin_idx in range(bin_idx_left, min(bin_idx_right + 1, self.camera_range)):
                    bins[bin_idx].append(box.cone)

        self.bins = bins

    
    def update_coordinates(self):
        pass


    def cluster(self, X, Y):
        """
        Perform DBSCAN clustering on LIDAR data.

        Parameters:
        - lidar_data: numpy array of shape (N, 2) containing Cartesian coordinates (x, y) of LIDAR points.
        - eps: Epsilon neighborhood radius for DBSCAN.
        - min_samples: Minimum number of points required to form a cluster.

        Returns:
        - clustered_points: List of lists, where each inner list contains points belonging to a cluster.
        """
        lidar_data = list(zip(X, Y))

        # Create DBSCAN instance and fit to data
        dbscan = DBSCAN(eps=self.eps, min_samples=self.min_samples)
        clusters = dbscan.fit_predict(lidar_data)

        # Extract the cluster labels
        unique_labels = np.unique(clusters)

        # Convert clusters to a list (if it's a numpy array) to ensure integer values
        clusters = clusters.tolist()

        # Create a list to store the clustered points
        clustered_points = []

        # Iterate through clusters and filter out noise points (label -1)
        for label in unique_labels:
            if label != -1:  # Skip noise points
                points_in_cluster = []
                for i, cluster_label in enumerate(clusters):
                    if cluster_label == label:
                        points_in_cluster.append(lidar_data[i])
                clustered_points.append(points_in_cluster)

        return clustered_points        

    def update_map(self):
        self.ax.clear()

        blindspot = plt.Circle((0, 0), 0.09, color="red", fill=False)
        self.ax.add_patch(blindspot)
        self.ax.scatter(self.X, self.Y, marker=".", color="black")

        limit = 4
        self.ax.set_xlim([-limit, limit])
        self.ax.set_ylim([-limit, limit])
        self.get_logger().info("Updated Lidar Map")

    def save_map(self):
        self.fig.savefig(IMSAVE_PATH)
        self.get_logger().info("Saved Lidar Map")

    
    def callback(self, msg_cones, msg_lidar):
        """
        is called when a message is received
        """
        # range min: 0.12 m
        # range max: 3.5 m
        # the ranges start on the right side of the turtlebot and continue clockwise (entry 270 is the front)

        self.get_logger().info(f'Received synchronized messages')

        self.bounding_boxes = msg_cones.bounding_boxes
        self.ranges = msg_lidar.ranges[self.camera_fov[0]:self.camera_fov[1]+1] # takes only the ranges in the fov of the camera
        print(self.camera_fov)
        exit()
        self.update_bins()
        # self.update_coordinates()
        print(msg_lidar.ranges)
        exit()
        for (b, r) in zip(self.bins, self.ranges):
            print(b, r)
        exit()
        for i in self.coordinates:
            print(i)
        exit()

        self.get_coordinates()

        cluster = self.cluster(self.X, self.Y)
        ranges, identifier = self.convert_to_polar_with_identifiers(cluster)
        self.cut_lidar_data(ranges, identifier)
        #for r, i in zip(ranges, identifier):
        #    print(r, i)

        self.update_map()
        self.save_map()




def main(args=None):
    rclpy.init(args=args)
    lidar_subscriber = imageFusion()
    rclpy.spin(lidar_subscriber)

    lidar_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
