# dice_math_node.py
from std_msgs.msg import Int32MultiArray, Int32

class DiceMathNode(Node):
    def __init__(self):
        super().__init__('dice_math_node')
        self.sub = self.create_subscription(Int32MultiArray, '/dice_values', self.callback, 10)
        self.pub = self.create_publisher(Int32, '/dice_sum', 10)

    def callback(self, msg):
        total = 0
        for val in msg.data:
            opp = 7 - val
            total += opp
        self.pub.publish(Int32(data=total))
        self.get_logger().info(f'Opposite sides sum: {total}')
