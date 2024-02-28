import numpy as np

TOTAL_LEFT_MOVED, TOTAL_RIGHT_MOVED = 0, 0
WHEEL_DISTANCE = 57 #TODO: get wheel distance of turle bot

START_X = 140
START_Y = 50
START_RAD = 0
START_POSITIONS = [[230, 50], [140, 50], [50, 50]]
END_POSITIONS = [[230, 360], [140, 360], [50, 360]]
LAMBDA = 0.5 # forward direction
LAMBDA_TAR = 0.5 # Repelling force of obstacles

beta_1 = 0
beta_2 = 0
sigma = 0

#TODO: Get maximal velocity that should be assignes
MAX_VELOCITY = 1

#TODO: Get timestep
TIMESTEP = 0


#TODO: get lidar data and make data on same scale
PSI_OBS = np.deg2rad(range(-180, 180))
lidar_data = 0


def getDeltaPhi(lam, phi, psi):
    """
    Returns the new direction of robot
    """
    f_obs = 0
    for psi_obs_i in PSI_OBS:
        f_obs += f_obs_i(psi_obs_i, lidar_data, beta_1, beta_2, sigma)
    return f_tar(lam, phi, psi) + f_obs


def f_tar(lam_tar, phi, psi_tar):
    """
    Influence from target dynamics
    
    lam_tar: turning speed of the robot. Unit radians/s 
    phi: current direction in global coordinate system in radians
    psi_tar: direction of target in global coordinate system in radians
    
    returns influence of target to new phi
    """
    return -lam_tar * np.sin(phi - psi_tar)


def f_obs_i(psi_obs, lidar_data_i, beta_1, beta_2, sigma):
    """
    Creates repellors at the locations of obstacles
    
    psi_obs_i: direction in radians
    lidar_data_i: distance
    beta_1, beta_2, sigma: Positive constants
    
    Returns influence of psi_obs
    """
    lambda_ops_i = lambda_obs(lidar_data_i, beta_1, beta_2)
    exp_arg = (psi_obs**2)/(2*sigma**2)
    return lambda_ops_i*(psi_obs)*np.exp(-exp_arg)

def lambda_obs(d, beta_1, beta_2):
    """
    weight function
    """
    return beta_1 * np.exp(-d/beta_2)


def getVelocity(deltaPhi):
    """
    Returns the velocity that should be given to the wheels
    """
    velocity = (deltaPhi * (WHEEL_DISTANCE/2))/TIMESTEP
    if np.abs(LAMBDA) >= MAX_VELOCITY:
        return 0
    elif velocity > MAX_VELOCITY - LAMBDA:
        return MAX_VELOCITY - LAMBDA
    elif velocity < -MAX_VELOCITY + LAMBDA:
        return -MAX_VELOCITY + LAMBDA
    return velocity

def getDirection(x_start, y_start, x_end, y_end):
    """
    Calculates the heading direction
    """
    return -np.arctan2(y_start-y_end, x_start-x_end)

#TODO: make work with turlebot
def updateMovement(now_x, now_y, old_phi):
    """
    Updates the movement
    """
    global TOTAL_RIGHT_MOVED, TOTAL_LEFT_MOVED
    
    right_moved = encoder_right.getValue() * 20
    right_now_moved =  right_moved - TOTAL_RIGHT_MOVED
    TOTAL_RIGHT_MOVED = right_moved
    
    left_moved = encoder_left.getValue() * 20
    left_now_moved = left_moved - TOTAL_LEFT_MOVED
    TOTAL_LEFT_MOVED = left_moved
    
    new_phi = (old_phi + (right_now_moved - left_now_moved) / WHEEL_DISTANCE) % (2*np.pi)
    
    c = (left_now_moved + right_now_moved) / 2
    new_x = now_x - c * np.cos(new_phi)
    new_y = now_y + c * np.sin(new_phi)
    return new_x, new_y, new_phi


#TODO: make work with turtlebot
def setVelocity(v_l, v_r):
    """
    sets the new velocity
    """
    motor_left.setVelocity(v_l)
    motor_right.setVelocity(v_r)


def drive(x, y, phi, end_x, end_y):
     X_ARR, Y_ARR = [], []
     while True:
        #robot.step(timestep)
        psi = getDirection(x, y, end_x, end_y)
        delta_phi = getDeltaPhi(LAMBDA_TAR, phi, psi)
        v = getVelocity(delta_phi)
        setVelocity(-v+LAMBDA, v+LAMBDA)
        x, y, phi = updateMovement(x, y, phi)
        X_ARR.append(x), Y_ARR.append(y)
        