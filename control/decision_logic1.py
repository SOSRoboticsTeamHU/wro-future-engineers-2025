#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ROS2 Decision Node with HuskyLens UART color override and 360° LIDAR obstacle avoidance.
Uses the provided huskylib Interface over serial UART.
Red (ID 1) → turn right; Green (ID 2) → turn left; else fallback to LIDAR logic.
"""
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import math
import time
import RPi.GPIO as GPIO
# Import the provided HuskyLens interface
from huskytools.huskylens import Interface as HuskyLensInterface, RecognitionAlgorithm
from control.motor_controller import MotorController
from control.steering_controller import SteeringController
from config import FRONT_CLEAR_THRESHOLD, SIDE_CLEAR_THRESHOLD


class DecisionNode(Node):
    def __init__(self):
        super().__init__('decision_node')

        self.motor = MotorController()
        self.steering = SteeringController()

        # Initialize HuskyLens over UART serial
        # Adjust port as needed (e.g. '/dev/ttyAMA0' or '/dev/ttyUSB0')
        port = '/dev/ttyAMA0'
        try:
            self.hl = HuskyLensInterface(port=port, baudrate=9600, timeout=1.0)
        except Exception as e:
            self.get_logger().error(f"❌ Unable to open HuskyLens serial port {port}: {e}")
            raise

        # Verify connection and set algorithm
        if not self.hl.knock():
            self.get_logger().warn('⚠️ HuskyLens did not respond to knock')
        self.hl.set_algorithm(RecognitionAlgorithm.COLOR_RECOGNITION)

        # Subscribe to LIDAR data
        self.create_subscription(
            LaserScan,
            '/scan',
            self.lidar_callback,
            qos_profile=rclpy.qos.qos_profile_sensor_data
        )

        self.get_logger().info(f'✅ Decision node started: HuskyLens on {port} + 360° LIDAR.')

    def lidar_callback(self, msg: LaserScan):
        # 1) Color override via HuskyLens UART
        try:
            blocks = self.hl.get_blocks()
        except Exception as e:
            self.get_logger().warn(f"⚠️ HuskyLens error: {e}")
            blocks = []

        if blocks:
            tag = blocks[0]
            if tag.id == 1:
                self.get_logger().info("🔴 Red detected → TURN RIGHT")
                self.steering.right()
                return
            elif tag.id == 2:
                self.get_logger().info("🟢 Green detected → TURN LEFT")
                self.steering.left()
                return

        # 2) Fallback: LIDAR-based obstacle avoidance
        def extract_distance(angle_deg):
            idx = int((angle_deg % 360) / (msg.angle_increment * (180 / math.pi)))
            if 0 <= idx < len(msg.ranges):
                val = msg.ranges[idx]
                if val and not math.isinf(val) and val > 0.01:
                    return val
            return None

        front = extract_distance(180)
        left = extract_distance(90)
        right = extract_distance(270)

        self.get_logger().info(
            f"📡 front: {front or 'inf'} m | left: {left or 'inf'} m | right: {right or 'inf'} m"
        )

        obstacle_ahead = front is None or front < FRONT_CLEAR_THRESHOLD
        obstacle_left = left is None or left < SIDE_CLEAR_THRESHOLD
        obstacle_right = right is None or right < SIDE_CLEAR_THRESHOLD

        if obstacle_ahead:
            if not obstacle_left:
                self.get_logger().info("↖ Obstacle ahead → Turn LEFT")
                self.motor.move_forward(0.4)
                self.steering.right()
            elif not obstacle_right:
                self.get_logger().info("↗ Obstacle ahead → Turn RIGHT")
                self.motor.move_forward(0.4)
                self.steering.left()
            else:
                self.get_logger().info("⛔ Surrounded → STOP")
                self.motor.stop()
        else:
            self.get_logger().info("🟢 Path clear → Move forward")
            self.motor.move_forward(0.6)
            self.steering.center()


def main():
    rclpy.init()
    node = DecisionNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
