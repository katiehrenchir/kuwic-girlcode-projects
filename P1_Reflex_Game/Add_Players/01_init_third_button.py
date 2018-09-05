from gpiozero import LED, Button
from time import sleep
from random import uniform

# Declare LED at GPIO 4
led = LED(4)

# Declare buttons at GPIO 14 (top), 18 (middle), and 15 (bottom)
top_button = Button(14)
middle_button = Button(18)
bottom_button = Button(15)

# Assign player names to buttons
top_name = raw_input('Name of player using top button: ')
middle_name = raw_input('Name of player using middle button: ')
bottom_name = raw_input('Name of player using bottom button: ')

# Method to determine which player has pressed her button
def get_winner_name(button):
    if button.pin.number==14:
        return top_name
    elif button.pin.number==18:
        return middle_name
    else:
        return bottom_name

# Method to print message when a button has been pressed
def pressed(button):
    if led.value:
        print(get_winner_name(button) + ' won the game!')
    else:
        print('Button was not pressed!')
    
# Define behavior when either the top, bottom,
#  or middle buttons are pressed
top_button.when_pressed = pressed
middle_button.when_pressed = pressed
bottom_button.when_pressed = pressed
    
# Main program
while True:
    on_duration = uniform(4,5)
    led.on()
    sleep(on_duration)
    
    off_duration = uniform(5,10)
    led.off()
    sleep(off_duration)
    
