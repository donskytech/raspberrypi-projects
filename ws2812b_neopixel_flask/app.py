from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":        # on running python app.py
    app.run(host='0.0.0.0', port='8080', debug='true') # run the flask app
