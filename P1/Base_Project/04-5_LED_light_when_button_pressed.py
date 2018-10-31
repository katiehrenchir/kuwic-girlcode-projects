from gpiozero import LED, Button
from time import sleep
from random import uniform

# Declare LED at GPIO 4
led = LED(4)

# Declare buttons at GPIO 14 (top) and 15 (bottom)
top_button = Button(14)
bottom_button = Button(15)

# Main program
while True:
    top_button.wait_for_press()
    #on_duration = uniform(1,4)
    #print('on for {:f} seconds' .format(on_duration) )
    led.on()
    #sleep(on_duration)
    
    top_button.wait_for_release()
    #off_duration = uniform(.5,1)
    #print('off for {:f} seconds' .format(off_duration) )
    led.off()
    #sleep(off_duration)
    
