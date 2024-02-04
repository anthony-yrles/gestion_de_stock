import pygame as Py
from Button import *
from Admin import *
from modify_render import *
from main_render import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd

Py.init()

continuer = True
screen = Py.display.set_mode((900, 600))
font_maxi = Py.font.Font("./assets/font/Roboto-Black.ttf", 60)
font = Py.font.Font("./assets/font/Roboto-Black.ttf", 15)
product_button = Button(100, 20, 'PRODUIT', font_maxi, 0, 'Red', 'White')
category_button = Button(500, 20, 'CATEGORIE', font_maxi, 0, 'Red', 'White')
ajouter_image = Py.image.load('./assets/images/plus.png')
ajouter = Button_image(150, 500, ajouter_image, 1)
modify_image = Py.image.load('./assets/images/modify.png')
modify = Button_image(425, 500, modify_image, 1)
trash_image = Py.image.load('./assets/images/trash.png')
trash = Button_image(700, 500, trash_image, 1)
modify_name = Button(100, 200, 'Nom', font_maxi, 1, 'Red', 'Blue') 
modify_description = Button(400, 200, 'Description', font_maxi, 1, 'Red', 'Blue') 
modify_price = Button(100, 400, 'Prix', font_maxi, 1, 'Red', 'Blue') 
modify_quantity = Button(400, 400, 'Quantité', font_maxi, 1, 'Red', 'Blue') 
modify_id_category = Button(500, 250, 'Catégori', font_maxi, 1, 'Red', 'Blue')
admin = Admin()

while continuer:
    if product_button.render(screen):
        main_render_product(screen, font, admin)          
    elif category_button.render(screen):
        main_render_category(screen, font, admin)
    elif ajouter.draw(screen):
        cat_or_product = mb.askyesno("Produit ou Catégorie", "Vous voulez ajouter un Produit")
        if cat_or_product == 1:
            name_input = sd.askstring("Nom", "Quel est le nom de l'objet que vous voulez ajouter?: ")
            description_input = sd.askstring("Description", "Quel est la description de l'objet que vous voulez ajouter?: ")
            price_input = sd.askstring("Prix", "Quel est le prix de l'objet que vous voulez ajouter?: ")
            quantity_input = sd.askstring("Quantité", "Combien d'objet voulez vous ajouter?: ")
            category_input = sd.askstring("Catégorie ID", "Quel est la catégorie de l'objet: ")
            admin.create_product(name_input, description_input, price_input, quantity_input, category_input)
        else:
            name_input = sd.askstring("Nom", "Quel est le nom de la catégorie que vous voulez ajouter?: ")
            admin.create_category(name_input)
    elif modify.draw(screen):
        cat_or_product = mb.askyesno("Produit ou Catégorie", "Vous voulez ajouter un Produit")
        if cat_or_product == 1:
            value_to_modif = sd.askstring("Modifier", "Quel valeur de produit voulez-vous modifier? :")
            new_value = sd.askstring("Modifier", "Quel est la nouvelle valeur :")
            id_choice = sd.askinteger("Id", "Quel est l'id de l'objet à modifier? :")
            admin.update_product(id_choice, value_to_modif, new_value)
        else:
            value_to_modif = sd.askstring("Modifier", "Quel valeur de categorie voulez-vous modifier? :")
            new_value = sd.askstring("Modifier", "Quel est la nouvelle valeur :")
            id_choice = sd.askinteger("Id", "Quel est l'id de la categorie à modifier? :")
            admin.update_category(id_choice, value_to_modif, new_value)
    elif trash.draw(screen):
        cat_or_product = mb.askyesno("Produit ou Catégorie", "Vous voulez ajouter un Produit")
        if cat_or_product == 1:
            id_to_delete = sd.askinteger("Supprimer", "Quel est l'id de l'objet à supprimer? :")
            admin.delete_product(id_to_delete)
        else:
            id_to_delete = sd.askinteger("Supprimer", "Quel est l'id de la catégorie à supprimer? :")
            admin.delete_category(id_to_delete)

    for event in Py.event.get():
        if event.type == Py.QUIT:
            continuer = False
    Py.display.flip()
Py.quit()    