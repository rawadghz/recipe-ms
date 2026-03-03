"""
Routes package - exports blueprints.
"""
from flask import Blueprint, render_template

# Main blueprint
main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """Home page with recipe overview."""
    return render_template('index.html')


# Import and re-export recipes blueprint
from routes.recipes import bp as recipes_bp

__all__ = ['main_bp', 'recipes_bp']
