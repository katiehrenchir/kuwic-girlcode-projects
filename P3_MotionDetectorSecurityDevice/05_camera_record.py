from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep

pir = MotionSensor(4)
camera = PiCamera()
camera.rotation = 180
camera.resolution = (400,400)

video_location = "/home/pi/Desktop/SecurityCamera/intruder_video.h264"

while True:
    # Wait for an intruder
    pir.wait_for_motion()

    # Show camera preview when motion detected
    camera.start_recording(video_location)
    print("Motion detected!")

    # Wait for the intruder to leave
    sleep(5)
    camera.stop_recording()

