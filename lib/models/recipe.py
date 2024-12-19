import sqlite3

class Recipe:
    def __init__(self, id, name, description, instructions):
        self.id = id
        self.name = name
        self.description = description
        self.instructions = instructions

    @classmethod
    def connect_db(cls):

        return sqlite3.connect("recipes.db")

    @classmethod
    def create_table(cls):
        
        conn = cls.connect_db()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            instructions TEXT
        )
        """)

        conn.commit()
        conn.close()

    @classmethod
    def create(cls, name, description, instructions):
        
        conn = cls.connect_db()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO recipes (name, description, instructions)
        VALUES (?, ?, ?)
        """, (name, description, instructions))

        conn.commit()
        recipe_id = cursor.lastrowid  
        conn.close()

        return cls(recipe_id, name, description, instructions)

    @classmethod
    def get_all(cls):
       
        conn = cls.connect_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM recipes")
        rows = cursor.fetchall()

        conn.close()

        
        recipes = [cls(row[0], row[1], row[2], row[3]) for row in rows]
        return recipes

    @classmethod
    def find_by_recipe_id(cls, recipe_id):
        
        conn = cls.connect_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM recipes WHERE id = ?", (recipe_id,))
        row = cursor.fetchone()

        conn.close()

        if row:
            return cls(row[0], row[1], row[2], row[3])
        return None

    @classmethod
    def delete(cls, recipe_id):
        # Delete a recipe by its ID
        conn = cls.connect_db()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM recipes WHERE id = ?", (recipe_id,))
        conn.commit()
        conn.close()

    def show(self):
        return f"Recipe ID: {self.id} Name: {self.name}, Description: {self.description}, Instructions: {self.instructions}"
