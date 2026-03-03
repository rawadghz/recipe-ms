"""
Database models and utilities for recipe management.
"""
import json
import sqlite3
import os
from contextlib import contextmanager
from datetime import datetime


class RecipeDatabase:
    """Database manager for recipes."""

    def __init__(self, db_path):
        self.db_path = db_path
        self._init_database()

    def _get_connection(self):
        """Create a database connection."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    @contextmanager
    def _connect(self):
        """Context manager for database connections."""
        conn = self._get_connection()
        try:
            yield conn
        finally:
            conn.close()

    def _init_database(self):
        """Initialize the database with schema."""
        schema_path = os.path.join(os.path.dirname(__file__), 'schema.sql')
        with open(schema_path, 'r') as f:
            schema = f.read()
        
        with self._connect() as conn:
            conn.executescript(schema)
            conn.commit()

    def get_all_recipes(self):
        """Retrieve all recipes."""
        with self._connect() as conn:
            cursor = conn.execute(
                'SELECT * FROM recipes ORDER BY created_at DESC'
            )
            return [dict(row) for row in cursor.fetchall()]

    def get_recipe_by_id(self, recipe_id):
        """Retrieve a single recipe by ID."""
        with self._connect() as conn:
            cursor = conn.execute(
                'SELECT * FROM recipes WHERE id = ?',
                (recipe_id,)
            )
            row = cursor.fetchone()
            return dict(row) if row else None

    def create_recipe(self, title, description, ingredients, instructions, 
                      cooking_time, difficulty, category=None, tag=None, rating=None):
        """Create a new recipe."""
        with self._connect() as conn:
            cursor = conn.execute(
                '''INSERT INTO recipes 
                   (title, description, ingredients, instructions, cooking_time, difficulty, category, tag, rating)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                (title, description, ingredients, instructions, cooking_time, difficulty, category, tag, rating)
            )
            conn.commit()
            return cursor.lastrowid

    def update_recipe(self, recipe_id, title, description, ingredients, 
                      instructions, cooking_time, difficulty, category=None, tag=None, rating=None):
        """Update an existing recipe."""
        with self._connect() as conn:
            conn.execute(
                '''UPDATE recipes 
                   SET title = ?, description = ?, ingredients = ?, 
                       instructions = ?, cooking_time = ?, difficulty = ?,
                       category = ?, tag = ?, rating = ?,
                       updated_at = CURRENT_TIMESTAMP
                   WHERE id = ?''',
                (title, description, ingredients, instructions, 
                 cooking_time, difficulty, category, tag, rating, recipe_id)
            )
            conn.commit()

    def delete_recipe(self, recipe_id):
        """Delete a recipe by ID."""
        with self._connect() as conn:
            conn.execute('DELETE FROM recipes WHERE id = ?', (recipe_id,))
            conn.commit()

    def search_recipes(self, query):
        """Search recipes by title or ingredients."""
        with self._connect() as conn:
            cursor = conn.execute(
                '''SELECT * FROM recipes 
                   WHERE title LIKE ? OR ingredients LIKE ?
                   ORDER BY created_at DESC''',
                (f'%{query}%', f'%{query}%')
            )
            return [dict(row) for row in cursor.fetchall()]

    def get_recipes_by_category(self, category):
        """Get all recipes in a specific category."""
        with self._connect() as conn:
            cursor = conn.execute(
                'SELECT * FROM recipes WHERE category = ? ORDER BY created_at DESC',
                (category,)
            )
            return [dict(row) for row in cursor.fetchall()]

    def get_all_categories(self):
        """Get all unique categories."""
        with self._connect() as conn:
            cursor = conn.execute(
                'SELECT DISTINCT category FROM recipes WHERE category IS NOT NULL AND category != "" ORDER BY category'
            )
            return [row['category'] for row in cursor.fetchall()]


def parse_ingredients(ingredients_text):
    """Parse ingredients from text to list."""
    if not ingredients_text:
        return []
    return [ing.strip() for ing in ingredients_text.split('\n') if ing.strip()]


def serialize_ingredients(ingredients_list):
    """Serialize ingredients list to text."""
    if isinstance(ingredients_list, list):
        return '\n'.join(ingredients_list)
    return ingredients_list
