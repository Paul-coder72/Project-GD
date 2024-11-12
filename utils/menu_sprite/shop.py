import pygame

shop_shelf = pygame.image.load('assets/img/icons/shop/shop_shelf.png')
shop_shelf_pos = shop_shelf.get_rect()
shop_shelf_pos.center = (512, 370)

scratch = pygame.image.load('assets//img/characters/shopkeeper/scratch3.png')
scratch_pos = scratch.get_rect()
scratch_pos.center = (650, 145)

shop_deco = pygame.image.load('assets/img/icons/shop/shop_deco.png')
shop_deco_pos = shop_deco.get_rect()
shop_deco_pos.center = (290, 190)

shop_bg = pygame.image.load('assets/img/icons/shop/bg_shop.png')
