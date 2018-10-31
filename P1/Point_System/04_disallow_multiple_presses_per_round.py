from gpiozero import Button, LED
from random import uniform
from sys import exit
from time import sleep
from threading import Event

# Declare LED at GPIO 4
led = LED(4)

# Declare buttons at GPIO 14 (top) and 15 (bottom)
top_button = Button(14)
bottom_button = Button(15)

# Assign player names to buttons
top_name = raw_input('Name of player using top button: ')
bottom_name = raw_input('Name of player using bottom button: ')

# Method to determine which player has pressed her button
def get_name(button):
    if button.pin.number==14:
        return top_name
    else:
        return bottom_name
    
# Initialize points for each player (0)
top_points = 0
bottom_points = 0

# Initialize number of points needed to win
point_goal = 3

# Method to determine whether someone has enough points to
# win the game
def winner_found(points_needed):
    if top_points >= points_needed:
        return top_name
    elif bottom_points >= points_needed:
        return bottom_name
    else:
        False
        
# Method to assign 1 point to a player
def award_points(button):
    if button.pin.number==14:
        global top_points
        top_points = top_points + 1
    else:
        global bottom_points
        bottom_points = bottom_points + 1

# Method to remove 1 point from a player
def revoke_points(button):
    if button.pin.number==14:
        global top_points
        top_points = top_points - 1
    else:
        global bottom_points
        bottom_points = bottom_points - 1

# Method to print the current score of each player
def print_score():
    print("=============")
    print("SCORE BOARD: ")
    print(get_name(top_button) + ": " + str(top_points) )
    print(get_name(bottom_button) + ": " + str(bottom_points))
    print("=============")

# Method to print message when a button has been pressed
def pressed(button):
    round_over.set()
    if led.value:
        print(get_name(button) + ' won this round!')
        award_points(button)
        print_score()
    else:
        print('LED was not lit!')
        revoke_points(button)
        print_score()
    
# Define behavior when either the top or
# bottom buttons are pressed
top_button.when_pressed = pressed
bottom_button.when_pressed = pressed

# Event to determine whether or not the round is over
# Triggered by the pressed() method
round_over = Event()

# Main program
while not winner_found(point_goal):
    on_duration = uniform(.5,1)
    led.on()
    # Wait for the random on_duration or until
    # a player has won this round
    round_over.wait(on_duration)
    
    off_duration = uniform(5,10)
    led.off()
    sleep(off_duration)
    
    # Clear the round thread
    round_over.clear()
        
# End the game and print the final score
print("Game is over! Winner: " + winner_found(point_goal))
print_score()
exit()


