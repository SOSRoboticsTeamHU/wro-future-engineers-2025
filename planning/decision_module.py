# decision_module.py
def make_decision(camera_data, lidar_data):
    """
    camera_data: {
        'pole_color': 'red' / 'green' / None,
        'parking_detected': True / False
    }
    lidar_data: {
        'free_angle': float (0–360),
        'obstacle_ahead': True / False
    }
    """
    if camera_data['parking_detected']:
        return { 'speed': 0.0, 'steering': 0.0 }  # stop in parking zone

    if camera_data['pole_color'] == 'red':
        return { 'speed': 0.4, 'steering': 0.5 }  # steer right
    elif camera_data['pole_color'] == 'green':
        return { 'speed': 0.4, 'steering': -0.5 }  # steer left

    if lidar_data['obstacle_ahead']:
        angle = lidar_data['free_angle']
        steering = ((angle - 180) / 180)  # normalize to -1.0 to 1.0
        return { 'speed': 0.3, 'steering': steering }

    return { 'speed': 0.6, 'steering': 0.0 }  # go straight
