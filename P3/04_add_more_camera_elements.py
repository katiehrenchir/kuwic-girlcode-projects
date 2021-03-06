from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep

pir = MotionSensor(4)
camera = PiCamera()
camera.rotation = 180
camera.resolution = (400,400)

image_location = "/home/pi/Desktop/SecurityCamera/image.jpg"

while True:
    # Wait for an intruder
    pir.wait_for_motion()

    # Show camera preview when motion detected
    camera.start_preview()
    print("Motion detected!")
    camera.capture(image_location)

    camera.stop_preview()

