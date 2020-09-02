#!/usr/bin/python3
"""Runs a Flask web application /hbnb"""
from flask import Flask, render_template


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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """number template in html

    Args:
        n ([int]): [Number]

    Returns:
        [type]: [template]
    """
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run()
