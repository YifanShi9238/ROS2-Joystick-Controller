# dice_detector_node.py
import cv2
import numpy as np
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

class DiceDetectorNode(Node):
    def __init__(self):
        super().__init__('dice_detector_node')
        self.bridge = CvBridge()
        self.sub = self.create_subscription(Image, '/camera/image_raw', self.image_callback, 10)
        self.pub = self.create_publisher(Int32MultiArray, '/dice_values', 10)

    def image_callback(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # --- simple blob detection for pips ---
        # This is where you detect dice and count dots
        dice_values = [3, 4]  # placeholder for detected values
        arr = Int32MultiArray(data=dice_values)
        self.pub.publish(arr)
