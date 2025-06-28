from control.steering_controller import SteeringController
from time import sleep

steering = SteeringController()

steering.center()

steering.left()
sleep(1)

steering.right()
sleep(1)

steering.center()
