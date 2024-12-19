class RecipeIngredient:
    recipe_ingredients = []

    def __init__(self, recipe_id, ingredient_id):
        self.id = len(self._recipe_ingredients) + 1
        self.recipe_id = recipe_id
        self.ingredient_id = ingredient_id

    @classmethod
    def create (cls, recipe_id, ingredient_id):
        recipe_ingredient = cls(recipe_id, ingredient_id)
        cls._recipe_ingredients.append(recipe_ingredient)
        return recipe_ingredient
    
    @classmethod
    def get_all(cls):
        return cls._recipe_ingredients
    
    @classmethod
    def delete(cls, recipe_ingredient_id):
        recipe_ingredient = next((ingredient for ingredient in cls._recipe_ingredients if ingredient.id == recipe_ingredient_id), None)
        if recipe_ingredient:
            cls._recipe_ingredients.remove(recipe_ingredient)

        