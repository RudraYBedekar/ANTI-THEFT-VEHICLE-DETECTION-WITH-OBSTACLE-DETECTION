
# Anti-Theft Vehicle Detection with Obstacle Detection

This project aims to reduce vehicle theft using face recognition-based ignition. A Raspberry Pi system detects faces, authorizes users, and denies access to unrecognized individuals. In case of unauthorized access, the system activates a buzzer and sends an email notification with the intruder's image.

## Features
- Face recognition-based vehicle ignition
- GPS tracking and Wi-Fi alerts
- Email notification with intruder images
- Buzzer alarm for unauthorized access

## Hardware Requirements
- Raspberry Pi 3
- Camera Module
- DC Motor and L293D Motor Driver
- Regulator and Rectifier

## Software Requirements
- Python 3
- OpenCV
- Flask (optional for remote control)
- Raspberry Pi OS (NOOBS)

## Setup Instructions
1. Install Raspberry Pi OS using NOOBS.
2. Update the system and install dependencies:
    ```bash
    sudo apt-get update
    sudo apt-get install python3-opencv python3-pip
    pip3 install flask
    ```
3. Connect hardware components (camera, motor, etc.).
4. Run the face recognition code:
    ```bash
    python3 code/face_detection.py
    ```
5. The system activates a buzzer for unrecognized faces and grants access to authorized users.

## Future Scope
- Addition of infrared sensors to detect masked intruders.
- Integration of gas and fire sensors for enhanced vehicle safety.

## Team Members
- Prasad Raykar [20ET5501]
- Nikita Kandekar [20ET5502]
- Rudra Bedekar [20ET5503]
- Saail Choughule [20ET5506]

Guide: Mrs. Priya Mule
