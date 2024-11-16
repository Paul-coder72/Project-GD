import pygame
import random

from utils.variables import *
from utils.load_bg import *
from utils.menu_sprite import menu, shop
from utils.menu_principal import *
from game import *

pygame.init()

# contenu de la fenetre
        
background = pygame.transform.scale(background, (wrect.right, wrect.bottom))

def on_click_play():
    global menu_buttons, jeu_actif
    menu_buttons = False
    jeu_actif = True

def on_click_editor():
    global menu_buttons
    menu_buttons = False

def on_click_sprite():
    global menu_buttons, menu_sprite
    menu_buttons = False
    menu_sprite = True

def on_click_back():
    global menu_buttons, game, menu_editor, menu_sprite, menu_shop, background
    game = False
    menu_editor = False
    menu_sprite = False
    menu_shop = False
    menu_buttons = True

    background = bg7

def on_click_shop():
    global menu_buttons, menu_shop, menu_sprite, background
    menu_buttons = False
    menu_sprite = False
    menu_shop = True

    background = shop.shop_bg.convert()

def affichage():

    window.blit(background, (0, 0))
    global music
    
    if menu_buttons:
        window.blit(button_sprite, button_sprite_pos)
        window.blit(button_editor, button_editor_pos)
        window.blit(button_play, button_play_pos)
        window.blit(title, title_pos)
        if music != 0:
            music = 0
            pygame.mixer.music.load(homeMusic)
            pygame.mixer.music.play() 
            
    else:
        window.blit(button_back, button_back_pos)

    if game:
        window.blit(button_back, button_back_pos)

    if menu_sprite:
        window.blit(menu.shop_button, menu.shop_button_pos)

    if menu_shop:
        window.blit(shop.shop_shelf, shop.shop_shelf_pos)
        window.blit(shop.shop_deco, shop.shop_deco_pos)
        window.blit(shop.scratch, shop.scratch_pos)
        if music != 1:
            music = 1
            pygame.mixer.music.load(shopMusic)
            pygame.mixer.music.play() 


    pygame.display.update()

def check_music():
    if not pygame.mixer.music.get_busy():
        if music == 0:
            pygame.mixer.music.load(homeMusic)
            pygame.mixer.music.play()
        elif music == 1:
            pygame.mixer.music.load(shopMusic)
            pygame.mixer.music.play()

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.MOUSEBUTTONDOWN:

            if menu_buttons:
                if button_editor_pos.collidepoint(event.pos):
                    on_click_editor()
                elif button_play_pos.collidepoint(event.pos):
                    on_click_play()
                elif button_sprite_pos.collidepoint(event.pos):
                    on_click_sprite()
            else:
                if button_back_pos.collidepoint(event.pos):
                    on_click_back()
            
            if menu_sprite:
                if menu.shop_button_pos.collidepoint(event.pos):
                    on_click_shop()

    check_music()

    pygame.display.flip()
    clock.tick(60)
    
    affichage()



pygame.quit()
