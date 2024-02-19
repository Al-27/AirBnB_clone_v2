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


@app.route("/states_list", strict_slashes=False)
def states_route():
    from models.state import State
    states = storage.all(State)
    return render_template("7-states_list.html", states=states.values())


@app.teardown_appcontext
def req_tear(exception):
    storage.close()


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
