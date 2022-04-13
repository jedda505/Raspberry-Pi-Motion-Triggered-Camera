# --Import Packages

import time
import asyncio
from picamera import PiCamera
from gpiozero import MotionSensor
from signal import pause
import random

# --Defining Motion Camera Class and Functions

camera = PiCamera()
pir = MotionSensor(4)

while True:
    pir.wait_for_motion()
    camera.start_preview()
    camera.start_recording('/home/pi/Desktop/video.h264')
    pir.wait_for_no_motion()
    camera.stop_preview()
    camera.stop_recording()

#     camera.start_recording('/home/pi/Desktop/video.h264')
#     time.sleep(10)
#     camera.stop_recording()

# asyncio.run(takevid())

# --Functions

# async def take_vid():
#     await pir.when_motion:
#         return camera.start_preview()
#         camera.start_recording('/home/pi/Desktop/video.h264')
#         time.sleep(20)
#         camera.stop_recording()

# -- Start recording

# pir.when_motion = camera
#
# camera.start_preview()
#
# camera.start_recording('/home/pi/Desktop/video.h264')
#
# time.sleep(10)
#
# camera.stop_recording()
#
# camera.stop_preview()
