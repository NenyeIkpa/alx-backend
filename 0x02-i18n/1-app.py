#!/usr/bin/env python3

"""
  Basic Flask App - Configuraion with Babel
"""

from flask import Flask, render_template


class Config:
    """ holds app configurations """
    LANGUAGES = ['en', 'fr']
    
    
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index() -> str:
    """ prints text in html format """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
