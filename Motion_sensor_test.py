from gpiozero import MotionSensor

pir = MotionSensor(14)

pir.wait_for_motion()
print("Motion detected")