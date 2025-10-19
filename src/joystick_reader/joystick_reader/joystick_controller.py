#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist


class JoystickController(Node):
    def __init__(self):
        super().__init__('joystick_controller')

        # Subscribe to joystick inputs
        self.subscription = self.create_subscription(
            Joy, '/joy', self.joy_callback, 10)

        # Publisher for turtle velocity
        self.pub_cmd = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        self.get_logger().info('Joystick controller node started!')

    def joy_callback(self, msg: Joy):
        """Map Logitech F310 D-pad input to turtle motion."""
        twist = Twist()

        # For most Logitech F310 controllers in XInput mode:
        dpad_horizontal = msg.axes[6]  # left/right
        dpad_vertical = msg.axes[7]    # up/down

        # Tune the speed scales
        linear_speed = 2.0
        angular_speed = -2.0

        # Map D-pad movement to linear and angular velocity
        twist.linear.x = linear_speed * dpad_vertical
        twist.angular.z = -angular_speed * dpad_horizontal

        # Publish motion
        self.pub_cmd.publish(twist)

        # Print feedback
        self.get_logger().info(
            f"D-pad input -> linear: {twist.linear.x:.2f}, angular: {twist.angular.z:.2f}"
        )


def main(args=None):
    rclpy.init(args=args)
    node = JoystickController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
