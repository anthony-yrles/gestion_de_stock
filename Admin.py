from Category import *
from Product import *

class Admin:
    def __init__(self) -> None:
        self.category = Category()
        self.product = Product()

    def create_category(self, name):
        self.category.create(name)
    
    def create_product(self, name, descritpion, prix, quantity, id_category):
        self.product.create(name, descritpion, prix, quantity, id_category)
    
    def update_category(self, id, name):
        self.category.update(id, name)

    def update_product(self, id, name, descritpion, prix, quantity, id_category):
        self.product.update(id, name, descritpion, prix, quantity, id_category)

    def delete_category(self, id):
        self.category.delete(id)

    def delete_product(self, id):
        self.product.delete(id)

    def find_category(self, id):
        self.category.find(id)

    def find_product(self, id):
        self.product.find(id)

    def find_category_all(self):
        return self.product.find_all()

    def find_product_all(self):
        return self.product.find_all()