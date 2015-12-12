from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('config/default.py')

    @app.route('/')
    def index():
        return "Hello World"

    db.init_app(app)

    return app
