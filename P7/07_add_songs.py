from gpiozero import Button
from time import sleep
import os

class Key:
    # Notice - two underscores before and after 'init'
    def __init__(self, note_name=None, pin=None):
        # Self refers to the current object - our current key
        self.note_name = note_name
        self.note_file_name = note_name + ".mp3"
        
        self.pin = pin
        self.button = Button(pin)
        # Change 'pressed' to 'self.pressed'
        self.button.when_pressed = self.pressed
        
    # Move the pressed method inside the Key class
    # Select all of the method and press "tab" once
    # Add 'self' as a passed parameter to this method
    def pressed(self):
        # Change this system call to include each Key's note file name
        os.system("omxplayer -o local notes/" + self.note_file_name + " &")

# Notice the notes strings correspond to the file names of each note
# Since we have the files for any note, feel free to customize your keyboard
notes = ["c", "d", "e", "f", "g"]
button_pins = [26, 19, 13, 6, 5]
# Create an empty list - we'll use this to store our keys (buttons)!
keys = []

# If adding more keys, update the range
for x in range(0,5):
    # Comment out the print statements if you desire
    # print(x)
    keys.append( Key(notes[x], button_pins[x]) )
    # print(keys[x].note_name)

#--------------------------------
def mary_had_a_little_lamb():
    print("playing Mary Had a Little Lamb")
    # These values correspond to the position of the note in the array
    mary_lamb = [2,1,0,1,2,2,2,
                 1,1,1,2,4,4,
                 2,1,0,1,2,2,2,
                 2,1,1,2,1,0]
    
    for note in mary_lamb:
        keys[note].pressed()
        # Sleep determines the BPM
        sleep(.75)
        
def hot_cross_buns():
    print("playing Hot Cross Buns")
    # These values correspond to the position of the note in the array
    hot_cross_buns = [2,1,0,2,1,0,
                      0,0,0,0,1,1,1,1,
                      2,1,0]
    
    for note in hot_cross_buns:
        keys[note].pressed()
        # Sleep determines the BPM
        sleep(.5)
#--------------------------------

while True:
    # It actually doesn't matter what you put right here, so long as it keeps
    # the program running
    #keys[0].button.wait_for_press()
    hot_cross_buns()
    sleep(5)
    