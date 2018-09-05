from gpiozero import LED
from time import sleep
from random import uniform

led = LED(4)

while True:
    led.on()
    sleep(uniform(1,4))
    
    led.off()
    sleep(uniform(1,4))
    from gpiozero import LED
from time import sleep
from random import uniform

led = LED(4)

while True:
    on_duration = uniform(1,4)
    print('on for {:f} seconds' .format(on_duration) )
    led.on()
    sleep(on_duration)
    
    off_duration = uniform(.5,1)
    print('off for {:f} seconds' .format(off_duration) )
    led.off()
    sleep(off_duration)
