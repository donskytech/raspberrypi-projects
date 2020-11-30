from flask import Flask, render_template, jsonify, request
from gevent.pywsgi import WSGIServer
from ws2812b_neopixel_luma_led_matrix.neopixel_demo import show_effect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/change')
def change_effect():
    effect = request.args.get('effect', '')
    print("Received effect change request :: " + effect)
    show_effect(effect)
    return jsonify("success : true")


if __name__ == "__main__":        # on running python app.py
    # app.run(host='192.168.100.10', port='8080', debug='true', threaded='true')                     # run the flask app
    http_server = WSGIServer(('0.0.0.0', 8081), app)
    http_server.serve_forever()
