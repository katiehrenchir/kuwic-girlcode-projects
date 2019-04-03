from gpiozero import Button

def pressed():
    print("I was pressed!")

# Our button is wired into GPIO 26
test_button = Button(26)
test_button.when_pressed = pressed

while True:
    test_button.wait_for_press()