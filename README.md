# ROS2-Joystick-Controller
The lightning_talk_demo branch is built for quick demostration and try out by any new-to-ROS2 developer with a controller that is compatible with the underlying operation system, typically Linux (playstation, xbox, etc) on joy package functionality on ROS2.  

## System Requirement
This codebase is develop under ROS2 Jazzy Jalisco with python version 3.12. To install ROS2 Jazzy, checkout ROS2 Jazzy Installation Official Guide: https://docs.ros.org/en/jazzy/Installation.html

## Quick Start
git clone https://github.com/YifanShi9238/ROS2-Joystick-Controller.git
cd ROS2-Joystick-Controller
git checkout lightning_talk_demo
colcon build && . install/setup.bash

## Demo 1: Joystick Listener demo
After plugged in controller 
lsusb to check usb connection
ros2 run joy joy_node
ros2 run joystick_reader joystick_listener

## Demo 2: Joystick Turtlesim demo
ros2 launch joystick_reader turtle_joy.launch.py

## License
This project is licensed under the Apache License 2.0 — see the [LICENSE](./LICENSE) file for details.
