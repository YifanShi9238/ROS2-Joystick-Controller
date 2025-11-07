from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Node(package='dice_roller', executable='dice_roller_node', output='screen'),
        Node(package='dice_roller', executable='dice_detector_node', output='screen'),
        Node(package='dice_roller', executable='dice_math_node', output='screen'),
        # Node(package='v4l2_camera', executable='v4l2_camera_node', output='screen'),
    ])