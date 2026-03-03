"""
Recipe routes blueprint - CRUD operations for recipes.
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app

bp = Blueprint('recipes', __name__, url_prefix='/recipes')


@bp.route('/')
def list_recipes():
    """List all recipes, optionally filtered by category."""
    category = request.args.get('category', '').strip()
    categories = current_app.db.get_all_categories()
    
    if category:
        recipes = current_app.db.get_recipes_by_category(category)
    else:
        recipes = current_app.db.get_all_recipes()
    
    return render_template('recipe_list.html', recipes=recipes, current_category=category, categories=categories)


@bp.route('/<int:recipe_id>')
def recipe_detail(recipe_id):
    """View a single recipe."""
    recipe = current_app.db.get_recipe_by_id(recipe_id)
    if recipe is None:
        flash('Recipe not found', 'error')
        return redirect(url_for('recipes.list_recipes'))
    return render_template('recipe_detail.html', recipe=recipe)


@bp.route('/new', methods=['GET', 'POST'])
def create_recipe():
    """Create a new recipe."""
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        ingredients = request.form.get('ingredients', '').strip()
        instructions = request.form.get('instructions', '').strip()
        cooking_time = request.form.get('cooking_time', '')
        difficulty = request.form.get('difficulty', 'Medium')
        category = request.form.get('category', '').strip()
        tag = request.form.get('tag', '')
        rating = request.form.get('rating', '')
        
        # Validation
        errors = []
        if not title:
            errors.append('Title is required')
        if not ingredients:
            errors.append('Ingredients are required')
        if not instructions:
            errors.append('Instructions are required')
        
        if errors:
            for error in errors:
                flash(error, 'error')
            return render_template('recipe_form.html', 
                                   recipe=request.form,
                                   action='Create')
        
        # Create recipe
        recipe_id = current_app.db.create_recipe(
            title=title,
            description=description,
            ingredients=ingredients,
            instructions=instructions,
            cooking_time=int(cooking_time) if cooking_time else None,
            difficulty=difficulty,
            category=category if category else None,
            tag=tag if tag else None,
            rating=int(rating) if rating else None
        )
        
        flash('Recipe created successfully!', 'success')
        return redirect(url_for('recipes.recipe_detail', recipe_id=recipe_id))
    
    return render_template('recipe_form.html', action='Create')


@bp.route('/<int:recipe_id>/edit', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    """Edit an existing recipe."""
    recipe = current_app.db.get_recipe_by_id(recipe_id)
    
    if recipe is None:
        flash('Recipe not found', 'error')
        return redirect(url_for('recipes.list_recipes'))
    
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        ingredients = request.form.get('ingredients', '').strip()
        instructions = request.form.get('instructions', '').strip()
        cooking_time = request.form.get('cooking_time', '')
        difficulty = request.form.get('difficulty', 'Medium')
        category = request.form.get('category', '').strip()
        tag = request.form.get('tag', '')
        rating = request.form.get('rating', '')
        
        # Validation
        errors = []
        if not title:
            errors.append('Title is required')
        if not ingredients:
            errors.append('Ingredients are required')
        if not instructions:
            errors.append('Instructions are required')
        
        if errors:
            for error in errors:
                flash(error, 'error')
            return render_template('recipe_form.html',
                                   recipe=request.form,
                                   action='Edit')
        
        # Update recipe
        current_app.db.update_recipe(
            recipe_id=recipe_id,
            title=title,
            description=description,
            ingredients=ingredients,
            instructions=instructions,
            cooking_time=int(cooking_time) if cooking_time else None,
            difficulty=difficulty,
            category=category if category else None,
            tag=tag if tag else None,
            rating=int(rating) if rating else None
        )
        
        flash('Recipe updated successfully!', 'success')
        return redirect(url_for('recipes.recipe_detail', recipe_id=recipe_id))
    
    return render_template('recipe_form.html', recipe=recipe, action='Edit')


@bp.route('/<int:recipe_id>/delete', methods=['POST'])
def delete_recipe(recipe_id):
    """Delete a recipe."""
    recipe = current_app.db.get_recipe_by_id(recipe_id)
    
    if recipe is None:
        flash('Recipe not found', 'error')
        return redirect(url_for('recipes.list_recipes'))
    
    current_app.db.delete_recipe(recipe_id)
    flash('Recipe deleted successfully!', 'success')
    return redirect(url_for('recipes.list_recipes'))


@bp.route('/search')
def search_recipes():
    """Search recipes."""
    query = request.args.get('q', '').strip()
    
    if not query:
        return redirect(url_for('recipes.list_recipes'))
    
    recipes = current_app.db.search_recipes(query)
    return render_template('recipe_search.html', recipes=recipes, query=query)
