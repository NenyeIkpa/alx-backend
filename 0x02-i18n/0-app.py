#!/usr/bin/env python3

"""
  Basic Flask App
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """ prints text in html format """
    return render_template('templates/index.html')
