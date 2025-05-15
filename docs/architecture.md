# System Architecture – WRO 2025 Autonomous Car

## Overview
This document describes the modular system architecture of the self-driving robot built for the WRO 2025 Future Engineers category.

## Modules

### 1. Camera Module
- Captures video using a Pi camera.
- Processes lane detection and colored object recognition (e.g., obstacle indicators, parking zone).

### 2. LiDAR Module
- Reads distance data from a YDLidar X4.
- Performs obstacle detection and path clearance analysis.

### 3. Control Module
- Contains PID controller logic for steering.
- Handles motor PWM and steering servo control.

### 4. Planning Module
- Makes decisions about direction based on sensor input.
- Integrates rules (e.g., passing colored poles on correct side).

### 5. Utility Module
- Logging, config, and shared utilities.

## Data Flow
Camera + LiDAR → Perception → Decision → Motor & Steering → Movement
