#!/bin/bash
export ROS_DOMAIN_ID=31
source /opt/ros/humble/setup.bash
source /home/ubuntu/turtlebot-avai/install/setup.bash
ros2 run core_nodes opencr
