import sqlite3

class RecipeIngredient:
    @classmethod
    def connect_db(cls):
        return sqlite3.connect("company.db")
    
    @classmethod
    def create_table(cls):
        conn = cls.connect_db()
        cursor = conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS recipe_ingredients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            recipe_id INTEGER,
            ingredient_id INTEGER,
            FOREIGN KEY (recipe_id) REFERENCES recipes(id),
            FOREIGN KEY (ingredient_id) REFERENCES ingredients(id)
        )
        """)
        
        conn.commit()
        conn.close()
    
    @classmethod
    def create(cls, recipe_id, ingredient_id):
        conn = cls.connect_db()
        cursor = conn.cursor()
        
        cursor.execute("""
        INSERT INTO recipe_ingredients (recipe_id, ingredient_id)
        VALUES (?, ?)
        """, (recipe_id, ingredient_id))
        
        conn.commit()
        recipe_ingredient_id = cursor.lastrowid
        conn.close()
        
        return cls(recipe_ingredient_id, recipe_id, ingredient_id)
    
    @classmethod
    def get_all(cls):
        conn = cls.connect_db()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM recipe_ingredients")
        rows = cursor.fetchall()
        
        conn.close()
        
        recipe_ingredients = [cls(row[0], row[1], row[2]) for row in rows]
        return recipe_ingredients
    
    @classmethod
    def delete(cls, recipe_ingredient_id):
        conn = cls.connect_db()
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM recipe_ingredients WHERE id = ?", (recipe_ingredient_id,))
        conn.commit()
        conn.close()
    
    def __init__(self, id, recipe_id, ingredient_id):
        self.id = id
        self.recipe_id = recipe_id
        self.ingredient_id = ingredient_id
    
    def show(self):
        return f"RecipeIngredient ID: {self.id}, Recipe ID: {self.recipe_id}, Ingredient ID: {self.ingredient_id}"
