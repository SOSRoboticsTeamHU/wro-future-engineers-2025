# Hardware Setup – WRO Future Engineers Car

## Microcontroller
- **Raspberry Pi 4 or 5**
- OS: Raspberry Pi OS (64-bit)

## Sensors
- **Camera**: Raspberry Pi Camera Module v2 (or compatible)
- **LiDAR**: YDLidar X4, USB connected

## Actuators
- **Drive Motor**: DC motor (PWM controlled via motor driver)
- **Steering**: Servo motor (controlled via GPIO or PCA9685)

## Wiring Guide

### Motor Driver (L298N or similar)
- IN1, IN2 → Pi GPIO
- ENA → PWM pin or PCA9685
- 12V input → Battery
- OUT1/OUT2 → DC motor

### Servo Motor
- Signal → GPIO or PCA9685 channel
- VCC → 5V
- GND → Common ground

### YDLidar X4
- Connect via USB
- Check `/dev/ttyUSB0` or use `ls /dev/tty*` to find device

### Power Supply
- Use external battery for motors (e.g. ParkSide 12V)
- Power Pi via USB-C (at least 3A recommended)
