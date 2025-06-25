# config.py

# Kamera IP-címek
FRONT_CAM_IP = "http://192.168.4.100:81/stream"
REAR_CAM_IP = "http://192.168.4.101:81/stream"

# Motorvezérlés (GPIO lábak)
PWM_PIN = 18
DIR_PIN = 23

# Szervóvezérlés (MG996R)
SERVO_PIN = 12
SERVO_CENTER = 90
SERVO_LEFT = 45
SERVO_RIGHT = 135

# HSV tartományok RGB alapján (piros, zöld, lila parkoló)
COLOR_RANGES = {
    "red": ((0, 100, 100), (10, 255, 255)),
    "green": ((50, 100, 100), (70, 255, 255)),
    "parking": ((140, 100, 100), (160, 255, 255))
}
