#!/usr/bin/python3
""" starts a Flask web application: """
from flask import Flask, abort, render_template

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


@app.route('/number/<n>')
def number(n):
    """ number funtion """
    try:
        n_int = int(n)
        return f"{n} is a number"
    except Exception:
        abort(404)


@app.route('/number_odd_or_even/<n>')
def number_odd_or_even(n):
    """ number_odd_or_even funtion """
    try:
        n_int = int(n)
        if n_int % 2 == 0:
            m = 'even'
        else:
            m = 'odd'
        return render_template('6-number_odd_or_even.html', n=n, m=m)
    except Exception:
        abort(404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
