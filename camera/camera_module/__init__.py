import cv2
import numpy as np
from config import FRONT_CAM_STREAM, REAR_CAM_STREAM

RED_LOWER = np.array([0, 100, 100])
RED_UPPER = np.array([10, 255, 255])

GREEN_LOWER = np.array([50, 100, 100])
GREEN_UPPER = np.array([70, 255, 255])

MAGENTA_LOWER = np.array([140, 100, 100])
MAGENTA_UPPER = np.array([160, 255, 255])

POLE_DETECTION_THRESHOLD = 5000  # pixelösszeg (jobb/bal oldalon)
PARKING_DETECTION_THRESHOLD = 5000  # pixelösszeg (kép alján)

def detect_color_area(frame, lower_hsv, upper_hsv):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    return mask

def analyze_front_camera():
    cap = cv2.VideoCapture(FRONT_CAM_STREAM)
    ret, frame = cap.read()
    cap.release()

    if not ret or frame is None:
        return {'pole_color': None}

    red_mask = detect_color_area(frame, RED_LOWER, RED_UPPER)
    green_mask = detect_color_area(frame, GREEN_LOWER, GREEN_UPPER)

    height, width = frame.shape[:2]
    left_area = green_mask[:, :width//2]
    right_area = red_mask[:, width//2:]

    if np.sum(left_area) > POLE_DETECTION_THRESHOLD:
        return {'pole_color': 'green'}
    elif np.sum(right_area) > POLE_DETECTION_THRESHOLD:
        return {'pole_color': 'red'}
    else:
        return {'pole_color': None}

def analyze_rear_camera():
    cap = cv2.VideoCapture(REAR_CAM_STREAM)
    ret, frame = cap.read()
    cap.release()

    if not ret or frame is None:
        return {'parking_detected': False}

    magenta_mask = detect_color_area(frame, MAGENTA_LOWER, MAGENTA_UPPER)

    height, width = frame.shape[:2]
    lower_section = magenta_mask[int(height * 0.7):, :]

    if np.sum(lower_section) > PARKING_DETECTION_THRESHOLD:
        return {'parking_detected': True}
    else:
        return {'parking_detected': False}

def get_camera_data():
    cam_data = {}
    cam_data.update(analyze_front_camera())
    cam_data.update(analyze_rear_camera())
    return cam_data
