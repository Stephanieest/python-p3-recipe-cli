#!/usr/bin/env python3
# lib/debug.py

from models.ingredient import Ingredient

Ingredient(1, "cheese", "a block of cheese")

print(Ingredient.id)
print(Ingredient.name)
print(Ingredient.quantity)
