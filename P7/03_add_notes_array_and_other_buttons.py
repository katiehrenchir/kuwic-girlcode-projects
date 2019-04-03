from gpiozero import Button
import os

def pressed():
    print("I was pressed!")
    # Change "local" to "hdmi" when running on the LEEP2 TVs
    os.system("omxplayer -o local notes/c.mp3 &")

# Our button is wired into GPIO 26
test_button = Button(26)
test_button.when_pressed = pressed

# Notice the notes strings correspond to the file names of each note
notes = ["c", "c_sharp", "d", "d_sharp", "e", "f", "f_sharp", "g", "a", "b"]
button_pins = [26, 19, 13, 6, 5, 11, 9, 10, 22, 27]
# Create an empty list - we'll use this to store our keys (buttons)!
keys = []

while True:
    test_button.wait_for_press()

