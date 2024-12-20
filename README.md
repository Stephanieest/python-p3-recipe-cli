# Recipe Manager CLI App

Welcome to the **Recipe Manager CLI App**! This is a command-line tool to help you manage and organize recipes, ingredients, and their relationships in a simple way. The app uses an SQLite database (`company.db`) to store and retrieve your data.

## Features

- **Manage Recipes**: Add, list, and delete recipes.
- **Manage Ingredients**: Add, list, and delete ingredients.
- **Manage Recipe Ingredients**: Link ingredients to recipes and remove them as needed.

## Requirements

- **Python 3.x** installed on your system.
- **SQLite3** (Python’s built-in library for SQLite).

## Installation

### Step 1: Clone or Download the Repository

Clone the repository using Git:

```bash
git clone https://github.com/Stephanieest/python-p3-recipe-cli.git
cd python-p3-recipe-cli

Step 2: Set Up the Database
Before running the app, ensure that the required tables in the SQLite database are created. Run the following script to set up the tables:

python
Copy code
from models.recipe import Recipe
from models.ingredient import Ingredient
from models.recipe_ingredient import RecipeIngredient

Recipe.create_table()
Ingredient.create_table()
RecipeIngredient.create_table()
This will create the necessary tables (recipes, ingredients, recipe_ingredients) in the company.db file.

Step 3: Run the App
To run the app, execute the cli.py script:

bash
Copy code
python main.py
Usage
Once you run the app, you’ll be presented with a main menu where you can choose what to do:

Main Menu
markdown
Copy code
Please select an option:
0. Exit
1. Manage Recipes
2. Manage Ingredients
3. Manage Recipe Ingredients
Manage Recipes
Add Recipe
Enter a recipe name, description, and instructions.

Example input:

Enter recipe name: Pasta
Enter recipe description: A simple pasta recipe
Enter recipe instructions: Boil water, cook pasta, add sauce
List All Recipes
View all saved recipes with their names, descriptions, and instructions.

Delete Recipe
Delete a recipe by entering its ID.

Example input:

Enter the recipe ID to delete: 1
Manage Ingredients
Add Ingredient
Enter the name and quantity of an ingredient.

Example input:

Enter ingredient name: Tomato
Enter ingredient quantity: 2
List All Ingredients
View all saved ingredients with their names and quantities.

Delete Ingredient
Delete an ingredient by entering its ID.

Example input:

Enter the ingredient ID to delete: 1
Manage Recipe Ingredients
Add Recipe Ingredient
Link an ingredient to a recipe by entering both the recipe ID and ingredient ID.

Example input:

Enter recipe ID: 1
Enter ingredient ID: 1
List All Recipe Ingredients
View the links between recipes and their ingredients.

Delete Recipe Ingredient
Remove a recipe-ingredient link by entering its ID.

Example input:

Enter recipe ingredient ID to delete: 1
File Structure

python-p3-recipe-cli/
│
├── models/
│   ├── recipe.py             # Recipe class for managing recipes
│   ├── ingredient.py         # Ingredient class for managing ingredients
│   └── recipe_ingredient.py  # RecipeIngredient class for managing recipe-ingredient links
│
├── main.py                   # Main script to run the CLI app
├── company.db                # SQLite database where recipes, ingredients, and links are stored
└── requirements.txt          # (Optional) File with dependencies (if applicable)


License
This project is open-source and available under the MIT License.

Happy Cooking! 🍳
yaml
Copy code

---


