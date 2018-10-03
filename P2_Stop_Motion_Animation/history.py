from picamera import PiCamera

camera = PiCamera()
camera.rotation = 180

camera.start_preview()
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()
