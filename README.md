WRO 2025 Future Engineers Robot Project 🚗🤖
============================================

Overview
--------

This repository contains the software and documentation for an autonomous robot developed for the WRO 2025 Future Engineers competition. The robot utilizes a YDLiDAR X4 for 360° obstacle avoidance and a HuskyLens for advanced color detection, all integrated into an RC car body with custom 3D-printed parts.

Key Features
------------

*   **360° LiDAR-based Obstacle Avoidance:**
    
    *   YDLiDAR X4 sensor
        
    *   ROS 2 Jazzy distribution for reliable, real-time operation
        
*   **Advanced Color Detection:**
    
    *   HuskyLens for rapid color recognition
        
    *   Effective decision-making based on color inputs
        
*   **Motor and Servo Control:**
    
    *   GPIO-based motor control for forward/reverse movement
        
    *   Servo-based precision steering control
        
*   **Mechanical Design:**
    
    *   Custom RC car chassis integration
        
    *   3D-printed mounts and brackets
        
*   **Autonomous Startup:**
    
    *   Automated system startup via systemd on Raspberry Pi
        

Repository Structure
--------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   wro_robot/  ├── control/  │   ├── decision_logic.py  │   ├── motor_controller.py  │   ├── steering_controller.py  │   └── huskylens_module.py  ├── scripts/  │   └── start_robot.sh  ├── system/  │   ├── wro_robot.service  │   └── ydlidar.service  ├── ROS/  │   └── YDLIDAR_ws/  │       └── src/  │           └── lidar_driver/  ├── models/                    # 3D printable STL files  ├── docs/  │   ├── setup_guide.md  │   └── troubleshooting.md  ├── LICENSE  └── README.md   `

Getting Started
---------------

### Hardware Requirements

*   Raspberry Pi 5 with Ubuntu 24.04 LTS
    
*   YDLiDAR X4
    
*   HuskyLens sensor
    
*   RC car chassis
    
*   3D-printed mounting parts (see models/)
    
*   Servo motor for steering
    
*   GPIO Motor controller
    

### Software Installation

1.  git clone
    
2.  sudo apt updatesudo apt install ros-jazzy-desktop python3-gpiozero python3-opencvpip install -r requirements.txt
    
3.  cd ROS/YDLIDAR\_wscolcon build
    
4.  sudo cp system/\*.service /etc/systemd/system/sudo systemctl enable wro\_robot.service ydlidar.service
    
5.  sudo reboot
    

Documentation
-------------

*   [Setup Guide](docs/setup_guide.md)
    
*   [Troubleshooting Guide](docs/troubleshooting.md)
    

Contribution
------------

Contributions are welcome! Fork the repository and submit pull requests with enhancements or fixes.

License
-------

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Authors
-------

*   [Zsombor Kukucska](https://github.com/SOSRoboticsTeamHU)