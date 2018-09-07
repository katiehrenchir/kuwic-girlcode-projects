from gpiozero import LED

led = LED(4)

while True:
    led.on()
