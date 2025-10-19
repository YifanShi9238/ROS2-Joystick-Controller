from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        # Launch the turtlesim window
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim',
            output='screen'
        ),

        # Launch the joystick driver
        Node(
            package='joy',
            executable='joy_node',
            name='joy_node',
            output='screen'
        ),

        # # Launch your custom joystick listener node
        # Node(
        #     package='joystick_',
        #     executable='joystick_listener',
        #     name='joystick_listener',
        #     output='screen'
        # ),

        Node(
            package='joystick_reader',
            executable='joystick_controller',
            output='screen'
        ),
    ])
