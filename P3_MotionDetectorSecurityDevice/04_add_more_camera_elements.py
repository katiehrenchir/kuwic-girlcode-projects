from gpiozero import MotionSensor
from picamera import PiCamera

pir = MotionSensor(4)
camera = PiCamera()
image_location = "/home/pi/Desktop/SecurityCamera/image.jpg"

while True:
    # Wait for an intruder
    pir.wait_for_motion()

    # Show camera preview while intruder is present
    camera.start_preview()
    print("Motion detected!")
    camera.capture(image_location)

    # Wait for the intruder to leave
    pir.wait_for_no_motion()
    camera.stop_preview()
    camera.close()

