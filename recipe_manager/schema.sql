-- Database schema for recipe management system.

CREATE TABLE IF NOT EXISTS recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    ingredients TEXT NOT NULL,
    instructions TEXT NOT NULL,
    cooking_time INTEGER,
    difficulty TEXT CHECK(difficulty IN ('Easy', 'Medium', 'Hard')),
    category TEXT,
    tag TEXT CHECK(tag IN ('favorite', 'to_try', 'made_before', '')),
    rating INTEGER CHECK(rating >= 1 AND rating <= 5),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_recipes_title ON recipes(title);
CREATE INDEX IF NOT EXISTS idx_recipes_difficulty ON recipes(difficulty);
CREATE INDEX IF NOT EXISTS idx_recipes_tag ON recipes(tag);
CREATE INDEX IF NOT EXISTS idx_recipes_category ON recipes(category);
