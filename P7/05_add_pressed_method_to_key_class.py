from gpiozero import Button
import os

class Key:
    def __init__(self, note_name=None, pin=None):
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
        print(self.note_name + " was pressed!")
        # Change local to hdmi to use on LEEP2 TVs
        os.system("omxplayer -o local notes/" + self.note_file_name + " &")
        
notes = ["c", "c_sharp", "d", "d_sharp", "e", "f", "f_sharp", "g", "a", "b"]
button_pins = [26, 19, 13, 6, 5, 11, 9, 10, 22, 27]
keys = []

for x in range(0,10):
    print(x)
    keys.append( Key(notes[x], button_pins[x]) )
    print(keys[x].note_name)

while True:
    # It actually doesn't matter what you put right here, so long as it keeps
    # the program running
    keys[0].button.wait_for_press()



