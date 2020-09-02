#!/usr/bin/python3
"""Runs a Flask web application /hbnb"""
from flask import Flask


app = Flask(__name__)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hbnb(text="is cool"):
    """template
    Returns:
        [str]: [template]
    """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Numbers template

    Args:
        n ([int]): [Number]

    Returns:
        [int]: [int template]
    """
    return '{:d} is a number'.format(n)

if __name__ == '__main__':
    app.run()
