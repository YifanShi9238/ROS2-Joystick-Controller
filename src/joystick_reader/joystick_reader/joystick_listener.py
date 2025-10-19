#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy

class JoystickListener(Node):
    def __init__(self):
        super().__init__('joystick_test')
        self.subscription = self.create_subscription(
            Joy, '/joy', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning
        self.get_logger().info('Joystick listener node started!')

    def listener_callback(self, msg: Joy):
        # Print axes and buttons clearly
        print("\n--- Joystick Input ---")
        for i, val in enumerate(msg.axes):
            print(f"Axis {i}: {val:.3f}")
        for i, val in enumerate(msg.buttons):
            print(f"Button {i}: {'Pressed' if val else 'Released'}")

def main(args=None):
    rclpy.init(args=args)
    node = JoystickListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

