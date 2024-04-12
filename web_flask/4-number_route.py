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


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text="is cool"):
    """
    Route handler that returns 'Python' followed by the 'text'
    parameter with underscores replaced by spaces.
    The default value of text is 'is cool'
    """
    text_with_escape = text.replace('_', ' ')
    return f'Python {text_with_escape}'


@app.route("/number/<int:n>", strict_slashes=False)
def num(n):
    """
    Route handler that returns a message indicating whether 'n' is a number.
    """
    return f'{n} is a number'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
