import RPi.GPIO as GPIO

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_freq, dyn_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_freq = pwm_freq
        self.dyn_range = dyn_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial = 0)

        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_freq)
        self.pwm.start(0.0)
    
    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dyn_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.0 - {self.dyn_range:.2f}) В")
            print("Устанавливаем 0.0 В")
            self.pwm.ChangeDutyCycle(0.0)
        print(f"Коэф. заполнения: {voltage / self.dyn_range:.2f}")
        self.pwm.ChangeDutyCycle(voltage / self.dyn_range * 100)

    def deinit(self):
        self.pwm.stop()
        GPIO.cleanup()

if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.290, True)
    
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)
            
            except ValueError:
                print("Вы ввели не число. Попробуйте еще раз\n")
    
    finally:
        dac.deinit()