"""
Main Flask application for recipe management.
"""
import os
from flask import Flask, render_template, request, redirect, url_for, flash
from config import config
from models import RecipeDatabase, parse_ingredients


def create_app(config_name=None):
    """Application factory."""
    if config_name is None:
        config_name = os.environ.get('FLASK_CONFIG', 'default')
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize database
    db_path = app.config.get('DATABASE_PATH', 'recipes.db')
    if not os.path.isabs(db_path):
        db_path = os.path.join(os.path.dirname(__file__), db_path)
    app.db = RecipeDatabase(db_path)
    
    # Register routes
    from routes import main_bp, recipes_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(recipes_bp)
    
    return app


# Create the application instance
app = create_app()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
