# pid_controller.py
def pid_control(error, prev_error, integral, dt, kp=0.6, ki=0.0, kd=0.2):
    integral += error * dt
    derivative = (error - prev_error) / dt if dt > 0 else 0
    output = kp * error + ki * integral + kd * derivative
    return output, integral
