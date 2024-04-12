#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Route handler to display a list of states."""
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def teardown(exception):
    """Close the current SQLAlchemy Session after each request."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
