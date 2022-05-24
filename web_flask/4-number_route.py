#!/usr/bin/python3
""" starts a Flask web application: """
from flask import Flask, abort

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
    return "C {}".format(text)


@app.route('/python')
@app.route('/python/<text>')
def python(text="is cool"):
    """ python funtion """
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<n>')
def number(n):
    """ number funtion """
    try:
        n_int = int(n)
        return "{} is a number".format(n)
    except Exception:
        abort(404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
