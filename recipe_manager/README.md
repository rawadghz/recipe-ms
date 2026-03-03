# Recipe Manager

A web-based recipe management system built with Flask, SQLite, and Jinja2 templates.

## Tech Stack

- **Backend**: Flask (Python web framework)
- **Database**: SQLite (built-in Python)
- **Templates**: Jinja2
- **Styling**: Custom CSS
- **Package Manager**: Poetry

## Prerequisites

- Python 3.9 or higher
- Poetry (for dependency management)

## Installation

### 1. Install Poetry

If you don't have Poetry installed, follow the instructions at [https://python-poetry.org/docs/#installation](https://python-poetry.org/docs/#installation)

Or on macOS/Linux:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Or on Windows:
```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

### 2. Install Dependencies

Navigate to the project directory and install dependencies:

```bash
cd recipe_manager
poetry install
```

This will:
- Create a virtual environment
- Install Flask and Jinja2
- Install development dependencies (pytest)

## Usage

### Running the Application

Activate the virtual environment and run:

```bash
poetry run python app.py
```

Or without activating:

```bash
poetry run python app.py
```

The application will start at `http://localhost:5000`

### Development Mode

The app runs in debug mode by default. Any changes to the code will automatically reload the server.

## Project Structure

```
recipe_manager/
├── app.py              # Main Flask application
├── config.py           # Configuration settings
├── models.py           # Database models and utilities
├── schema.sql          # Database schema
├── pyproject.toml      # Poetry configuration
├── routes/
│   ├── __init__.py    # Main blueprint
│   └── recipes.py     # Recipe CRUD routes
├── templates/
│   ├── base.html      # Base template
│   ├── index.html     # Home page
│   ├── recipe_list.html
│   ├── recipe_detail.html
│   ├── recipe_form.html
│   └── recipe_search.html
└── static/
    └── style.css      # Stylesheet
```

## Features

- **Create Recipes** - Add new recipes with title, description, ingredients, and instructions
- **View Recipes** - Browse all recipes or filter by category
- **Edit Recipes** - Update any recipe details
- **Delete Recipes** - Remove recipes you no longer need
- **Search** - Find recipes by title or ingredients
- **Categories** - Organize recipes by category (Breakfast, Lunch, Dinner, Dessert, etc.)
- **Tags** - Mark recipes as "Favorite", "To Try", or "Made Before"
- **Ratings** - Rate recipes from 1-5 stars

## Adding a Recipe

1. Click "Add Recipe" in the navigation
2. Fill in the details:
   - **Title** (required)
   - **Description** (optional)
   - **Cooking Time** (in minutes)
   - **Difficulty** (Easy, Medium, Hard)
   - **Category** (with autocomplete suggestions)
   - **Tag** (Favorite, To Try, Made Before)
   - **Rating** (1-5 stars)
   - **Ingredients** (one per line)
   - **Instructions** (one step per line)
3. Click "Create Recipe"

## Filtering by Category

On the recipes list page:
- Click category pills to filter recipes
- Click "All" to see all recipes
- Click a category link on any recipe card or detail page

## Customizing Categories

The category field supports any text value. Suggested categories include:
- Breakfast, Lunch, Dinner, Dessert, Snack, Appetizer
- Italian, Mexican, Asian, American, Mediterranean

Simply type in the category field - it will auto-complete from existing categories.

## Testing

Run tests with pytest:

```bash
poetry run pytest
```

## License

MIT License
