from gpiozero import LED, Button
from time import sleep
from random import uniform

# Declare LED at GPIO 4
led = LED(4)

# Declare buttons at GPIO 14 (top) and 15 (bottom)
top_button = Button(14)
bottom_button = Button(15)

# Assign player names to buttons
# raw_input denotes a str 
top_name = raw_input('Name of player using top button: ')
bottom_name = raw_input('Name of player using bottom button: ')

# Take in the count length for the coundown
countdown_length = input('Countdown length: ')

# Method to determine which player has pressed her button
def get_winner_name(button):
    if button.pin.number==14:
        return top_name
    else:
        return bottom_name

# Method to print message when a button has been pressed
def pressed(button):
    if led.value:
        print(get_winner_name(button) + ' won the game!')
    else:
        print('Button was not pressed!')
    
# Define behavior when either the top or
# bottom buttons are pressed
top_button.when_pressed = pressed
bottom_button.when_pressed = pressed
    
# Method to print countdown before start of game
# Counts down from 3 with 1 second pause inbetween prints
def countdown(seconds):
    print('Game starting in... ' + str(seconds))
    for num in reversed(range (1,seconds)):
        print(num)
        sleep(1)
    print('GO!')
    sleep(1) 
    
#Print the countdown before we start the game
countdown(countdown_length)
    
# Main program
while True:
    on_duration = uniform(.1,.3)
    led.on()
    sleep(on_duration)
    
    off_duration = uniform(5,10)
    led.off()
    sleep(off_duration)
