#!/usr/bin/python3
""" starts a Flask web application: """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """ index funtion """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """ hbnb funtion """
    return "HBNB"


@app.route('/c/<text>')
def c(text):
    """ c funtion """
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python')
@app.route('/python/<text>')
def python(text="is cool"):
    """ python funtion """
    text = text.replace('_', ' ')
    return f"Python {text}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
