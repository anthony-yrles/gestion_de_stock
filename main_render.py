import pygame as Py
from Button_image import *


def main_render_product(screen, font, admin):
    screen.fill((0,0,0))
    total_product = admin.find_product_all()
    for index in total_product:
        rectangle = Py.Rect(20, 50 + 50 * index[0], 860, 40)
        Py.draw.rect(screen, 'White', rectangle)
        id_rectangle = Py.Rect(50, 50 + 50 * index[0], 80, 40)
        text_id = font.render(str(index[0]), True, ('Black'))
        id_text = text_id.get_rect(center=id_rectangle.center)
        screen.blit(text_id, id_text)
        name_rectangle = Py.Rect(250, 50 + 50 * index[0], 80, 40)
        text_name = font.render(index[1], True, ('Black'))
        name_text = text_name.get_rect(center=name_rectangle.center)
        screen.blit(text_name, name_text)
        descritpion_rectangle = Py.Rect(450, 50 + 50 * index[0], 20, 40)
        text_descritpion = font.render('...', True, ('Black'))
        descritpion_text = text_descritpion.get_rect(center=descritpion_rectangle.center)
        screen.blit(text_descritpion, descritpion_text)
        price_name = Py.Rect(570, 50 + 50 * index[0], 20, 40)
        text_price = font.render(str(index[3]), True, ('Black'))
        price_text = text_price.get_rect(center=price_name.center)
        screen.blit(text_price, price_text)
        quantity_name = Py.Rect(690, 50 + 50 * index[0], 20, 40)
        text_quantity = font.render(str(index[4]), True, ('Black'))
        quantity_text = text_quantity.get_rect(center=quantity_name.center)
        screen.blit(text_quantity, quantity_text)
        id_category_name = Py.Rect(810, 50 + 50 * index[0], 20, 40)
        text_id_category = font.render(str(index[5]), True, ('Black'))
        id_category_text = text_id_category.get_rect(center=id_category_name.center)
        screen.blit(text_id_category, id_category_text)

def main_render_category(screen, font, admin):
    screen.fill((0,0,0))
    total_category = admin.find_category_all()
    for index in total_category:
        rectangle = Py.Rect(20, 50 + 50 * index[0], 860, 40)
        Py.draw.rect(screen, 'White', rectangle)
        id_rectangle = Py.Rect(150, 50 + 50 * index[0], 80, 40)
        text_id = font.render(str(index[0]), True, ('Black'))
        id_text = text_id.get_rect(center=id_rectangle.center)
        screen.blit(text_id, id_text)
        category_rectangle = Py.Rect(650, 50 + 50 * index[0], 80, 40)
        text_category = font.render(index[1], True, ('Black'))
        category_text = text_category.get_rect(center=category_rectangle.center)
        screen.blit(text_category, category_text)