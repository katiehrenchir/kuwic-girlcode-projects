from gpiozero import Button
import os

class Key:
    def __init__(self, note_name=None, pin=None):
        # Self refers to the current object - our current key
        self.note_name = note_name
        self.note_file_name = note_name + ".mp3"
        
        self.pin = pin
        self.button = Button(pin)
        self.button.when_pressed = pressed

def pressed():
    print("I was pressed!")
    # Notice that every key is playing the same note right now
    os.system("omxplayer -o local notes/c.mp3 &")

# Remove the test button
# Notice the notes strings correspond to the file names of each note
notes = ["c", "c_sharp", "d", "d_sharp", "e", "f", "f_sharp", "g", "a", "b"]
button_pins = [26, 19, 13, 6, 5, 11, 9, 10, 22, 27]
# Create an empty list - we'll use this to store our keys (buttons)!
keys = []

for x in range(0,10):
    print(x)
    keys.append( Key(notes[x], button_pins[x]) )
    print(keys[x].note_name)

while True:
    # It actually doesn't matter what you put right here, so long as it keeps
    # the program running
    keys[0].button.wait_for_press()


