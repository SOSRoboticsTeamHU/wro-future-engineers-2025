# Usage Guide

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/wro-future-engineers-2025.git
cd wro-future-engineers-2025
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Connect hardware
- Ensure the Pi camera is connected.
- Connect the motor controller and servo (PCA9685 or GPIO).
- Plug in the YDLidar X4 via USB.

### 4. Run the system
```bash
python main.py
```

## Controls
- Autonomous drive starts automatically.
- Press `Ctrl+C` to stop safely.

## Troubleshooting
- No camera? Check ribbon connection and enable camera in `raspi-config`.
- LiDAR not spinning? Check power supply and USB device path.
