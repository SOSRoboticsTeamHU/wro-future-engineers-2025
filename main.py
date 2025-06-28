from control.motor_controller import MotorController
from control.steering_controller import SteeringController
from control.decision_logic import make_decision  # ezt majd írjuk
import time

motor = MotorController()
steering = SteeringController()

while True:
    decision = make_decision()  # pl. "GO", "TURN LEFT", stb.

    if decision == "GO":
        motor.forward()
        steering.center()
    elif decision == "TURN LEFT":
        motor.forward()
        steering.turn(-30)
    elif decision == "TURN RIGHT":
        motor.forward()
        steering.turn(30)
    elif decision == "REVERSE":
        motor.backward()
        steering.center()
    else:
        motor.stop()
        steering.center()

    time.sleep(0.1)
