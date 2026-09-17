import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26

GPIO.setup(led, GPIO.OUT)

pwm = GPIO.PWM(led, 200)
duty = 0.0
pwm.start(duty)

while True:
    while duty < 100.0:
        pwm.ChangeDutyCycle(duty)
        time.sleep(0.04)
        duty += 1.0
    
    while duty > 0.0:
        pwm.ChangeDutyCycle(duty)
        time.sleep(0.04)
        duty -= 1.0