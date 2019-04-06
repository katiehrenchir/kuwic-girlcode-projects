from gpiozero import Button
import os

# Probably wire in the rest of the buttons before starting this part

class Key:
    # Notice - two underscores before and after 'init'
    def __init__(self, note_name=None, pin=None):
        # Self refers to the current object - our current key
        self.note_name = note_name
        self.note_file_name = note_name + ".mp3"
        
        self.pin = pin
        self.button = Button(pin)
        self.button.when_pressed = pressed

def pressed():
    print("I was pressed!")
    # Change "local" to "hdmi" when running on the LEEP2 TVs
    os.system("omxplayer -o local notes/c.mp3 &")

# Our button is wired into GPIO 26
test_button = Button(26)
test_button.when_pressed = pressed

while True:
    test_button.wait_for_press()

