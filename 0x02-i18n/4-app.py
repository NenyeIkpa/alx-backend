#!/usr/bin/env python3

"""
  Basic Flask - Detecting CL query for locale
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ holds app configurations """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str():
    """returns the best matched locale """
    queries = request.query_string.decode('utf-8').split('&')
    query_table = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='),
        queries,
    ))
    if 'locale' in query_table:
        if query_table['locale'] in app.config["LANGUAGES"]:
            return query_table['locale']
    return request.accept.languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """ prints text in html format """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
