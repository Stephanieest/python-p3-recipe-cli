class Ingredients:
    ingredients = []


    def __init__(self, name, quantity):
        self.id = len(self._ingredients) + 1
        self.name = name
        self.quantity = quantity

    @classmethod
    def create(cls, name, quantity):
        ingredient = cls(name, quantity)
        cls._ingredients.append(ingredient)
        return ingredient
    
    @classmethod
    def get_all(cls):
        return cls._ingredients
    
    @classmethod
    def find_by_id(cls, ingredient_id):
        for ingredient in cls._ingredients:
            if ingredient.id == ingredient_id:
                return ingredient
        return None
    
    @classmethod
    def delete(cls, ingredient_id):
        ingredient = cls.find_by_id(ingredient_id)
        if ingredient:
            cls._ingredients.remove(ingredient)
        