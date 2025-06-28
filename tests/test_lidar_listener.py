# tests/test_decision_logic.py
from control.motor_controller import MotorController
from control.steering_controller import SteeringController
import time
import random

motor = MotorController()
steering = SteeringController()

def simulate_lidar_decision():
    print("🔧 Teszt: Döntési logika szimuláció indul...")
    try:
        while True:
            # Szimulált távolságok (méterben)
            min_front = random.uniform(0.2, 1.5)
            min_left = random.uniform(0.2, 1.5)
            min_right = random.uniform(0.2, 1.5)
            min_back = random.uniform(0.2, 1.5)

            print(f"➡️  Front: {min_front:.2f} | Left: {min_left:.2f} | Right: {min_right:.2f} | Back: {min_back:.2f}")

            if min_front < 0.5:
                if min_left > 0.7:
                    print("↩️ TURN LEFT")
                    motor.forward()
                    steering.left()
                elif min_right > 0.7:
                    print("↪️ TURN RIGHT")
                    motor.forward()
                    steering.right()
                elif min_back > 0.5:
                    print("🔙 REVERSE")
                    motor.backward()
                else:
                    print("⛔ STOP")
                    motor.stop()
            else:
                print("⬆️ GO")
                motor.forward()
                steering.center()

            time.sleep(2)

    except KeyboardInterrupt:
        print("🛑 Teszt leállítva.")
        motor.stop()
        steering.center()

if __name__ == "__main__":
    simulate_lidar_decision()
