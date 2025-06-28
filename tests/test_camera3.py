from camera.camera_module_test import get_camera_frame

frame = get_camera_frame()

if frame is not None:
    print("📷 Kép érkezett, méret:", frame.shape)
else:
    print("❌ Nem kaptunk képet")