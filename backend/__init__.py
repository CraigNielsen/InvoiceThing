from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.cors import CORS

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config.from_pyfile('config/default.py')

    @app.route('/')
    def index():
        return "Hello World"

    from backend.api.v1 import v1_bp
    app.register_blueprint(v1_bp, url_prefix='/api/v1')

    db.init_app(app)

    return app
