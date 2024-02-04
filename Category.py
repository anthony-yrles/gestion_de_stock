from Db import Db

class Category:
    def __init__(self):
        self.table = 'category'
        self.db = Db(host='localhost', user='root', password='SKenan30mg/', database='store')

    def create(self, name):
        query = f'INSERT INTO {self.table} (name) VALUES (%s)'
        params = (name,)
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
        query = f'SELECT * FROM cage WHERE id=%s'
        params = (id,)
        return self.db.fetch(query, params)
    
    def find_all(self):
        query = f'SELECT * FROM category'
        return self.db.fetch(query)