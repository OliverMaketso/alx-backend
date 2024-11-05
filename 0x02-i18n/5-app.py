#!/usr/bin/env python3
"""This module instantiates babel"""
from flask import Flask, render_template, request, g
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
app.url_map.strict_slashes = False

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """returns a dictionary or none if the ID
    cannot be found or if login_as was not passed"""
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request() -> None:
    """set the user in flask.g for the current request."""
    g.user = get_user()

@babel.localeselector
def get_locale():
    """return a local langage"""
    locale = request.args.get('locale', None)
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def indeex():
    """route"""
    return render_template('3-index.html')

if __name__ == '__main__':
    app.run(debug=True)
