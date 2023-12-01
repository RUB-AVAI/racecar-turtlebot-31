#!/bin/bash
export ROS_DOMAIN_ID=31
source /opt/ros/humble/setup.bash
cd /opt/ros/humble/share/hls_lfcd_lds_driver/launch
ros2 launch hlds_laser.launch.py
