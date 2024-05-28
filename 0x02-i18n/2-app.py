#!/usr/bin/env python3
"""This script setup a basic Flask app with a babel object"""


from flask import Flask, render_template
from flask_babel import Babel


class Config():
    """Used to configure languages """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """determine the best match with our supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """return the index page"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run("127.0.0.1", "8000")
