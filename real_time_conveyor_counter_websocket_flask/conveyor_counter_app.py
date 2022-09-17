from flask import Flask, render_template, request
from flask_socketio import SocketIO
from random import random
from threading import Lock
from datetime import datetime
import RPi.GPIO as GPIO

sensor_pin = 23

# set the behaviour of led as output
is_load_detected = False
count = 0

"""
The callback will listen to
"""
def check_event(pin):
    global count
    if is_load_detected:
        print("Sending counter event...")
        count+=1
        socketio.emit('updateSensorData', {'value': count, "date": get_current_datetime()})

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)
GPIO.add_event_detect(sensor_pin, GPIO.FALLING, callback=check_event)


# Flask and Flask-SocketIO configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = 'donsky!'
socketio = SocketIO(app, cors_allowed_origins='*')

"""
Background Thread
"""
thread = None
thread_lock = Lock()

"""
Get current date time
"""
def get_current_datetime():
    now = datetime.now()
    return now.strftime("%m/%d/%Y %H:%M:%S")

"""
Generate random sequence of dummy sensor values and send it to our clients
"""
def background_thread():
    print("Generating random sensor values")
    global is_load_detected
    try:
        while True:
            if GPIO.input(sensor_pin):
                is_load_detected = False
            else:
                is_load_detected = True
    except KeyboardInterrupt:
        GPIO.cleanup()

"""
Serve root index file
"""
@app.route('/')
def index():
    return render_template('index.html')

"""
Decorator for connect
"""
@socketio.on('connect')
def connect():
    global thread
    print('Client connected')

    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)

"""
Decorator for disconnect
"""
@socketio.on('disconnect')
def disconnect():
    print('Client disconnected',  request.sid)

if __name__ == '__main__':
    # Access app in all IP not just localhost
    socketio.run(app, host="0.0.0.0")