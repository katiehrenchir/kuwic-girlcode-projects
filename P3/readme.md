# [Project 3 - Motion Activated Security Device][1] 
This project involves creating a “security” device to begin recording video when motion is detected. Girls will connect both a PIR motion sensor and a camera to their pi. The terminal will be used to learn the basics of these components. Then, the girls will write Python code to being capturing video when the PIR sensor detects motion, and write this video to memory.

Concepts:
* Circuit construction
  * PiCamera module
  * PIR Motion Sensor
* Python coding
  * PiCamera interaction
  * MotionSensor interaction
  * While loops
  * Writing video files to memory


Materials Needed:
* Raspberry pi camera module
* PIR Motion Sensor
* 3 Female-to-Female jumper wires

## Playing the Saved Video (h264)
To play a video in .h264 format, open a terminal in the directory containing your video and run the following command
```
omxplayer test_video.h264
```
Note that file name will depend on your implementation. Alternatively, double click your file in a file browser, select the "Custom Command Line" tab, and enter
```
omxplayer %f
```
into the "Command line to execute" field. 


## Circuit Diagram for Connecting PIR Sensor

![Image of Push Button Circuit](https://projects-static.raspberrypi.org/projects/rpi-gpio-connect-pir/f486753f7a342f6f379ea947b695541d5c793396/en/images/pir-diagram.png)


## Documentation Links
[MotionSensor][2] documentation from the GPIO Zero library.
[PiCamera][3] documentation from the PiCamera library.  


[1]:https://projects.raspberrypi.org/en/projects/parent-detector
[2]:https://gpiozero.readthedocs.io/en/stable/api_input.html#motion-sensor-d-sun-pir
[3]:https://picamera.readthedocs.io/en/release-1.13/