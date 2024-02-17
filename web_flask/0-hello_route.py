#!/usr/bin/python3
"""
this is a doc
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_route():
    return "Hello HBNB!"
    
if __name__ == "__main__":
    app.run("0.0.0.0",5000)