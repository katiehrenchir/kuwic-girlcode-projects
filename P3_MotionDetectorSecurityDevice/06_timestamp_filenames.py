from datetime import datetime
from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep

pir = MotionSensor(4)
camera = PiCamera()
camera.rotation = 180

video_filepath = "/home/pi/Desktop/SecurityCamera/"

while True:
    # Name the video file with time information
    # This way, the videos will be ordered by date in our folder
    current_time = "{0:%Y}-{0:%m}-{0:%d}_{0:%X}".format(datetime.now()) 
    video_filename = video_filepath + current_time + "_intruder_video.h264"

    # Wait for an intruder
    pir.wait_for_motion()

    # Show camera preview when motion detected
    camera.start_recording(video_filename)
    print("Motion detected!")

    # Wait for the intruder to leave
    sleep(5)
    camera.stop_recording()

