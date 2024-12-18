#!/usr/bin/env python3
"""This module instantiates babel"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """This class sets the LANGUAGES attribute
    to support EN and fr
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

@app.route('/')
def indeex():
    """route"""
    return render_template('1-index.html')

if __name__ == '__main__':
    app.run(debug=True)
