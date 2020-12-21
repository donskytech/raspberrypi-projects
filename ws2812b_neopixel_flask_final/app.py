from flask import Flask, render_template, jsonify, request
import subprocess
import time

app = Flask(__name__)
process = None


def show_effect(effect):
    global process
    process = subprocess.Popen(["python3", "neopixel_main_demo.py", effect])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/change')
def change_effect():
    global process
    effect = request.args.get('effect', '')

    if process is not None:
        process.kill()
        while not process.poll():
            time.sleep(0.1)
        del process

    show_effect(effect)

    return jsonify("success : true")


if __name__ == "__main__":        # on running python app.py
    app.run(host='0.0.0.0', port='8080', debug='true')  # run the flask app


