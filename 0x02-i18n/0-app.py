#!/usr/bin/env python3
"""This script setup a basic Flask app"""


from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """return the index page"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run("127.0.0.1", "8000")
