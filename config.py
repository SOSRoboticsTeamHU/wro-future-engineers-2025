# config.py

# Kamera IP-címek
FRONT_CAM_IP = "http://192.168.4.100:81/stream"
REAR_CAM_IP = "http://192.168.4.101:81/stream"

# config.py
MOTOR_FORWARD_PIN = 12
MOTOR_BACKWARD_PIN = 13
SERVO_PIN = 4

FRONT_CLEAR_THRESHOLD = 0.3
SIDE_CLEAR_THRESHOLD = 0.2  # Minimális biztonságos távolság (méter)

# HSV tartományok RGB alapján (piros, zöld, lila parkoló)
COLOR_RANGES = {
    "red": ((0, 100, 100), (10, 255, 255)),
    "green": ((50, 100, 100), (70, 255, 255)),
    "parking": ((140, 100, 100), (160, 255, 255))
}
