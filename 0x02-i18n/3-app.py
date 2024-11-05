#!/usr/bin/env python3
"""This module instantiates babel"""
from flask import Flask, render_template, request
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

@babel.localeselector
def get_locale():
    """return a local langage"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def indeex():
    """route"""
    return render_template('3-index.html')

if __name__ == '__main__':
    app.run(debug=True)
