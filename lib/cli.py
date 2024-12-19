#!/usr/bin/env python3
# lib/cli.py

from models.recipe import Recipe
from models.ingredient import Ingredients
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
            print("Invalid choice!!!!")


def menu():
    print("Please select an option:")
    print("0. Exit")
    print("1. Manage Recipes")
    print("2. Manage Ingredients")
    print("3 Manage Recipe Ingredients")

def exit_program():
    print("Goodbye!!!")
    exit()


if __name__ == "__main__":
    main()
