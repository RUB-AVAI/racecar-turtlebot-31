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

def center_of_range(range):
    return np.mean(range)

def bb_ratio(box):
    delta_x = np.abs(box.min_x - box.max_x)
    delta_y = np.abs(box.min_y - box.max_y)
    return delta_y / delta_x
    

def preprocess_bounding_boxes(yolo_msg, log_to_console=False):
    # all boxes have an estimate ratio of the delta_y / delta_x = 1.9 (+- 0.25)
    # this function utilizes this property to artificially enlarge the bounding
    # which are located at the edge of the camera image in their x dimension, so they
    # can be matched with the clusters more easily, because the center in the x dimension
    # aligns with the center of the cluster
    processed_boxes = []
    threshold = 2.5
    desired_ratio = 2.3
    boundary_offset = 20
    for box in yolo_msg.bounding_boxes:
        if bb_ratio(box) > threshold:
        #     # check if box is at right or left boundary
        #     if box.min_x < boundary_offset:
        #         #left boundary
        #         min_x_ = box.max_x - (box.max_y - box.min_y) / desired_ratio
        #         box.min_x = min_x_
        #         if log_to_console:
        #             print(f"found bounding box (label {box.cone}) with unusual box_ratio at left image boundary.")
        #             print(f"new bb box: {box}")
        #     elif box.max_x > 640 - boundary_offset:
        #         #right boundary
        #         max_x_ = (box.max_y - box.min_y) / desired_ratio + box.min_x
        #         box.max_x = max_x_
        #         if log_to_console:
        #             print(f"found bounding box (label {box.cone}) with unusual box_ratio at right image boundary.")
        #             print(f"new bb box: {box}")
        #     else:
        #         if log_to_console:
        #             print(f"found bounding box (label {box.cone}) with unusual box_ratio but not at boundary of camera image")
        # processed_boxes.append(box)
            pass
        else:
            processed_boxes.append(box)
    yolo_msg.bounding_boxes = processed_boxes
    return yolo_msg

class Map:
    def __init__(self, size=10000, epsilon=100) -> None:
        # all distances are in mm
        self.size = size
        self.discretization_steps = 10 # = 1cm
        self.epsilon = epsilon
        self.dim = (int(size / self.discretization_steps), int(size / self.discretization_steps))
        self.data = np.zeros(self.dim) - 1
        
        self.y_errors = []
        self.x_errors = []
        
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
        hits = self.check_vicinity(x, y)
        if len(hits) > 0:
            print(f"new cone: {x}, {y}")
            for hit in hits:
                x_error = x - hit[0]
                y_error = y - hit[1]
                self.x_errors.append(x_error)
                self.y_errors.append(y_error)
                print(f"existing cone: {hit[0]}, {hit[1]}")
                print(f"errors: {x_error}  {y_error}")
        else:
            self.data[x, y] = cone
        
    
    def check_vicinity(self, X, Y):
        epsilon = int(self.epsilon / self.discretization_steps)
        hits = []
        for x in range(X - epsilon, X + epsilon + 1):
            for y in range(Y - epsilon, Y + epsilon):
                if self.data[x, y] != -1:
                    hits.append((x, y, self.data[x, y]))
        return hits
    
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
        self.fig.tight_layout()
        self.fig.savefig(IMSAVE_PATH)
        


# map = Map()

# map.set(0, 0, 90, 1500, -500, 1)
# map.save_plot()
