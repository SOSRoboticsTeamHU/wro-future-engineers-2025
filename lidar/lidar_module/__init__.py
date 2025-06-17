from rplidar import RPLidar
from config import LIDAR_PORT
import numpy as np

class LidarProcessor:
    def __init__(self, port=LIDAR_PORT):
        self.lidar = RPLidar(port)
        self.lidar.connect()

    def get_scan_data(self):
        scan = []
        for scan_data in self.lidar.iter_scans(max_buf_meas=500):
            scan = scan_data
            break
        return scan

    def find_clear_path(self, scan, min_distance=300):
        angles = []
        for _, angle, dist in scan:
            if dist > min_distance:
                angles.append(angle)

        if not angles:
            return {'free_angle': 180.0, 'obstacle_ahead': True, 'obstacle_distance': 0.0}

        angle_array = np.array(angles)
        mean_angle = np.mean(angle_array)

        obstacle_distance = 9999
        for _, angle, dist in scan:
            if 170 <= angle <= 190:
                obstacle_distance = min(obstacle_distance, dist)

        return {
            'free_angle': mean_angle,
            'obstacle_ahead': obstacle_distance < min_distance,
            'obstacle_distance': obstacle_distance / 1000  # méterben
        }

    def stop(self):
        self.lidar.stop()
        self.lidar.disconnect()
