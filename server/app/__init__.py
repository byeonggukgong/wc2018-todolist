# -*- coding: utf-8 -*-

from flask import Flask

from app import todo
from app.extensions import db, ma, cors


def create_app() -> Flask:
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/sqlite3.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    _register_extensions(app)
    _register_blueprints(app)

    return app


def _register_extensions(app) -> None:
    db.init_app(app)
    ma.init_app(app)
    cors.init_app(app)


def _register_blueprints(app) -> None:
    app.register_blueprint(todo.views.blueprint)
