#!/usr/bin/env python3
from models.recipe import Recipe
from models.ingredient import Ingredient
from models.recipe_ingredient import RecipeIngredient


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            manage_recipes()
        elif choice == "2":
            manage_ingredients()
        elif choice == "3":
            manage_recipe_ingredients()
        else:
            print("Invalid choice!")

def menu():
    print("Please select an option:")
    print("0. Exit")
    print("1. Manage Recipes")
    print("2. Manage Ingredients")
    print("3. Manage Recipe Ingredients")

def exit_program():
    print("Goodbye!")
    exit()

def manage_recipes():
    while True:
        print("\n1. Add Recipe")
        print("2. List All Recipes")
        print("3. Delete Recipe")
        print("4. Back")
        choice = input("> ")
        
        if choice == "1":
            add_recipe()
        elif choice == "2":
            list_recipes()
        elif choice == "3":
            delete_recipe()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

def list_recipes():
    recipes = Recipe.get_all()
    if recipes:
        for recipe in recipes:
            print(recipe.show())
    else:
        print("No recipes found.")

def add_recipe():
    name = input("Enter recipe name: ")
    description = input("Enter recipe description: ")
    instructions = input("Enter recipe instructions: ")
    Recipe.create(name, description, instructions)
    print(f"Recipe '{name}' added successfully.")

def delete_recipe():
    recipe_id = input("Enter the recipe ID to delete: ")
    try:
        recipe_id = int(recipe_id)
        Recipe.delete(recipe_id)
        print(f"Recipe with ID {recipe_id} deleted.")
    except ValueError:
        print("Invalid ID. Please enter a number.")

def manage_ingredients():
    while True:
        print("\n1. Add Ingredient")
        print("2. List All Ingredients")
        print("3. Delete Ingredient")
        print("4. Back")
        choice = input("> ")
        
        if choice == "1":
            add_ingredient()
        elif choice == "2":
            list_ingredients()
        elif choice == "3":
            delete_ingredient()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

def list_ingredients():
    ingredients = Ingredient.get_all()
    if ingredients:
        for ingredient in ingredients:
            print(ingredient.show())
    else:
        print("No ingredients found.")

def add_ingredient():
    name = input("Enter ingredient name: ")
    quantity = input("Enter ingredient quantity: ")
    Ingredient.create(name, quantity)
    print(f"Ingredient '{name}' added successfully.")

def delete_ingredient():
    ingredient_id = input("Enter the ingredient ID to delete: ")
    try:
        ingredient_id = int(ingredient_id)
        Ingredient.delete(ingredient_id)
        print(f"Ingredient with ID {ingredient_id} deleted.")
    except ValueError:
        print("Invalid ID. Please enter a number.")

def manage_recipe_ingredients():
    while True:
        print("\n1. Add Recipe Ingredient")
        print("2. List All Recipe Ingredients")
        print("3. Delete Recipe Ingredient")
        print("4. Back")
        choice = input("> ")
        
        if choice == "1":
            add_recipe_ingredient()
        elif choice == "2":
            list_recipe_ingredients()
        elif choice == "3":
            delete_recipe_ingredient()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

def list_recipe_ingredients():
    recipe_ingredients = RecipeIngredient.get_all()
    if recipe_ingredients:
        for recipe_ingredient in recipe_ingredients:
            print(recipe_ingredient.show())
    else:
        print("No recipe ingredients found.")

def add_recipe_ingredient():
    recipe_id = input("Enter recipe ID: ")
    ingredient_id = input("Enter ingredient ID: ")
    try:
        recipe_id = int(recipe_id)
        ingredient_id = int(ingredient_id)
        RecipeIngredient.create(recipe_id, ingredient_id)
        print(f"Recipe Ingredient added: Recipe ID {recipe_id}, Ingredient ID {ingredient_id}.")
    except ValueError:
        print("Invalid IDs. Please enter valid numbers.")

def delete_recipe_ingredient():
    recipe_ingredient_id = input("Enter recipe ingredient ID to delete: ")
    try:
        recipe_ingredient_id = int(recipe_ingredient_id)
        RecipeIngredient.delete(recipe_ingredient_id)
        print(f"Recipe Ingredient with ID {recipe_ingredient_id} deleted.")
    except ValueError:
        print("Invalid ID. Please enter a number.")

if __name__ == "__main__":
    main()
