import time
from utils.logger import log
from utils.timer import Timer

from camera.camera_module import get_camera_data
from lidar.lidar_module import LidarProcessor
from planning.decision_module import make_decision

def test_main_loop():
    log("TESZT: Vezérlési ciklus indul (motorok NEM aktívak)")
    lidar = LidarProcessor()
    timer = Timer()
    loop_delay = 0.5  # 2 Hz tesztciklus

    try:
        for i in range(10):  # 10 ciklus erejéig fusson
            # 1. Szenzoradatok beolvasása
            camera_data = get_camera_data()
            scan = lidar.get_scan_data()
            lidar_data = lidar.find_clear_path(scan)

            # 2. Döntéshozatal
            action = make_decision(camera_data, lidar_data)

            # 3. Csak logoljuk, nem vezérelünk
            log(f"[CAM] {camera_data} | [LIDAR] {lidar_data}")
            log(f"[DECISION] Speed={action['speed']} Steering={action['steering']}")
            time.sleep(loop_delay)

    except KeyboardInterrupt:
        log("Leállítás (Ctrl+C)")
    finally:
        lidar.stop()
        log("LiDAR leállítva")

if __name__ == "__main__":
    test_main_loop()
