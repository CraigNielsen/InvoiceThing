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

    from backend.api.users import bp
    app.register_blueprint(bp, url_prefix='/api')

    from backend.api.users.user import bp_user
    app.register_blueprint(bp_user, url_prefix='/api/users')
    
    db.init_app(app)

    return app
