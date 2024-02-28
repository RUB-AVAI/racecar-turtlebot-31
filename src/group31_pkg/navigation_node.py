import numpy as np

TOTAL_LEFT_MOVED, TOTAL_RIGHT_MOVED = 0, 0
WHEEL_DISTANCE = 57

START_X = 140
START_Y = 50
START_RAD = 0
START_POSITIONS = [[230, 50], [140, 50], [50, 50]]
END_POSITIONS = [[230, 360], [140, 360], [50, 360]]
LAMBDA, LAMBDA_TAR = 0.5, 0.5


def f_tar(lam_tar, phi, psi_tar):
    """
    Influence from target dynamics
    
    lam: 
    """
    return -lam * np.sin(phi - psi)
