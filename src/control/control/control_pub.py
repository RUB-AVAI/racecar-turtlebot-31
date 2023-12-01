# Copyright 2015 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
#import termios
import pygame
#import tty

import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node


class control_pub(Node):

    def __init__(self):
        super().__init__('control_pub')
        self.maxLinearVelocity = 0.26
        self.maxAngularVelocity = 1.82
        self.linearVelocityChangeValue = 0.01
        self.angularVelocityChangeValue = 0.1
        self.linearVelocity = 0.0  # backward/forward
        self.angularVelocity = 0.0  # sideways
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.timer = self.create_timer(0, self.callback)

    def callback(self):
            #while 1:
            try:
                #key = self.getKey()
                for event in pygame.event.get():
                    twist = Twist()
                    if event.type == pygame.KEYDOWN:
                        print(event.key)
                        if event.unicode == 'w':
                            self.linearVelocity += self.linearVelocityChangeValue
                        if event.unicode == 's':
                            self.linearVelocity -= self.linearVelocityChangeValue
                        if event.unicode == 'a':
                            self.angularVelocity += self.angularVelocityChangeValue
                        if event.unicode == 'd':
                            self.angularVelocity -= self.angularVelocityChangeValue
                        if event.unicode == 'e':
                            self.linearVelocity = 0.0
                            self.angularVelocity = 0.0

                        twist.linear.x = self.linearVelocity
                        twist.linear.y = 0.0
                        twist.linear.z = 0.0
                        twist.angular.x = 0.0
                        twist.angular.y = 0.0
                        twist.angular.z = self.angularVelocity
                        self.get_logger().info(
                            f'linearVelocity = {self.linearVelocity}, angularVelocity = {self.angularVelocity}')
                        self.publisher.publish(twist)
            except Exception as error:
                self.get_logger().info(error)

    def getKey(self):
        '''settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin)
        x = 0
        while x == 0:
            x = sys.stdin.read(1)[0]
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)'''

        return x

    def getLinearVelocity(self):
        return self.linearVelocity

    def getAngularVelocity(self):
        return self.angularVelocity

    def setLinearVelocity(self, value):
        self.linearVelocity = value

    def setAngularVelocity(self, value):
        self.angularVelocity = value


def main(args=None):
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Pygame Keyboard Test')

    rclpy.init(args=args)
    pub = control_pub()
    rclpy.spin(pub)

    pub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

