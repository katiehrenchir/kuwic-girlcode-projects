from gpiozero import Button
import os

def pressed():
    print("I was pressed!")
    # Change "local" to "hdmi" when running on the LEEP2 TVs
    os.system("omxplayer -o local notes/c.mp3 &")

# Our button is wired into GPIO 26
test_button = Button(26)
test_button.when_pressed = pressed

while True:
    test_button.wait_for_press()
