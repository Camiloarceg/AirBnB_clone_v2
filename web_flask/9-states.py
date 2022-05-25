#!/usr/bin/python3
""" starts a Flask web application: """
from flask import Flask, abort, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
@app.route('/states/<id>')
def cities_by_states(id=None):
    """ cities_by_states funtion """
    states = storage.all(State).values()
    if id:
        _id = id
        id_state = None
        for state in states:
            if state.id == _id:
                id_state = state
                break
    else:
        id_state = list(states)
    return (render_template('9-states.html', **locals()))


@app.teardown_appcontext
def teardown_appcontext(self):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
