import cv2
import serial
from cvzone.HandTrackingModule import HandDetector

pythoncap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.5, maxHands=1)

# Initialize serial connection
bt = serial.Serial("COM6", 9600, timeout=1)

while True:
    ret, frame = pythoncap.read()  # Corrected variable name

    frame = cv2.flip(frame, 1)

    hands, frame = detector.findHands(frame)

    if not hands:
        print("No hands detected")

    else:
        hand1 = hands[0]
        fingers = detector.fingersUp(hand1)
        count = fingers.count(1)
        print(count)

        # Define command variable
        command = ''

        # Sending command based on finger count
        if count == 0:
            command = '0'  # Stop
        elif count == 1:
            command = '1'  # Forward
        elif count == 2:
            command = '2'  # Right
        elif count == 3:
            command = '3'  # Left
        elif count == 4:
            command = '4'  # Back

        bt.write(command.encode("utf-8"))

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

pythoncap.release()
cv2.destroyAllWindows()