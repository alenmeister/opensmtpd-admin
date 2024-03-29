"""Initialize application"""

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap5
from flask_cors import CORS
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_minify import Minify

# Extension instances
bcrypt = Bcrypt()
db = SQLAlchemy()
login_manager = LoginManager()
bootstrap = Bootstrap5()


def create_app() -> Flask:
    """Create a Flask application using the app factory pattern"""

    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialize plugins
    CORS(app)
    Minify(app=app, html=True, js=True, cssless=True)
    bcrypt.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)

    with app.app_context():
        # pylint: disable=import-outside-toplevel
        from . import auth, routes
        from . import errors
        from .assets import compile_static_assets

        # Register blueprints
        app.register_blueprint(auth.auth_blueprint)
        app.register_blueprint(routes.main_blueprint)

        # Register error handlers
        app.register_error_handler(403, errors.forbidden)
        app.register_error_handler(404, errors.page_not_found)
        app.register_error_handler(500, errors.internal_server_error)

        # Compile static assets
        if app.config['ENVIRONMENT'] == 'development':
            compile_static_assets(app)

        return app
