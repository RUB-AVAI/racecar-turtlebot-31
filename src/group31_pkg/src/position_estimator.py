import os
import rclpy
import numpy as np
import matplotlib.pyplot as plt
from rclpy.node import Node
from message_filters import ApproximateTimeSynchronizer, Subscriber
from avai_messages.msg import Estimator_Position, Velocities
from sensor_msgs.msg import LaserScan
from time import sleep

class KalmanFilter:
    def __init__(self, initial_state, process_covariance, measurement_covariance, state_transition, identity_matrix_size):
        self.state = np.array(initial_state, dtype=float)
        self.state_estimate = self.state.copy()
        
        self.process_covariance = np.array(process_covariance, dtype=float)
        self.measurement_covariance = np.array(measurement_covariance, dtype=float)
        self.state_transition = np.array(state_transition, dtype=float)
        self.identity_matrix = np.identity(identity_matrix_size)


    def predict(self):
        # Predict the next state
        self.state = np.dot(self.state_transition, self.state)
        # Update the state covariance matrix
        self.process_covariance = np.dot(np.dot(self.state_transition, self.process_covariance),
                                         self.state_transition.T)


    def update(self, measurement):
        # Compute Kalman gain
        kalman_gain = np.dot(
            np.dot(self.process_covariance, self.identity_matrix.T), 
            np.linalg.inv(np.dot(np.dot(self.identity_matrix, self.process_covariance), self.identity_matrix.T) + self.measurement_covariance)
        )

        # Update the state estimate
        self.state_estimate = self.state + np.dot(kalman_gain, measurement - np.dot(self.identity_matrix, self.state))

        # Update the state covariance matrix
        self.process_covariance = np.dot((self.identity_matrix - np.dot(kalman_gain, self.identity_matrix)), self.process_covariance)


class PositionEstimator(Node):
    def __init__(self):
        super().__init__('position_estimator')
        
        self.position_publisher()
        
        self.USE_KALMAN = False
    
        # Start position
        self.x = 0
        self.y = 0
        self.phi = 0
        
        # Kalman Filter
        process_covariance = [[0, 0], [0, 0]]
        measurement_covariance = [[0, 0], [0, 0]]
        state_transition = [[0, 0], [0, 0]]
        
        if self.USE_KALMAN:
            self.filter = KalmanFilter(
                initial_state=[self.x, self.y],
                process_covariance=process_covariance,
                measurement_covariance=measurement_covariance,
                state_transition=state_transition,
                identity_matrix_size=2
            )
