import RPi.GPIO as GPIO
import time

# Set the Row Pins
ROW_1 = 17
ROW_2 = 27
ROW_3 = 22
ROW_4 = 5

# Set the Column Pins
COL_1 = 23
COL_2 = 24
COL_3 = 25
COL_4 = 16

GPIO.setwarnings(False)
# BCM numbering
GPIO.setmode(GPIO.BCM)

# Set Row pins as output
GPIO.setup(ROW_1, GPIO.OUT)
GPIO.setup(ROW_2, GPIO.OUT)
GPIO.setup(ROW_3, GPIO.OUT)
GPIO.setup(ROW_4, GPIO.OUT)

# Set column pins as input and Pulled up high by default
GPIO.setup(COL_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(COL_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(COL_3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(COL_4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# function to read each row and each column
def readRow(line, characters):
    GPIO.output(line, GPIO.LOW)
    if(GPIO.input(COL_1) == GPIO.LOW):
        print(f"Using Polling, Input Received ::  {characters[0]}")
    if(GPIO.input(COL_2) == GPIO.LOW):
        print(f"Using Polling, Input Received ::  {characters[1]}")
    if(GPIO.input(COL_3) == GPIO.LOW):
        print(f"Using Polling, Input Received ::  {characters[2]}")
    if(GPIO.input(COL_4) == GPIO.LOW):
        print(f"Using Polling, Input Received ::  {characters[3]}")
    GPIO.output(line, GPIO.HIGH)

# Endless loop by checking each row 
try:
    print("Press buttons on your keypad. Ctrl+C to exit.")
    while True:
        readRow(ROW_1, ["1","2","3","A"])
        readRow(ROW_2, ["4","5","6","B"])
        readRow(ROW_3, ["7","8","9","C"])
        readRow(ROW_4, ["*","0","#","D"])
        time.sleep(0.2) # adjust this per your own setup
except KeyboardInterrupt:
    print("\nKeypad Application Interrupted!")
    GPIO.cleanup()