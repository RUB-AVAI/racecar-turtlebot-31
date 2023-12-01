import rclpy
import numpy as np
import matplotlib.pyplot as plt
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from rclpy.qos import ReliabilityPolicy, QoSProfile, DurabilityPolicy, HistoryPolicy
import os


#global variables
TOPIC = "/scan"
IMSAVE_PATH = os.path.dirname(os.path.realpath(__file__)) + "/../../visualisations/lidar_map"
QUEUE_SIZE = 10

class LidarSubscriber(Node):

    def __init__(self):
        super().__init__('lidar_subscriber')

        qos_profile = QoSProfile(reliability=ReliabilityPolicy.BEST_EFFORT, depth=QUEUE_SIZE)

        self.subscription = self.create_subscription(LaserScan, TOPIC, self.listener_callback, rclpy.qos.qos_profile_sensor_data)
        self.subscription  # prevent unused variable warning

        # figure 
        self.fig, self.ax = plt.subplots()
        plt.axis("equal")
        



    def listener_callback(self, msg):
        # range min: 0.12 m
        # range max: 3.5 m
    
        self.get_logger().info("Data Received")
        intensities = np.array(msg.intensities)
        ranges = np.array(msg.ranges)


        X = []
        Y = []
        
        for angle, range in enumerate(ranges):
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

        self.fig.savefig(IMSAVE_PATH)


        




        



def main(args=None):
    rclpy.init(args=args)
    lidar_subscriber = LidarSubscriber()
    rclpy.spin(lidar_subscriber)


    lidar_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()