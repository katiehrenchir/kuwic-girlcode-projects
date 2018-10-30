from gpiozero import MotionSensor
from picamera import PiCamera

pir = MotionSensor(4)
camera = PiCamera()
image_location = "/home/pi/Desktop/SecurityCamera/image.jpg"

while True:
    pir.wait_for_motion()
    camera.start_preview()
    print("Motion detected!")
    camera.capture(image_location)
    camera.close()

