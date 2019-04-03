from gpiozero import Button
from time import sleep
import os

class Key:
    def __init__(self, note_name=None, pin=None):
        self.note_name = note_name
        self.note_file_name = note_name + ".mp3"
        
        self.pin = pin
        self.button = Button(pin)
        self.button.when_pressed = self.pressed

    def pressed(self):
        print(self.note_name + " played")
        os.system("omxplayer -o local notes/" + self.note_file_name + " &")
        
notes = ["c", "c_sharp", "d", "d_sharp", "e", "f", "f_sharp", "g", "a", "b"]
button_pins = [26, 19, 13, 6, 5, 11, 9, 10, 22, 27]
keys = []

for x in range(0,10):
    keys.append( Key(notes[x], button_pins[x]) )

#--------------------------------
def welcome_to_the_black_parade():
    print("Playing Welcome to the Black Parade")
    black_parade = [7,6,9,4,2,7,0,9,4,8,2]
    
    for note in black_parade:
        keys[note].pressed()
        # Sleep determines the BPM
        sleep(1)

def mary_had_a_little_lamb():
    print("playing Mary Had a Little Lamb")
    mary_lamb = [4,2,0,2,4,4,4]
    
    for note in mary_lamb:
        keys[note].pressed()
        # Sleep determines the BPM
        sleep(.5)
#--------------------------------

while True:
    #keys[0].button.wait_for_press()
    mary_had_a_little_lamb()


