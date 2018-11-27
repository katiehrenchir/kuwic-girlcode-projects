# [Project 4 - Ultrasonic Theremin][1] 
This project involves creating a theremin (an instrument controlled by the position of the musician’s hands relative to a distance sensor). Girls will connect an ultrasonic distance sensor to a pi, then write some Python code to detect the distances around it. Next, girls will use Sonic Pi to emit noise. Finally the girls will use message passing (this is quite advanced!) to send pitch information (a function of the distance information) from their Python code to Sonic Pi.

Here's a very cool video of a theremin in action: https://www.youtube.com/watch?v=K6KbEnGnymk&feature=youtu.be&t=18

Concepts:
* Circuit construction
  * Ultrasonic distance sensor
  * Resistors and strength differences
* Python coding
  * Distance sensor libraries
  * Message passing: sending
* Ruby coding (Sonic Pi)
  * Live loops
  * Message passing: receiving


Materials Needed:
* Ultrasonic distance sensor
* 330 Ohm resistor
* 470 Ohm resistor
* 3+ Male-to-Male jumper wires
* 4+ Male-to-Female jumper wires

## Installing pythonosc
The message passing functions of the python script use a library called 'pythonosc'. To install this library, run the following command in a terminal window.
```
pip install python-osc
```
If you need to specify to install this library using python 3, run the same command using `pip3`



## Circuit Diagram for Connecting Ultrasonic Distance Sensor

![Image of Push Button Circuit](https://projects-static.raspberrypi.org/projects/ultrasonic-theremin/14dba599d11aabc6c6fe64208e12c2631bdea374/en/images/circuit.png)


## Documentation Links
[DistanceSensor][2] documentation from the GPIO Zero library.

[Sonic Pi][3] tutorial.  


[1]:https://projects.raspberrypi.org/en/projects/ultrasonic-theremin
[2]:https://gpiozero.readthedocs.io/en/stable/api_input.html#distance-sensor-hc-sr04
[3]:https://sonic-pi.net/tutorial.html
