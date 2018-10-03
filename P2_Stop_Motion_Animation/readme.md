# [Project 2 - Stop Motion Animation][1] 
This project involves creating stop-motion animation videos using still frames captured when a button is pushed. Girls will connect a camera to their pi and then use the terminal to learn the basic ways to interact with it. Then, girls will write Python code to take photos when buttons are pressed and save them to memory with unique file names using while loops and counters. Finally, girls will use the command line to compile their still frames into a video.  

Concepts:
* Circuit construction
  * PiCamera module
  * Tactile button
* Terminal Commands
  * Interact with raspistill via the terminal
  * Compile still images into video
* Python coding
  * PiCamera interaction
  * GPIO button integration
  * Try/Except exception catching
  * While loops


Materials Needed:
* Raspberry pi camera module
* 1 tactile push button
* 2 Male-to-Female jumper wires

## Checking your raspberry pi camera's functionality
To test the preview function of your camera, run the following command. It is alright if your image is upside-down, we can correct this later with our code. 
```
raspistill -k
```
If this command does not work, ensure that your camera module is enabled. Run the following command and check to see if the 'camera' section is enabled. Ask an instructor for help if you get stumped!
```
sudo raspi-config
```


## Compiling the images into a .gif
To compile a collection of still images into a .gif file, use the following command:
```
ffmpeg -framerate 5 -f image2 StopMotionImages/image%03d.jpg stop_motion.gif
```
Note that filepath and image file names will depend on your implementation. The framerate can also be altered, in this example it is 5.


## Circuit Diagram for Base Project


![Image of Push Button Circuit](https://projects-static.raspberrypi.org/projects/push-button-stop-motion/12c581bd3c4f76e1b2351e787e8e0af595494f53/en/images/picamera-gpio-setup.png)

[1]:https://projects.raspberrypi.org/en/projects/push-button-stop-motion
