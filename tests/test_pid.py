from control.pid_controller import pid_control

error = 0.5
prev_error = 0.3
integral = 0.0
dt = 0.1

output, new_integral = pid_control(error, prev_error, integral, dt)
print("Steering output:", output)
