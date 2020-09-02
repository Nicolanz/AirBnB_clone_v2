#!/usr/bin/python3
"""Runs a Flask web application /hbnb"""
from flask import Flask


app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """template
    Returns:
        [str]: [template]
    """
    return 'HBNB'

if __name__ == '__main__':
    app.run()
