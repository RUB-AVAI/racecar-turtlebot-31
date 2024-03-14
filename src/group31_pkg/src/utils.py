import numpy as np
import matplotlib.pyplot as plt
import os
import math
from scipy.interpolate import interp1d
from data_fusion import FOV, VISUALISATION

IMSAVE_PATH = os.path.dirname(os.path.realpath(__file__)) + "/../../visualisations/global_map"
BLUE = 0
ORANGE = 1
YELLOW = 2

def get_timestamp_as_float(msg):
    return msg.header.stamp.sec + msg.header.stamp.nanosec / 1e9

# def secondary_fuse_criterion(cluster_range, box_range):
#     if box_range[0] < cluster_range[0] and cluster_range[0] < box_range[1]:
#         return True, 0
#     if box_range[0] < cluster_range[1] and cluster_range[1] < box_range[1]:
#         return True, 1
    
#     return False, None


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

def average_cluster_position(cluster_msg):
        cone_x_pos = np.mean(cluster_msg.x_positions)
        cone_y_pos = np.mean(cluster_msg.y_positions)
        
        return cone_x_pos, cone_y_pos



def center_of_range(range):
    return np.mean(range)

def bb_ratio(box):
    delta_x = np.abs(box.min_x - box.max_x)
    delta_y = np.abs(box.min_y - box.max_y)
    return delta_y / delta_x

def bb_surface(box):
    delta_x = np.abs(box.min_x - box.max_x)
    delta_y = np.abs(box.min_y - box.max_y)
    return delta_y * delta_x


data = np.load("data/data_1_merged.npy")
f = interp1d(data[:, 2], data[:, 0], bounds_error=True)

def estimate_cone_range(bounding_box):
    try:
        surface = bb_surface(bounding_box)
        range = f(surface)
    except ValueError:
        return None
    return range

def estimate_cone_angle(bounding_box):
    # we fitted a linear regression model to data we collected
    # regression model: f(x) = 213.02497443 - 0.10669489 * x
    
    box_x_position = (bounding_box.min_x + bounding_box.max_x) / 2
    return 213.02497443 - 0.10669489 * box_x_position

def estimate_cone_position(bounding_box):
    estimated_range = estimate_cone_range(bounding_box)
    if estimated_range is None:
        # cone does not lie in lidar range
        return None
    estimated_angle = estimate_cone_angle(bounding_box)
    radiant = estimated_angle / 360 * 2 * np.pi
    x = np.cos(radiant) * estimated_range
    y = np.sin(radiant) * estimated_range
    
    return (x, y)



def could_be_cone(cluster, max_size=200, max_range=4000):
    # rule out the ones that are too far away
    if np.mean(cluster.ranges) > max_range:
        return False
    # estimate size of cluster by calculating difference between edges
    left_edge = (cluster.x_positions[0], cluster.y_positions[0])
    right_edge = (cluster.x_positions[-1], cluster.y_positions[-1])
    tmp = (left_edge[0] - right_edge[0], left_edge[1] - right_edge[1])
    distance = np.linalg.norm(tmp)
    if distance > max_size:
        return False
    
    return True
    

fig, ax = plt.subplots()

def plot_clusters_and_cones(clusters, cone_positions, labels):
    IMSAVE_PATH = os.path.dirname(os.path.realpath(__file__)) + "/../../visualisations/cones_and_clusters"
    
    plt.axis("equal")
    ax.clear()

    blindspot = plt.Circle((0, 0), 90, color="red", fill=False)
    ax.add_patch(blindspot)
    
    
    
    colors = ["blue", "orange", "yellow"]
    
    for label, position in zip(labels, cone_positions):
        # scatter each cluster individually so they get different colors
        cone = plt.Circle((position[0], position[1]), 100, color = colors[label], fill=True)
        ax.add_patch(cone)
        
    for cluster in clusters:
        # scatter each cluster individually so they get different colors
        ax.scatter(cluster.x_positions, cluster.y_positions, marker=".")
        
    limit = 5000 # mm
    ax.set_xlim([-limit, limit])
    ax.set_ylim([-limit, limit])
    ax.set_box_aspect(1)
        
    fig.tight_layout()
    fig.savefig(IMSAVE_PATH)
    

def plot_clusters(clusters):
    IMSAVE_PATH = os.path.dirname(os.path.realpath(__file__)) + "/../../visualisations/pl"
    plt.axis("equal")
    ax.clear()

    blindspot = plt.Circle((0, 0), 90, color="red", fill=False)
    ax.add_patch(blindspot)
    
    for cluster in clusters:
        # scatter each cluster individually so they get different colors
        ax.scatter(cluster.x_positions, cluster.y_positions, marker=".")
    limit = 5000 # mm
    ax.set_xlim([-limit, limit])
    ax.set_ylim([-limit, limit])
    ax.set_box_aspect(1)
        
    fig.tight_layout()
    fig.savefig(IMSAVE_PATH)


def plot_cones(positions, labels):
    IMSAVE_PATH = os.path.dirname(os.path.realpath(__file__)) + "/../../visualisations/estimated_cone_positions"
    plt.axis("equal")
    ax.clear()

    blindspot = plt.Circle((0, 0), 90, color="red", fill=False)
    ax.add_patch(blindspot)
    
    colors = ["blue", "orange", "yellow"]
    
    for label, position in zip(labels, positions):
        # scatter each cluster individually so they get different colors
        cone = plt.Circle((position[0], position[1]), 100, color = colors[label], fill=True)
        ax.add_patch(cone)
        
    limit = 5000 # mm
    ax.set_xlim([-limit, limit])
    ax.set_ylim([-limit, limit])
    ax.set_box_aspect(1)
        
    fig.tight_layout()
    fig.savefig(IMSAVE_PATH)
    
    
    

def preprocess_bounding_boxes(yolo_msg, log_to_console=False):
    # all boxes have an estimate ratio of the delta_y / delta_x = 1.9 (+- 0.25)
    # this function utilizes this property to artificially enlarge the bounding
    # which are located at the edge of the camera image in their x dimension, so they
    # can be matched with the clusters more easily, because the center in the x dimension
    # aligns with the center of the cluster
    processed_boxes = []
    threshold = 3.0
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
    def __init__(self, size=20000, epsilon=100, min_hist=3) -> None:
        # all distances are in mm
        self.size = size
        self.discretization_steps = 10 # = 1cm
        self.epsilon = epsilon
        self.min_hist = min_hist
        self.dim = (int(size / self.discretization_steps), int(size / self.discretization_steps), 2)
        self.data = np.zeros(self.dim, dtype=np.int8)
        self.data[:, :, 0] = -1
        
        self.y_errors = []
        self.x_errors = []
        
        self.start_pos = (0, 0)
        
        
        self.last_seen_size = 10
        self.last_seen = [(None, None)] * self.last_seen_size
        self.last_seen_idx = -1
        
        self.last_blue = (None, None)
        self.last_yellow = (None, None)
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
        if len(hits) == 1:
            # print(f"new cone: {x}, {y}")
            hit = hits[0]
            self.data[hit[0], hit[1], 1] += 1
            if self.data[hit[0], hit[1], 1] >= self.min_hist:
                self.last_seen_idx = (self.last_seen_idx + 1) % self.last_seen_size
                self.last_seen[self.last_seen_idx % self.last_seen_size] = (hit[0], hit[1])
                
                # old approach
                if self.data[hit[0], hit[1], 0] == BLUE:
                    self.last_blue = (hit[0], hit[1])
                elif self.data[hit[0], hit[1], 0] == YELLOW:
                    self.last_yellow = (hit[0], hit[1])
            x_error = x - hit[0]
            y_error = y - hit[1]
            self.x_errors.append(x_error)
            self.y_errors.append(y_error)
            # print(f"existing cone: {hit[0]}, {hit[1]}")
            # print(f"errors: {x_error}  {y_error}")
        elif len(hits) > 1:
            print(hits)
            print("not adding a cone because of multiambiguity")
        else:
            self.data[x, y, 0] = cone
            self.data[x, y, 1] = 1
            
            
    def estimate_new_target(self):
        # # returns (x, y, angle). eiter x and y are NOne or angle is None, since tbot should only drive or turn
        # TURN_ANGLE = 20
        # N = 5
        # history = []
        
        # for i in range(N):
        #     history.append(self.last_seen[(self.last_seen_idx - i) % self.last_seen_size])
        
        
        
        # yellows = 0
        # blues = 0
        # last_blue = None
        # last_yellow = None
        
        # for i, (x, y) in enumerate(history):
        #     if x is None:
        #         break
            
        #     if self.data[x, y, 0] == YELLOW:
        #         if last_yellow is None:
        #             last_yellow = (x, y)
        #         yellows += 1
        #     if self.data[x, y, 0] == BLUE:
        #         if last_blue is None:
        #             last_blue = (x, y)
        #         blues += 1
        
        # if yellows == N:
        #     # only saw yellows, turn left
        #     pass
        #     # return None, None, -TURN_ANGLE
        # elif blues == N:
        #     # only saw blues, turn right
        #     pass
        #     # return None, None, TURN_ANGLE
        # elif last_blue and last_yellow:
        #     # drive to center of blue and yellow
        #     (bx, by) = last_blue
        #     (yx, yy) = last_yellow
        #     bx *= self.discretization_steps
        #     by *= self.discretization_steps
        #     yx *= self.discretization_steps
        #     yy *= self.discretization_steps
            
        #     bx -= self.size / 2
        #     by -= self.size / 2
        #     yx -= self.size / 2
        #     yy -= self.size / 2
            
        #     return ((bx + yx) / 2, (by + yy) / 2, None)
        # return None, None, None
        
        
        
        
        
        
        
        
        
        
        if self.last_blue[0] is not None and self.last_yellow[0] is not None:
            (bx, by) = self.last_blue
            (yx, yy) = self.last_yellow
            bx *= self.discretization_steps
            by *= self.discretization_steps
            yx *= self.discretization_steps
            yy *= self.discretization_steps
            
            bx -= self.size / 2
            by -= self.size / 2
            yx -= self.size / 2
            yy -= self.size / 2
            
            return ((bx + yx) / 2, (by + yy) / 2, None)
        else:
            print("could not find blue and yellow cones to create a point")
            return None, None, None
        
    
    def check_vicinity(self, X, Y):
        epsilon = int(self.epsilon / self.discretization_steps)
        hits = []
        for x in range(X - epsilon, X + epsilon + 1):
            for y in range(Y - epsilon, Y + epsilon):
                if self.data[x, y, 0] != -1:
                    hits.append((x, y, self.data[x, y]))
        return hits
    
    def get_cones(self):
        # only to be called from outside since it gives back positions, not indices
        valid_positions = [[], [], []]
        for i in [0, 1, 2]:
            cone_positions = (np.argwhere(self.data[:, :, 0] == i))
            for cone_pos in cone_positions:
                if self.data[cone_pos[0], cone_pos[1], 1] >= self.min_hist:
                    valid_positions[i].append(cone_pos * self.discretization_steps)
        
        return valid_positions
            
        
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
