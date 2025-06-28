# 🤖 WRO Future Engineers 2025 – Autonomous Robot System

This repository contains the full software stack for our WRO 2025 Future Engineers autonomous RC car, built on **Raspberry Pi 5** with a **360° LiDAR**, dual **ESP32-CAM** modules, and **HuskyLens UART** vision.

---

## 🧠 Features

- ✅ **ROS 2 Jazzy-based LIDAR obstacle avoidance**
- 🎨 **Color detection with HuskyLens over UART**
  - 🔴 Red = turn right
  - 🟢 Green = turn left
- 🚗 **Motor and steering control via GPIO**
- 🔁 Auto-launch system on boot (via `systemd`)
- 🛠️ Modular code structure for maintainability

---

## 🛠 Hardware Overview

Component	Details
- 🧠 Controller	Raspberry Pi 5
- 🛰️ Sensors	YDLidar X4, 2x ESP32-CAM, HuskyLens
- 🔋 Power	External battery
- 🛞 Drive	1x DC Motor (H-Bridge) + Servo
- 🧰 GPIO Pins	Motor: GPIO 32, 33 / Servo: GPIO 12
- 🧪 Platform	ROS 2 Jazzy + Python 3.12
- 🧪 Modes of Operation

1️⃣ Round 1 – LIDAR-only obstacle avoidance
2️⃣ Round 2 – HuskyLens color override + LIDAR

## 🧩 External Dependencies

huskytools Python package for UART HuskyLens
gpiozero, RPi.GPIO for hardware control
ROS 2 Jazzy runtime (manages /scan topic for LIDAR)

---

## 📸 Sample Output (on boot)

✅ Decision node started: HuskyLens on /dev/ttyAMA0 + 360° LIDAR.
📡 front: 0.34 m | left: 0.55 m | right: inf
🟢 Path clear → Move forward
📘 License

MIT License – free to use, modify, and distribute.

Made with ❤️ by the WRO Future Engineers SOS Robotics Team – 2025
