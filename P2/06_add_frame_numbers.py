from picamera import PiCamera
from time import sleep
from gpiozero import Button

button = Button(17)
camera = PiCamera()
camera.rotation = 180
camera.resolution = (1280, 960)

camera.start_preview()

image_number = 1
while True:
    try:
        button.wait_for_press()
        
        # Be sure to put your images in their own folder!
        camera.capture('/home/pi/Desktop/StopMotionImages/Peach2/image%03d.jpg' % image_number)
        image_number += 1
        
    except KeyboardInterrupt:
        camera.stop_preview()
        break




