# Recipe Management System

**recipe-ms** is a web based recipe manager totally built using AI (opencode and agents) accept for this file (the developer's notes). It makes use of flask (the python web framework) Jinja2 tempalte engine and sqlite3 for persistence.

## Tech Stack

- **Backend**: Flask (Python web framework)
- **WSGI Server**: Gunicorn
- **Database**: SQLite (built-in Python)
- **Templates**: Jinja2
- **Styling**: Custom CSS
- **Package Manager**: Poetry

## Prerequisites

- Python 3.9 or higher _(tested with python3.11)_
- Poetry _(for dependency management)_

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
- Navigate to code directory
- Create a virtual environment
- Install Flask and Jinja2
- Install development dependencies (pytest)

**NOTE:** unless stated otherwise, will always assume commands are running from `recipe_manager` directory _(rather from repository root directory)_

## Usage

### Running with Gunicorn (Recommended for Production)

```bash
poetry run gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app

# or (on linux)
`poetry env activate`
gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app
```

Options:
- `-w 4` - Number of worker processes
- `-b 0.0.0.0:5000` - Bind address
- `wsgi:app` - WSGI module and application variable

### Running in Development Mode

For development with auto-reload:

```bash
poetry run python app.py

# or (on linux) after `poetry env activate`:
python app.py
```

The application will start at `http://localhost:5000`

### Development vs Production

- **Development** (`python app.py`): Debug mode on, auto-reload
- **Production** (`gunicorn wsgi:app`): Debug off, multiple workers

## Project Structure

```
recipe_manager/
├── app.py              # Main Flask application
├── wsgi.py             # WSGI entry point for Gunicorn
├── config.py           # Configuration settings
├── models.py           # Database models and utilities
├── schema.sql          # Database schema
├── pyproject.toml      # Poetry configuration
├── poetry.lock         # Locked dependencies
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

**NO TESTS IMPLEMENTED**

```bash
poetry run pytest
```

## License

MIT License
