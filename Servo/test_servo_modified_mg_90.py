# Title:  SG90 Servo Driver Code - RPi.GPIO
# Author: donskytech

import RPi.GPIO as GPIO
import time


# setup RPi
GPIO.setwarnings(False)
servo_pin = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin,GPIO.OUT)

# 50 Hz or 20 ms PWM period
pwm = GPIO.PWM(servo_pin,50) 

print("Starting at zero...")
pwm.start(2) 

try:
    while True:
        print("Setting to zero...")
        pwm.ChangeDutyCycle(2) 
        time.sleep(1)

        print("Setting to 180...")
        pwm.ChangeDutyCycle(11) 
        time.sleep(1)

        print("Setting to 90...")
        pwm.ChangeDutyCycle(6.5) 
        time.sleep(1)
except KeyboardInterrupt:
    pwm.stop() 
    GPIO.cleanup()
    print("Program stopped")


