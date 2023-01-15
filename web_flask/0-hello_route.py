#!/usr/bin/python3
"""Start fals web app
Listening on port loacalhost:5000
Route displays "Hello HBNB
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Displays 'Hello HBNB!"""
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
