from flask import Blueprint
from .series import series_bp
from .actors import actors_bp
from .users import users_bp
def register_routes(app):
    app.register_blueprint(series_bp)
    app.register_blueprint(actors_bp)
    app.register_blueprint(users_bp)
