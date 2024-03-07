import numpy as np
import matplotlib.pyplot as plt
import os

IMSAVE_PATH = os.path.dirname(os.path.realpath(__file__)) + "/../../visualisations/global_map"


def get_timestamp_as_float(msg):
    return msg.header.stamp.sec + msg.header.stamp.nanosec / 1e9

def is_range_in_range(inner_range, outer_range):    
    # check if at left border
    if inner_range[0] < -1:
        # check only right border
        return inner_range[1] <= outer_range[1]
    #check if at right border
    elif inner_range[1] > 1:
        # check only left border
        return outer_range[0] <= inner_range[0]
    else:
        # check both borders
        return outer_range[0] <= inner_range[0] and inner_range[1] <= outer_range[1]
    
def rotate_point_around_origin(x, y, angle):
    angle = np.deg2rad(angle)
    return x * np.cos(angle) - y * np.sin(angle), y * np.cos(angle) + x * np.sin(angle)

def estimate_cone_position(cluster_msg):
        cone_x_pos = np.mean(cluster_msg.x_positions)
        cone_y_pos = np.mean(cluster_msg.y_positions)
        
        return cone_x_pos, cone_y_pos



class Map:
    def __init__(self, size=10000) -> None:
        # all distances are in mm
        self.size = size
        self.discretization_steps = 10 # = 1cm
        self.dim = (int(size / self.discretization_steps), int(size / self.discretization_steps))
        self.data = np.zeros(self.dim) - 1
        
        # plot
        self.fig, self.ax = plt.subplots()

    def set(self, x_position_t, y_position_t, facing_direction_t, x_position_cone, y_position_cone, cone):
        # the cone position is given in the local coordinate system of the turtlebot
        
        # position (0,0) is in the middle of the map
        glob_x_t = self.size / 2 + x_position_t
        glob_y_t = self.size / 2 + y_position_t
        
        # assuming that a facing direction of 180 is the front
        x_delta, y_delta = rotate_point_around_origin(x_position_cone, y_position_cone, facing_direction_t)
        
        glob_x_cone = glob_x_t + x_delta
        glob_y_cone = glob_y_t + y_delta
        
        # find array entry to set
        x = glob_x_cone / self.discretization_steps
        y = glob_y_cone / self.discretization_steps
        
        
        
        x = round(x)
        y = round(y)
        self.data[x, y] = cone
    
    
    def get_cones(self):
        cone_positions = []
        for i in [0, 1, 2]:
            cone_positions.append(np.argwhere(self.data == i) * self.discretization_steps) 
        return cone_positions
            
        
    def save_plot(self, x_pos_t = 0, y_pos_t = 0):
        
        x_pos_t += self.size / 2
        y_pos_t += self.size / 2
        
        # prepare plot 
        self.ax.clear()
        turtlebot = plt.Circle((x_pos_t, y_pos_t), 100, color="red", fill=True)
        self.ax.add_patch(turtlebot)
        cone_positions = self.get_cones()
        
        
        cone_size = 100
        fill_cones = True
        colors = ["blue", "orange", "yellow"]
        
        # blue
        for i, cones in enumerate(cone_positions):
            for cone in cones:
                cone = plt.Circle((cone[0], cone[1]), cone_size, color=colors[i], fill=fill_cones)
                self.ax.add_patch(cone)
        
        self.ax.set_xlim([0, self.size])
        self.ax.set_ylim([0, self.size])
        self.ax.set_box_aspect(1)
        self.fig.savefig(IMSAVE_PATH)


# map = Map()

# map.set(0, 0, 90, 1500, -500, 1)
# map.save_plot()
