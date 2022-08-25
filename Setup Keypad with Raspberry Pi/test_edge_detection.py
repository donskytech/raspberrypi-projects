import RPi.GPIO as GPIO
import time

def event_callback(pin):
    value = GPIO.input(pin)
    print(f"pin :: {pin}, value is {value}")

if __name__ == '__main__':
    button_pin = 23
    row_pin = 17

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(row_pin, GPIO.OUT)
    GPIO.setup(button_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

    GPIO.output(row_pin, GPIO.LOW)

    # events can be GPIO.RISING, GPIO.FALLING, or GPIO.BOTH
    GPIO.add_event_detect(button_pin, GPIO.BOTH,
                          callback=event_callback,
                          bouncetime=300)

    try:
        time.sleep(1000)
    except KeyboardInterrupt:
        GPIO.cleanup()