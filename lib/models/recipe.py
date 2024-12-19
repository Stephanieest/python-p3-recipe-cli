class Recipe:
    recipes = []

    def __init__(self, name, description, instructions):
        self.recipe_id = len(self._recipes) + 1
        self.name = name
        self.description = description
        self.insturctions = instructions

    
    @classmethod
    def create(cls, name, description, instructions):
        recipe = cls(name, description, instructions)
        cls._recipes.append(recipe)
        return recipe
    
    @classmethod
    def get_all(cls):
        return cls._recipes
    
    @classmethod
    def find_by_recipe_id(cls, recipe_id)
        for recipe in cls._recipes:
            if recipe.recipe_id == recipe_id:
                return recipe
        return None
    
    @classmethod
    def delete(cls, recipe_id)
        recipe = cls.find_by_recipe_id(recipe_id)
        if recipe :
            cls._recipes.remove(recipe)

    def show(self):
        return f"Recipe ID: {self.recipe_id} Name: {self.name}, Description: {self.desctiption}, Instructions: {self.instruvtions}"
    
    