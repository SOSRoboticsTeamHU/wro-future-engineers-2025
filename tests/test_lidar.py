from lidar.lidar_module import LidarProcessor
from utils.logger import log
import time

lidar = LidarProcessor()

try:
    for i in range(5):  # 5 szkennelés
        scan = lidar.get_scan_data()
        result = lidar.find_clear_path(scan)
        log(f"Scan {i+1}: {result}")
        time.sleep(0.5)
finally:
    lidar.stop()
    log("LiDAR leállítva.")
