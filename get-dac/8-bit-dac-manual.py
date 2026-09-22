import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# gpio_r2r = [22, 27, 17, 26, 25, 21, 20, 16]
gpio_r2r = [16, 20, 21, 25, 26, 17, 27, 22]
GPIO.setup(gpio_r2r, GPIO.OUT)

dynamic_range = 3.2

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.0 - {dynamic_range:.2f} В")
        print("Устанавливаем 0.0 В")
        return 0
    number = int(voltage / dynamic_range * 255)
    print(number)
    return number

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def number_to_dac(number):
    b = dec2bin(number)
    GPIO.output(gpio_r2r, b)
    print(b)


try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)
        except ValueError:
            print("Вы ввели не число. Попробуйте еще раз\n")
finally:
    GPIO.output(gpio_r2r, 0)
    GPIO.cleanup()