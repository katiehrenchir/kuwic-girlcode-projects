from datetime import datetime
from gpiozero import MotionSensor
from picamera import PiCamera

pir = MotionSensor(4)
camera = PiCamera()
video_location = "/home/pi/Desktop/SecurityCamera/"

while True:
    video_filename = "{0:%Y}-{0:%m}-{0:%d}_{0:%X}".format(datetime.now()) + "intruder_video.h264"

    # Wait for an intruder
    pir.wait_for_motion()

    # Show camera preview while intruder is present
    camera.start_recording(video_location)
    print("Motion detected!")

    # Wait for the intruder to leave
    pir.wait_for_no_motion()
    camera.stop_recording()
    camera.close()

