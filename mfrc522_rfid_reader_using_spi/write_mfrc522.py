import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        text = input('Input badge number:')
        print("Place your RFID card near the reader...")
        reader.write(text)
        print(f'{text} written to RFID Card')
finally:
        GPIO.cleanup()
