from planning.decision_module import make_decision

# Teszt 1: piros oszlop
cam_data = {'pole_color': 'red', 'parking_detected': False}
lidar_data = {'free_angle': 180, 'obstacle_ahead': False}

print(make_decision(cam_data, lidar_data))  # → jobbra fordulás

# Teszt 2: parkoló
cam_data = {'pole_color': None, 'parking_detected': True}
print(make_decision(cam_data, lidar_data))  # → megállás
