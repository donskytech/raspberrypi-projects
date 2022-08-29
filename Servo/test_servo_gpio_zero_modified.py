# Title:  SG90 Servo Driver Code - GPIOZero
# Author: donskytech

from gpiozero import Servo
from time import sleep

servo = Servo(12, min_pulse_width=0.0006, max_pulse_width=0.0026)

try:
    while True:
        print("Setting to min...")
        servo.min()
        sleep(1)

        print("Setting to mid...")
        servo.mid()
        sleep(1)

        print("Setting to max...")
        servo.max()
        sleep(1)
except KeyboardInterrupt:
	print("Exiting program")