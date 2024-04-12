#!/usr/bin/python3
"""
Script that start a simple Flask web application with two routes.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Route handler that returns 'Hello HBNB'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Route handler that returns 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    Route handler that returns 'C' followed by the 'text'
    parameter with underscores replaced by spaces
    """
    text_with_escape = text.replace('_', ' ')
    return f'C {text_with_escape}'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
