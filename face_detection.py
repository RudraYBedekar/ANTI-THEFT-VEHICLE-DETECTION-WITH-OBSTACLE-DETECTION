
import cv2
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
buzzer = 18
GPIO.setup(buzzer, GPIO.OUT)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def detect_face():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        if len(faces) == 0:
            GPIO.output(buzzer, True)
            print("Intruder Alert!")
            time.sleep(2)
            GPIO.output(buzzer, False)
        
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
        
        cv2.imshow('Face Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()

detect_face()
