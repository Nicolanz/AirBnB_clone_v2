#!/usr/bin/python3
"""Runs a  Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """template
    Returns:
        [str]: [template]
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run()
