#!/usr/bin/python3
"""Starts a flask app
    listens to 0.0.0.0:5000
"""
from flask import Flask, render_template
from models.__init__ import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """display an HTML page with a list of all state in BDstorage.
    sorted by name
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """removes the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
