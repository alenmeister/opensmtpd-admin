"""Initialize application"""

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# Extension instances
bcrypt = Bcrypt()
db = SQLAlchemy()
login_manager = LoginManager()


def create_app() -> Flask:
    """Create a Flask application using the app factory pattern"""

    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialize plugins
    CORS(app)
    bcrypt.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        # pylint: disable=import-outside-toplevel

        # Register blueprints
        from . import auth, routes
        app.register_blueprint(auth.auth_blueprint)
        app.register_blueprint(routes.main_blueprint)

        # Register error handlers
        from . import errors
        app.register_error_handler(403, errors.forbidden)
        app.register_error_handler(404, errors.page_not_found)
        app.register_error_handler(500, errors.internal_server_error)

        return app
