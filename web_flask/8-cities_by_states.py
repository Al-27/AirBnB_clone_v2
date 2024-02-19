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


@app.route("/cities_by_states", strict_slashes=False)
def cities_route():
    from models.state import State
    states = storage.all(State).values()
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def req_tear(exception):
    storage.close()


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
