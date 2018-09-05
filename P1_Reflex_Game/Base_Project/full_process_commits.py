from gpiozero import LED
from time import sleep
from random import uniform

led = LED(4)

while True:
    led.on()
    sleep(uniform(1,4))
    
    led.off()
    sleep(uniform(1,4))