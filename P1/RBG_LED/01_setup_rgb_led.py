from gpiozero import RGBLED, Button
from time import sleep

button = Button(2)

led = RGBLED(red=22, green=17, blue=27)


def pressed():
    print("button was pressed")
    
    
button.when_pressed = pressed


# Color the LED red
led.color=(1,0,0)
sleep(1)

# Color the LED green
led.color = (0,1,0)
sleep(1)

# Color the LED blue
led.color = (0,0,1)
sleep(1)

# Color the LED purple
led.color = (1,0,1)
sleep(1)

# Color the LED orange
led.color = (1, .5, 0)
sleep(1)