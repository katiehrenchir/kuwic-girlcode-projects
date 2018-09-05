from gpiozero import RGBLED, Button
from time import sleep
from random import uniform, randint

# Declare RGBLED at GPIO 22, 17, and 27
# By default, the 'on' method of RGBLED will be a
# white light
led = RGBLED(red=22, green=17, blue=27)
red = [1.0, 0.0, 0.0]
green = [0.0, 0.0, 1.0]

# Declare buttons at GPIO 14 (top) and 15 (bottom)
top_button = Button(14)
bottom_button = Button(15)

# Assign player names to buttons
top_name = raw_input('Name of player using top button: ')
bottom_name = raw_input('Name of player using bottom button: ')

# Method to determine which player has pressed her button
def get_winner_name(button):
    if button.pin.number==14:
        return top_name
    else:
        return bottom_name

# Method to print message when a button has been pressed
# Determines color of LED and prints message accordingly
def pressed(button):
    if led.value==green:
        print(get_winner_name(button) + ' won the game!')
    elif led.value==red:
        print('LED was red!')
    else:
        print('Button was not pressed!')


# Method to randomize the color of the LED between green and red
def light_LED_random_color():
    random_number = randint(1,2)
    if random_number==1:
        # Light the LED green
        led.color = green
    else:
        # Light the LED red
        led.color = red
    
# Define behavior when either the top or
# bottom buttons are pressed
top_button.when_pressed = pressed
bottom_button.when_pressed = pressed
    
# Main program
while True:
    on_duration = uniform(.1,.3)
    light_LED_random_color()
    sleep(on_duration)
    
    off_duration = uniform(5,10)
    led.off()
    sleep(off_duration)
    


