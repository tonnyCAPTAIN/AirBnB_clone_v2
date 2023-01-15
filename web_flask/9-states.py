#!/usr/bin/python3
"""Starts a flask app
    listens to 0.0.0.0:5000
"""
from flask import Flask, render_template
from models.__init__ import storage
from flask import Flask

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """display an HTML page with a list of all states in related cities.
    sorted by name
    """
    states = storage.all("State")
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("8-cities_by_states.html", state=states)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """removes the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
