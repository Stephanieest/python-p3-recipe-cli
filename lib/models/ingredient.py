import sqlite3

class Ingredient:
    @classmethod
    def connect_db(cls):
        return sqlite3.connect("company.db")
    
    @classmethod
    def create_table(cls):
        conn = cls.connect_db()
        cursor = conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS ingredients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity TEXT NOT NULL
        )
        """)
        
        conn.commit()
        conn.close()
    
    @classmethod
    def create(cls, name, quantity):
        conn = cls.connect_db()
        cursor = conn.cursor()
        
        cursor.execute("""
        INSERT INTO ingredients (name, quantity)
        VALUES (?, ?)
        """, (name, quantity))
        
        conn.commit()
        ingredient_id = cursor.lastrowid
        conn.close()
        
        return cls(ingredient_id, name, quantity)
    
    @classmethod
    def get_all(cls):
        conn = cls.connect_db()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM ingredients")
        rows = cursor.fetchall()
        
        conn.close()
        
        ingredients = [cls(row[0], row[1], row[2]) for row in rows]
        return ingredients
    
    @classmethod
    def find_by_id(cls, ingredient_id):
        conn = cls.connect_db()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM ingredients WHERE id = ?", (ingredient_id,))
        row = cursor.fetchone()
        
        conn.close()
        
        if row:
            return cls(row[0], row[1], row[2])
        return None
    
    @classmethod
    def delete(cls, ingredient_id):
        conn = cls.connect_db()
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM ingredients WHERE id = ?", (ingredient_id,))
        conn.commit()
        conn.close()
    
    def __init__(self, id, name, quantity):
        self.id = id
        self.name = name
        self.quantity = quantity
    
    def show(self):
        return f"Ingredient ID: {self.id}, Name: {self.name}, Quantity: {self.quantity}"
