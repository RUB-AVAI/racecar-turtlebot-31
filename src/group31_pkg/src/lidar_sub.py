import rclpy
import numpy as np
import matplotlib.pyplot as plt
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import os


#global variables
IMSAVE_PATH = os.path.dirname(os.path.realpath(__file__)) + "/../../visualisations/lidar_map"

class LidarSubscriber(Node):

    def __init__(self):
        super().__init__('lidar_subscriber')

        self.lidar_subscription = self.create_subscription(LaserScan, "/scan", self.lidar_listener_callback, rclpy.qos.qos_profile_sensor_data)
        self.lidar_subscription  # prevent unused variable warning

        # self.bounding_boxes_subscribtion = self.create_subscription()

        # figure 
        self.fig, self.ax = plt.subplots()
        plt.axis("equal")
        self.ranges = np.zeros(360)
        


    def update_map(self):
        X = []
        Y = []
        
        for angle, range in enumerate(self.ranges):
            # change the angles, so the y axis aligns with the camera
            angle = (angle + 180) % 360
            angle = 360 - angle
            if range != 0:
                radiant = angle / 360 * 2 * np.pi
                x = np.sin(radiant) * range
                y = np.cos(radiant) * range
                X.append(x)
                Y.append(y)
            
        self.ax.clear()

        blindspot = plt.Circle((0, 0), 0.09, color="red", fill=False)
        self.ax.add_patch(blindspot)
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