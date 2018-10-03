from picamera import PiCamera
from time import sleep
from gpiozero import Button

button = Button(17)
camera = PiCamera()
camera.rotation = 180

camera.start_preview()

while True:
    try:
        button.wait_for_press()
        #sleep(5)
        camera.capture('/home/pi/Desktop/iamge.jpg')
    except KeyboardInterrupt:
        camera.stop_preview()
        break
