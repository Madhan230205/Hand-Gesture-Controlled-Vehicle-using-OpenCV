# Hand-Gesture-Controlled-Vehicle-using-OpenCV
This Hand-Gesture-Controlled-Vehicle project enables users to drive an RC car using intuitive hand movements captured through a webcam and processed with OpenCV and MediaPipe for real-time gesture recognition.Detected gestures—such as open palm for “forward”, fist for “stop”, and directional cues for “left” or “right”—are translated into control signals and sent via serial communication to an Arduino (e.g., with an L293D motor driver) to operate the vehicle’s motors.Detected gestures—such as open palm for “forward”, fist for “stop”, and directional cues for “left” or “right”—are translated into control signals and sent via serial communication to an Arduino (e.g., with an L293D motor driver) to operate the vehicle’s motors.

# Tech Stack
1.Language: Python 3.7+
2.Computer Vision: OpenCV 4.x 
3.Hand Tracking: MediaPipe Hands 
4.Hardware Interface: PySerial for serial communication 
5.Microcontroller: Arduino Uno/Nano with L293D driver (or ESP32/HC-05 for wireless)

# Prerequisites
1.Python 3.7+ installed
2.opencv-python, mediapipe, and pyserial packages (pip install opencv-python mediapipe pyserial)
3.Arduino IDE with standard Serial and L293D examples
4.RC car chassis with DC motors and L293D motor driver shield
5.USB webcam (or Pi Camera on Raspberry Pi)

# Installation
1.Git clone
```
git clone https://github.com/Madhan230205/Hand-Gesture-Controlled-Vehicle-using-OpenCV.git
cd Hand-Gesture-Controlled-Vehicle-using-OpenCV
```
2.Install dependencies
```
pip install -r requirements.txt
```
3.Upload Arduino sketch
Open Arduino/control.ino and upload to your board via the Arduino IDE

# Usage
1.Launch Python Script
```
python gesture_vehicle.py --port COM3 --baud 9600
#Replace COM3 with your serial port (e.g., /dev/ttyUSB0 on Linux).
```

