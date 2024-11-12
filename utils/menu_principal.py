import pygame

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


menu_buttons = True
menu_play = False
menu_editor = False
menu_sprite = False
menu_shop = False


# musiques

homeMusic = 'assets/musics/home_music.mp3'
shopMusic = 'assets/musics/shop_music.mp3'
