import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [24, 22, 23, 27, 17, 25, 12, 16]
button1 = 9
button2 = 10


led_status = [0, 0, 0, 0, 0, 0, 0, 0]

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(button1, GPIO.IN)

led_target = 0

while True:
    if led_target < 0:
        led_target = 0
    elif led_target > 7:
        led_target = 7
    if (GPIO.input(button1)):
        led_status[led_target] = 1
        led_target += 1
    else:
        led_status[led_target] = 0
        led_target -= 1
    GPIO.output(leds, led_status)
    time.sleep(0.05)
