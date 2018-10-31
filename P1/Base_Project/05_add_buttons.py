from gpiozero import LED, Button
from time import sleep
from random import uniform

# Declare LED at GPIO 4
led = LED(4)

# Declare buttons at GPIO 14 (top) and 15 (bottom)
top_button = Button(14)
bottom_button = Button(15)

# Method to print message when a button has been pressed
def pressed(button):
    print("Button has been pressed!")
    
# Define behavior when either the top or
# bottom buttons are pressed
top_button.when_pressed = pressed
bottom_button.when_pressed = pressed
    
# Main program
while True:
    on_duration = uniform(1,4)
    print('on for {:f} seconds' .format(on_duration) )
    led.on()
    sleep(on_duration)
    
    off_duration = uniform(.5,1)
    print('off for {:f} seconds' .format(off_duration) )
    led.off()
    sleep(off_duration)
    
