from picamera import PiCamera

camera = PiCamera()

camera.start_preview()
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()