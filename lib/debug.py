#!/usr/bin/env python3
# lib/debug.py

from models.recipe import Recipe

recipe_instance = Recipe("1","chicken", "meat from bird", "cook it")

print(recipe_instance.id)
print(recipe_instance.name)
print(recipe_instance.description)
print(recipe_instance.instructions)





