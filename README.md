# ROS2-Joystick-Controller
The `lightning_talk_demo branch` is built for quick demostration and try out by any new-to-ROS2 developer with a controller that is compatible with the underlying operation system, typically Linux (playstation, xbox, etc) on joy package functionality on ROS2.  

## System Requirement
This codebase is developed under **ROS2 Jazzy Jalisco** with **Python version 3.12**. To install ROS2 Jazzy, follow the installation steps in [ROS2 Jazzy Installation Official Guide](https://docs.ros.org/en/jazzy/Installation.html)

## Quick Start
```
git clone https://github.com/YifanShi9238/ROS2-Joystick-Controller.git
cd ROS2-Joystick-Controller
git checkout lightning_talk_demo
colcon build && . install/setup.bash
```

## Demo 1: Joystick Listener demo
After plugged in controller, check usb connection of your controller by typing.
```
lsusb
```
Then running
```
ros2 run joy joy_node</pre>
ros2 run joystick_reader joystick_listener
```
<img width="2354" height="399" alt="Screenshot from 2025-10-21 22-52-58" src="https://github.com/user-attachments/assets/e7ad70bc-8ef2-43ee-9d1a-c32a067c7108" />
Figure 1. rqt_graph of the running nodes with one publisher and subscriber.

## Demo 2: Joystick Turtlesim demo
```
ros2 launch joystick_reader turtle_joy.launch.py
```

<img width="2353" height="728" alt="Screenshot from 2025-10-21 21-30-14" src="https://github.com/user-attachments/assets/d440f16a-8bd9-443d-b99f-fd295990581f" />
Figure 2. rqt_graph of the running nodes with two publishers and subscribers.
<span style="color:red">This text is red</span>


## Resource
For more information about joy packages, [joy - ROS Package Overview](https://index.ros.org/p/joy/#jazzy).
For more information about turtlesim & rqt, [Turtlesim & rqt Guide](https://docs.ros.org/en/jazzy/Tutorials/Beginner-CLI-Tools/Introducing-Turtlesim/Introducing-Turtlesim.html).

## License
This project is licensed under the Apache License 2.0 — see the [LICENSE](./LICENSE) file for details.
