# motor_control.py
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Pins to be defined in config.py
from config import MOTOR_PWM_PIN, MOTOR_DIR_PIN, SERVO_PIN

GPIO.setup(MOTOR_PWM_PIN, GPIO.OUT)
GPIO.setup(MOTOR_DIR_PIN, GPIO.OUT)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Motor PWM
motor_pwm = GPIO.PWM(MOTOR_PWM_PIN, 1000)  # 1kHz
motor_pwm.start(0)

# Servo PWM
servo = GPIO.PWM(SERVO_PIN, 50)  # 50Hz for MG996R
servo.start(7.5)  # Middle position

def set_motor(speed: float):
    # speed: -1.0 (full reverse) to 1.0 (full forward)
    direction = GPIO.HIGH if speed >= 0 else GPIO.LOW
    duty_cycle = min(abs(speed), 1.0) * 100

    GPIO.output(MOTOR_DIR_PIN, direction)
    motor_pwm.ChangeDutyCycle(duty_cycle)

def set_steering(angle: float):
    # angle: -1.0 (left) to 1.0 (right)
    duty_cycle = 7.5 + (angle * 2.5)  # -1.0 => 5.0, 0.0 => 7.5, 1.0 => 10.0
    servo.ChangeDutyCycle(duty_cycle)

def stop():
    motor_pwm.ChangeDutyCycle(0)
    servo.ChangeDutyCycle(7.5)

# Cleanup on exit
def cleanup():
    motor_pwm.stop()
    servo.stop()
    GPIO.cleanup()

# Example (to be deleted later)
if __name__ == '__main__':
    try:
        set_motor(0.5)
        set_steering(0.3)
        time.sleep(2)
        stop()
    finally:
        cleanup()
