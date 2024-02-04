from Db import Db

class Product:
    def __init__(self):
        self.table = 'product'
        self.db = Db(host='localhost', user='root', password='SKenan30mg/', database='store')

    def create(self, name, description, price, quantity, id_category):
        query = f'INSERT INTO {self.table} (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)'
        params = (name, description, price, quantity, id_category)
        self.db.executeQuery(query, params)
    
    def update(self, id, column, new_value):
        query = f"UPDATE {self.table} SET {column} = %s WHERE id = %s"
        values = (new_value, id)
        self.db.executeQuery(query, values)

    
    def delete(self, id):
        query = f'DELETE FROM {self.table} WHERE id=%s'
        params = (id,)
        self.db.executeQuery(query, params)
    
    def find(self, id):
        query = f'SELECT * FROM {self.table} WHERE id=%s'
        params = (id,)
        return self.db.fetch(query, params)
    
    def find_all(self):
        query = f'SELECT * FROM {self.table}'
        return self.db.fetch(query)