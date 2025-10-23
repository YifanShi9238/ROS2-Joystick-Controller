# ROS2-Joystick-Controller
The lightning_talk_demo branch is built for quick demostration and try out by any new-to-ROS2 developer with a controller that is compatible with the underlying operation system, typically Linux (playstation, xbox, etc) on joy package functionality on ROS2.  

## System Requirement
This codebase is develop under ROS2 Jazzy Jalisco with Python version 3.12. To install ROS2 Jazzy, checkout ROS2 Jazzy Installation Official Guide: https://docs.ros.org/en/jazzy/Installation.html
<img width="307" height="283" alt="Screenshot from 2025-10-21 21-40-55" src="https://github.com/user-attachments/assets/8c64b7b6-ce8e-4276-a332-b784c0727226" />

## Quick Start
<pre>'''git clone https://github.com/YifanShi9238/ROS2-Joystick-Controller.git
cd ROS2-Joystick-Controller
git checkout lightning_talk_demo
colcon build && . install/setup.bash'''</pre>

## Demo 1: Joystick Listener demo
After plugged in controller 
'lsusb' to check usb connection
<pre>'''ros2 run joy joy_node
ros2 run joystick_reader joystick_listener'''</pre>
<img width="2354" height="399" alt="Screenshot from 2025-10-21 22-52-58" src="https://github.com/user-attachments/assets/e7ad70bc-8ef2-43ee-9d1a-c32a067c7108" />


## Demo 2: Joystick Turtlesim demo
<pre>'''ros2 launch joystick_reader turtle_joy.launch.py'''</pre>
<img width="2353" height="728" alt="Screenshot from 2025-10-21 21-30-14" src="https://github.com/user-attachments/assets/d440f16a-8bd9-443d-b99f-fd295990581f" />


## Resource
For more information about joy packages, checkout: https://index.ros.org/p/joy/#jazzy
For more information about turtlesim & rqt, checkout: https://docs.ros.org/en/jazzy/Tutorials/Beginner-CLI-Tools/Introducing-Turtlesim/Introducing-Turtlesim.html

## License
This project is licensed under the Apache License 2.0 — see the [LICENSE](./LICENSE) file for details.
