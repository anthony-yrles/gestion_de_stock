import pygame as Py

def render_modify(screen, modify_name, modify_description, modify_price, modify_quantity, modify_id_category):
    screen.fill((0,0,0))
    modify_name.render(screen)
    modify_description.render(screen) 
    modify_price.render(screen)         
    modify_quantity.render(screen)         
    modify_id_category.render(screen)  