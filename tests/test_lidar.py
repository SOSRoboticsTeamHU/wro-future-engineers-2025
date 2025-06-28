import rclpy
from lidar.lidar_processor import LidarProcessor

def main():
    rclpy.init()
    node = LidarProcessor()

    try:
        while rclpy.ok():
            rclpy.spin_once(node, timeout_sec=0.1)
            front = node.get_sector_distance(350, 10)
            left = node.get_sector_distance(80, 100)
            right = node.get_sector_distance(260, 280)
            print(f"🌐 ront: {front:.2f}m  |  Left: {left:.2f}m  |  Right: {right:.2f}m")
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
