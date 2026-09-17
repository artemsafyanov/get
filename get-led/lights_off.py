import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

leds = [26, 16, 12, 25, 17, 27, 23, 22, 24]


GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)
