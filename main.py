import pygame as Py
from Button import *
from Button_image import *
from Admin import *

Py.init()

continuer = True
screen = Py.display.set_mode((900, 600))
font_maxi = Py.font.Font("./assets/font/Roboto-Black.ttf", 60)
font = Py.font.Font("./assets/font/Roboto-Black.ttf", 15)
product_button = Button(100, 20, 'PRODUIT', font_maxi, 0, 'Red', 'White')
category_button = Button(500, 20, 'CATEGORIE', font_maxi, 0, 'Red', 'White')
admin = Admin()

while continuer:
    if product_button.render(screen):
        screen.fill((0,0,0))
        total_product = admin.find_product_all()
        for index in total_product:
            rectangle = Py.Rect(20, 50 + 50 * index[0], 860, 40)
            Py.draw.rect(screen, 'White', rectangle)
            name_rectangle = Py.Rect(100, 50 + 50 * index[0], 80, 40)
            text_name = font.render(index[1], True, ('Black'))
            name_text = text_name.get_rect(center=name_rectangle.center)
            screen.blit(text_name, name_text)
            descritpion_name = Py.Rect(400, 50 + 50 * index[0], 20, 40)
            text_descritpion = font.render('description', True, ('Black'))
            descritpion_text = text_name.get_rect(center=descritpion_name.center)
            screen.blit(text_descritpion, descritpion_text)
            price_name = Py.Rect(550, 50 + 50 * index[0], 20, 40)
            text_price = font.render(str(index[3]), True, ('Black'))
            price_text = text_name.get_rect(center=price_name.center)
            screen.blit(text_price, price_text)
            quantity_name = Py.Rect(650, 50 + 50 * index[0], 20, 40)
            text_quantity = font.render(str(index[4]), True, ('Black'))
            quantity_text = text_name.get_rect(center=quantity_name.center)
            screen.blit(text_quantity, quantity_text)
            
    elif category_button.render(screen):
        screen.fill((0,0,0))
        total_category = admin.find_category_all()
        for index in total_category:
            rectangle = Py.Rect(20, 50 + 50 * index[0], 860, 40)
            Py.draw.rect(screen, 'White', rectangle)
            category_rectangle = Py.Rect(100, 50 + 50 * index[0], 80, 40)
            text_category = font.render(index[1], True, ('Black'))
            category_text = text_category.get_rect(center=category_rectangle.center)
            screen.blit(text_category, category_text)


    for event in Py.event.get():
        if event.type == Py.QUIT:
            continuer = False
    Py.display.flip()
Py.quit()    