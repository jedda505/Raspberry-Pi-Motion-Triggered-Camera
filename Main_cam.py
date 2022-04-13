import RPi.GPIO as GPIO
import time
import asyncio
from picamera import PiCamera
from gpiozero import MotionSensor
import random

# Definitions

IRSens = 14 #number of the pin connected to the sensor

Camera = PiCamera()


# GPIO setup


GPIO.setmode(GPIO.BCM) # naming convention links number to the pin
GPIO.setup(IRSens, GPIO.IN)


# Camera activate by IR motion sensor

try:
    print("Sensor Running - press CTRL + C to quit...")
    time.sleep(2)
    print("Ready")
    while True:
        if GPIO.input(IRSens):
            print("Motion Detected!")
            time.sleep(2)
            Camera.start_preview()
            Camera.stop_preview()
            Camera.start_recording('/home/pi/Desktop/t.h264')
            print("Recording Commenced...")
            time.sleep(15)
            Camera.stop_recording()
            print("Recording Complete!")
            time.sleep(0.5)
            
        time.sleep(0.1)
            
except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()


# while True:
#     while 1:
#         if GPIO.input(IRSens):
#             print("Recording")
#             Camera.start_recording('/home/pi/Desktop/t' + str(random.randint(0,100)) +'.h264')
#             time.sleep(20)
#         else:
#             print("No Motion")
#             time.sleep(5)
            

 