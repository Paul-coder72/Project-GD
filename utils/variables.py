import pygame
from utils.load_bg import *

icon = pygame.image.load("assets/icon.ico")
pygame.display.set_caption("Geometry Dash")
pygame.display.set_icon(icon)


window = pygame.display.set_mode((1024, 560))

music = -1

wrect = window.get_rect()

background = bg7.convert()

clock = pygame.time.Clock()
