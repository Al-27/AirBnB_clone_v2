#!/usr/bin/python3
"""this is a doc"""

from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_route():
    return "Hello HBNB!"

@app.route("/hbnb")
def hbnb_route():
    return "HBNB!"

@app.route("/c",strict_slashes=False)
@app.route("/c/<text>",strict_slashes=False)
def c_route(text="is_cool"):
    return f'C {escape(text).replace("_"," ")}'
    
@app.route("/python",strict_slashes=False)
@app.route("/python/<text>",strict_slashes=False)
def python_route(text="is_cool"):
    return f'Python {escape(text).replace("_"," ")}'

@app.route("/number/<int:number>",strict_slashes=False)
def number_route(number=None):
    return render_template("5-number.html",number=number)
    
if __name__ == "__main__":
    app.run("0.0.0.0",5000)