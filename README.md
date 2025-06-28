# WRO 2025 – Future Engineers Autonomous Car

# 🤖 WRO Future Engineers 2025 — Autonomous RC Car

This repository contains the complete codebase for our self-driving RC car developed for the **WRO Future Engineers 2025** competition. The robot is built using a Raspberry Pi 5, a 360° LiDAR (YDLidar X4), dual camera streams (ESP32-CAM), and GPIO-based control for the motor and steering systems.

---

## 📦 Project Structure

wro_robot/
├── camera/
│ ├── init.py
│ └── camera_module.py # Handles front/rear camera color detection
├── control/
│ ├── init.py
│ ├── motor_controller.py # Motor control (PWM GPIO)
│ ├── steering_controller.py # Servo-based steering control
│ └── decision_logic.py # Main logic (LIDAR-based obstacle avoidance + camera handling)
├── lidar/
│ ├── init.py
│ └── lidar_test_node.py # ROS 2 listener node for /scan topic
├── planning/
│ └── init.py # (reserved for future logic)
├── config.py # Centralized GPIO configuration
├── main.py # Optional CLI entry point
└── tests/
├── test_motor.py
├── test_steering.py
└── test_lidar_listener.py


---

## 🚘 Core Functionalities

| Round | Behavior |
|-------|----------|
| **1** | LiDAR-based 360° obstacle avoidance |
| **2** | LiDAR navigation + color-based direction adjustment (red = pass right, green = pass left) |
| **3** | Upon detecting **magenta**, stop and simulate parking |

---

## 🧠 Technologies

- **Language:** Python 3.12
- **Robot OS:** ROS 2 Jazzy (for LiDAR integration)
- **LiDAR:** YDLidar X4 (ROS 2 `/scan` topic)
- **Camera:** ESP32-CAM with WiFi MJPEG stream
- **Motor/Servo Control:** `gpiozero`, no pigpio
- **GPIO Pins:**
  - Motor: GPIO 12 (forward), GPIO 13 (backward)
  - Servo: GPIO 4 (steering)

## 📁 Structure
- `camera/`: vision processing
- `lidar/`: obstacle detection
- `control/`: PID and motion control
- `planning/`: decision logic
- `utils/`: logging and tools

## 📦 Requirements
See `requirements.txt` for Python libraries.

## 🛠️ Setup
1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the main program:
```bash
python main.py
```

## 📸 Media
Check the `media/` folder for videos and pictures of the robot in action.

## ⚙️ License
MIT License
