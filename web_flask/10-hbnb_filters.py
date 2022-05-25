#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
from models.amenity import Amenity
from models.state import State
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/hbnb_filters")
def hbnb_filters():
    """ Display a HTML page like 6-index.html """
    states = list(storage.all(State).values())
    amenities = list(storage.all(Amenity).values())
    states.sort(key=lambda x: x.name)
    amenities.sort(key=lambda x: x.name)
    return render_template(
        "10-hbnb_filters.html", states=states, amenities=amenities)


@app.teardown_appcontext
def teardown_db(self):
    """ Remove the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
