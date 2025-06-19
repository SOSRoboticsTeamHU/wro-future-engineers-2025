from camera.camera_module import get_camera_data
from utils.logger import log
import time

def test_camera_streams():
    log("CAMTEST: kamera stream teszt indul...")
    
    try:
        for i in range(10):  # 10 mintavétel
            data = get_camera_data()

            log(f"[{i+1}] Kamera adat: {data}")
            time.sleep(0.5)

    except KeyboardInterrupt:
        log("CAMTEST megszakítva (Ctrl+C)")
    except Exception as e:
        log(f"⚠️ Hiba: {e}")

    log("CAMTEST kész.")

if __name__ == "__main__":
    test_camera_streams()
