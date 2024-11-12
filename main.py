import pygame
import random

from variables import *
from load_bg import *
from menu_sprite import menu, shop
from levels import level1, level2, level3

pygame.init()
	
icon = pygame.image.load("assets/icon.ico")
pygame.display.set_caption("Geometry Dash")
pygame.display.set_icon(icon)


window = pygame.display.set_mode((1024, 560))

wrect = window.get_rect()

background = bg7.convert()

# contenu de la fenetre
        
button_play = pygame.image.load("assets/img/icons/buttons/play_button.png")
button_play_pos = button_play.get_rect()
button_play_pos.center = (512, 280)

button_sprite = pygame.image.load("assets/img/icons/buttons/sprite_button.png")
button_sprite_pos = button_sprite.get_rect()
button_sprite_pos.center = (282, 280)

button_editor = pygame.image.load("assets/img/icons/buttons/create_button.png")
button_editor_pos = button_editor.get_rect()
button_editor_pos.center = (742, 280)

title = pygame.image.load("assets/img/logos/geometry dash.png")
title_pos = title.get_rect()
title_pos.center = (512, 100)

button_back = pygame.image.load("assets/img/icons/buttons/back_button.png")
button_back_pos = button_back.get_rect()
button_back_pos.center = (35, 45)

gray_rect = pygame.image.load("assets/img/icons/gray_rect.png")
gray_rect_pos = gray_rect.get_rect()
gray_rect_pos.center = (512, 230)

global menu_play

background = pygame.transform.scale(background, (wrect.right, wrect.bottom))

menu_buttons = True
menu_play = False
menu_editor = False
menu_sprite = False
menu_shop = False

def on_click_play():
    global menu_buttons, menu_play
    global lvl1, lvl2, lvl3, lvl4, lvl5
    menu_buttons = False
    menu_play = True

    lvl1 = True

def on_click_editor():
    global menu_buttons
    menu_buttons = False

def on_click_sprite():
    global menu_buttons, menu_sprite
    menu_buttons = False
    menu_sprite = True

def on_click_back():
    global menu_buttons, menu_play, menu_editor, menu_sprite, menu_shop, background
    menu_play = False
    menu_editor = False
    menu_sprite = False
    menu_shop = False
    menu_buttons = True

    background = bg7.convert()

def on_click_shop():
    global menu_buttons, menu_shop, menu_sprite, background
    menu_buttons = False
    menu_sprite = False
    menu_shop = True

    background = shop.shop_bg.convert()


def affichage():

    window.blit(background, (0, 0))
    if menu_buttons:
        window.blit(button_sprite, button_sprite_pos)
        window.blit(button_editor, button_editor_pos)
        window.blit(button_play, button_play_pos)
        window.blit(title, title_pos)
        
    if menu_buttons == False:
        window.blit(button_back, button_back_pos)
    
    if menu_play:
        window.blit(gray_rect, gray_rect_pos)

        if lvl1:
            window.blit(level1.lvl1difficulty, level1.lvl1difficulty_pos)
            window.blit(level1.lvl1name, level1.lvl1name_pos)
            window.blit(level1.lvl1rightArrow, level1.lvl1rightArrow_pos)

    if menu_sprite:
        window.blit(menu.shop_button, menu.shop_button_pos)

    if menu_shop:
        window.blit(shop.shop_shelf, shop.shop_shelf_pos)

    pygame.display.update()
    

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:

            if menu_buttons:
                if button_editor_pos.collidepoint(event.pos):
                    on_click_editor()
                elif button_play_pos.collidepoint(event.pos):
                    on_click_play()
                elif button_sprite_pos.collidepoint(event.pos):
                    on_click_sprite()

            elif not menu_buttons:
                if button_back_pos.collidepoint(event.pos):
                    on_click_back()
            
            if menu_sprite:
                if menu.shop_button_pos.collidepoint(event.pos):
                    on_click_shop()
                

    pygame.display.flip()
    clock.tick(60)
    
    affichage()


pygame.quit()

