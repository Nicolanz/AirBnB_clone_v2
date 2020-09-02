#!/usr/bin/python3
"""Runs a Flask web application /hbnb"""
from flask import Flask


app = Flask(__name__)


@app.route('/c/<text>', strict_slashes=False)
def hbnb(text):
    """template
    Returns:
        [str]: [template]
    """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)

if __name__ == '__main__':
    app.run()
