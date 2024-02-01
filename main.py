import pygame as Py
from Button import *
from Button_image import *
from Admin import *

Py.init()

continuer = True
screen = Py.display.set_mode((900, 600))
font_maxi = Py.font.Font("./assets/font/Roboto-Black.ttf", 60)
product_button = Button(100, 50, 'PRODUIT', font_maxi, 0, 'Red', 'White')
category_button = Button(500, 50, 'CATEGORIE', font_maxi, 0, 'Red', 'White')
admin = Admin()

while continuer:
    if product_button.render(screen):
        total_product = admin.find_product_all()
        for index in total_product:
    # if category_button.render(screen):

    for event in Py.event.get():
        if event.type == Py.QUIT:
            continuer = False
    Py.display.flip()
Py.quit()    