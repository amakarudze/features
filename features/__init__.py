""" Application factory for our features app. """

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app(test_config=None):
    # create the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='development',
        SQLALCHEMY_DATABASE_URI='sqlite:////tmp/features.db',
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )
    db = SQLAlchemy()
    db.init_app(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # log the test config if passed in
        app.config.from_mapping(test_config)

    # ensure that instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says "Features Requests App"
    @app.route('/hello')
    def hello():
        return 'Feature Requests App'

    # Register views blueprint to provide routes for features app
    from . import views
    app.register_blueprint(views.bp)
    app.add_url_rule('/', endpoint='index')

    return app