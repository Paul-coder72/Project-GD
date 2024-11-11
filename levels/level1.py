import pygame
pygame.init()


lvl1difficulty = pygame.image.load('assets/img/icons/difficulty/d_easy.png')
lvl1difficulty_pos = lvl1difficulty.get_rect()
lvl1difficulty_pos.center = (150, 230)

lvl1name = pygame.image.load('assets/img/texts/stereoMadness.png')
lvl1name_pos = lvl1name.get_rect()
lvl1name_pos.center = (512, 230)

lvl1rightArrow = pygame.image.load('assets/img/icons/buttons/right_arrow.png')
lvl1rightArrow_pos = lvl1rightArrow.get_rect()
lvl1rightArrow_pos.center = (950, 400)