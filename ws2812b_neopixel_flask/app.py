from flask import Flask, render_template, jsonify
from gevent.pywsgi import WSGIServer

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":        # on running python app.py
    # app.run(host='192.168.100.10', port='8080', debug='true', threaded='true')                     # run the flask app
    http_server = WSGIServer(('0.0.0.0', 8081), app)
    http_server.serve_forever()
