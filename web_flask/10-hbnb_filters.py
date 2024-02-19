#!/usr/bin/python3
"""this is a doc"""

from flask import Flask, render_template
from markupsafe import escape
from models import storage

app = Flask(__name__)
# app.jinja_env.lstrip_blocks = True
# app.jinja_env.trim_blocks = True


@app.route("/")
def hello_route():
    return "Hello HBNB!"


@app.route("/hbnb_filters", strict_slashes=False)
def cities_route():
    from models.state import State
    from models.amenity import Amenity
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template(
        "10-hbnb_filters.html",
        states=states,
        amenities=amenities)


@app.teardown_appcontext
def req_tear(exception):
    storage.close()


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
