import RPi.GPIO as GPIO
import time
import drivers
from pad4pi import rpi_gpio
import requests

#change this to the IP address of your REST API Server
API_SERVER = "192.168.100.22:3000" 

KEYPAD = [
    [1, 2, 3, "A"],
    [4, 5, 6, "B"],
    [7, 8, 9, "C"],
    ["*", 0, "#", "D"]
]

ROW_PINS = [17, 27, 22, 5] # BCM numbering
COL_PINS = [23, 24, 25, 16] # BCM numbering

# setup RPi
GPIO.setwarnings(False)    

#setup servo config
servo_pin = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin,GPIO.OUT)

# Initialize pwm pin to 20 ms Period or 50HZ frequency
pwm = GPIO.PWM(servo_pin,50) 
pwm.start(0)

display = drivers.Lcd()

# Constants
DEFAULT_INDENT = "     "
input_key_codes = DEFAULT_INDENT
DEFAULT_KEYCODE_LENGTH = 6

def open_lock():
    print("Opening lock...")
    pwm.ChangeDutyCycle(11) 
    time.sleep(5)
    print("Closing lock after 5 secs...")
    close_lock()
    pwm.ChangeDutyCycle(0)  # prevent servo from jittering when not receiving any signal

def close_lock():
    print("Closing lock...")
    pwm.ChangeDutyCycle(2) 
    time.sleep(1)

def cleanup():
    pwm.stop() 
    GPIO.cleanup()
    display.lcd_clear()
    print("Releasing resources and stopping our Program...")

def display_to_lcd(data, position = 2, show_input_keycode = False, duration = 1):
    display.lcd_clear()

    if show_input_keycode:
        display.lcd_display_string("Input Keycode:", 1)
        display.lcd_display_string(input_key_codes, 2)
        time.sleep(0.1)

    if data is not None:
        display.lcd_display_string(data, position)
    if duration is not None:
        time.sleep(duration)

def init_keypad_driver():
    factory = rpi_gpio.KeypadFactory()
    keypad = factory.create_keypad(keypad=KEYPAD,row_pins=ROW_PINS, col_pins=COL_PINS, key_delay=100) 

    keypad.registerKeyPressHandler(handle_keypad_press)

def handle_keypad_press(key):
    global input_key_codes 
   
    if key == '*':
        print("Clearing input..")
        input_key_codes = DEFAULT_INDENT
        display_to_lcd(None, None, show_input_keycode = True)
    elif key == '#':
        if len(input_key_codes.strip()) < DEFAULT_KEYCODE_LENGTH:
            display_to_lcd("Incomplete!!!", 2, show_input_keycode = False, duration=1)
            display_to_lcd(None, None, show_input_keycode = True)
            return


        print("Connecting to REST API Server..")
        display_to_lcd("Checking......", 2, show_input_keycode = False)
        with_error, is_present = validate_keycode(input_key_codes)

        # If with error then do nothing as this will be displayed in the LCD
        if with_error:
            return
            
        if is_present:
            display_to_lcd("Valid Keycode!", 2, show_input_keycode = False, duration=1)
            input_key_codes = DEFAULT_INDENT
            open_lock()
            display_to_lcd(None, None, show_input_keycode = True)
        else:
            display_to_lcd("Invalid Keycode!", 2, show_input_keycode = False, duration=1)
            input_key_codes = DEFAULT_INDENT
            display_to_lcd(None, None, show_input_keycode = True)
    else:
        if len(input_key_codes.strip()) == DEFAULT_KEYCODE_LENGTH:
            display_to_lcd("Exceed Limit!!!", 2, show_input_keycode = False, duration=1)
            display_to_lcd(None, None, show_input_keycode = True)
            return
        input_key_codes += str(key)
        print(f"input_key_codes:: {input_key_codes}")
        display_to_lcd(None, None, show_input_keycode = True, duration=0.2)


def validate_keycode(keycode):
    with_error = False
    request_url = f"http://{API_SERVER}/api/keycodes/{keycode.strip()}"
    print(f"Validate using REST API Server :: {request_url}")

    try:
        response = requests.get(request_url, timeout=5)
    except requests.exceptions.RequestException as e:
        print(f"Error encountered calling REST API Server :: {e}")
        display_to_lcd("Server Error!!!", 2, show_input_keycode = False)
        with_error = True
        return with_error, False
    
    json_response = response.json()

    return with_error, json_response['success']


def main():
    print("Starting our RPi Keypad Database Security System..")
    
    display_to_lcd("Initializing..", 1)

    init_keypad_driver()

    display_to_lcd(None, None, show_input_keycode = True)

    print("Press buttons on your keypad. Ctrl+C to exit.")

if __name__ == "__main__":
    try:
        main()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        cleanup()
    