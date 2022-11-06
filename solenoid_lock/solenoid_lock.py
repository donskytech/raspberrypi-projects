import RPi.GPIO as GPIO
from time import sleep

RELAY_PIN = 23

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)

try:
    while (True):
        print("Turning on...")
        GPIO.output(RELAY_PIN, 1)
        sleep(1)
        print("Turning off...")
        GPIO.output(RELAY_PIN, 0)
        sleep(1)
finally:
    GPIO.cleanup()


