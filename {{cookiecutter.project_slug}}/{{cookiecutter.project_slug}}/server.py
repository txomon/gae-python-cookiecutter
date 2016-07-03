from __future__ import absolute_import, unicode_literals

import logging

import flask

from {{cookiecutter.project_slug}}.handlers import error_404, error_405, error_500, root_get
from {{cookiecutter.project_slug}}.restutils import Return, return_error

logger = logging.getLogger()

_app = None


def setup_logging(app):
    logging.basicConfig(level=logging.INFO)


def get_app():
    global _app
    if _app is not None:
        return _app

    app = flask.Flask(__name__)
    app.config['SECRET_KEY'] = '' # Put something here!
    setup_logging(app)

    app.register_error_handler(404, error_404)
    app.register_error_handler(405, error_405)
    app.register_error_handler(500, error_500)
    app.register_error_handler(Return, return_error)

    app.add_url_rule('/', None, root_get)
    app.add_url_rule('/{{cookiecutter.project_slug}}/', None, root_get)
    app.add_url_rule('/{{cookiecutter.project_slug}}/v{{cookiecutter.project_slug.split(".")[0]}}/', None, root_get)

    _app = app
    return _app


def wsgi(*args, **kwargs):
    app = get_app()
    return app(*args, **kwargs)
