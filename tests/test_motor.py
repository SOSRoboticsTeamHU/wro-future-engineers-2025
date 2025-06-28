from control.motor_controller import MotorController
from time import sleep

motor = MotorController()

print("Előre 70%")
motor.move_forward(0.7)
sleep(2)

print("Hátra 50%")
motor.move_backward(0.5)
sleep(2)

print("Stop")
motor.stop()
