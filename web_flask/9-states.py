#!/usr/bin/python3
"""this is a doc"""

from flask import Flask, render_template
from markupsafe import escape
from models import storage

app = Flask(__name__)
#app.jinja_env.lstrip_blocks = True
#app.jinja_env.trim_blocks = True

@app.route("/")
def hello_route():
    return "Hello HBNB!"

@app.route("/states",strict_slashes=False)
@app.route("/states/<id>",strict_slashes=False) 
def cities_route(id=None):
    from models.state import State
    states = storage.all(State)
    state = None
    if id is None:
        states = states.values()
    else: 
        id = f"State.{id}"
        if id in states.keys():
            state = states[id]
        states = None
            
    return render_template("9-states.html",states=states,state=state) 


@app.teardown_appcontext
def req_tear(exception):
    storage.close()

if __name__ == "__main__":
    app.run("0.0.0.0",5000)