#!/usr/bin/env python3
"""a simple flask app with one route"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """route"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
