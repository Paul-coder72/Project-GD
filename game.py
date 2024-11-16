import pygame
import random

from utils.variables import *

# Paramètres de la fenêtre
largeur, hauteur = 1024, 560

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)

# Paramètres du joueur
joueur_size = 30
joueur_x = 50
joueur_y = hauteur - joueur_size - 50
joueur_vitesse_y = 0
saut = False

# Paramètres des obstacles
obstacle_largeur = 30
obstacle_hauteur = 70
obstacle_vitesse = 5
obstacles = []

# Score
score = 0
police = pygame.font.Font(None, 36)

# Boucle de jeu principale
clock = pygame.time.Clock()
jeu_actif = False

while jeu_actif:
    window.fill(BLANC)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jeu_actif = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not saut:
                saut = True
                joueur_vitesse_y = -15

    # Mécanique du saut
    if saut:
        joueur_y += joueur_vitesse_y
        joueur_vitesse_y += 1  # Gravité
        if joueur_y >= hauteur - joueur_size - 50:
            joueur_y = hauteur - joueur_size - 50
            saut = False

    # Gestion des obstacles
    if len(obstacles) == 0 or obstacles[-1][0] < largeur - 200:
        obstacles.append([largeur, hauteur - obstacle_hauteur - 50])
    for obstacle in obstacles:
        obstacle[0] -= obstacle_vitesse
        pygame.draw.rect(window, ROUGE, (obstacle[0], obstacle[1], obstacle_largeur, obstacle_hauteur))
        if obstacle[0] + obstacle_largeur < 0:
            obstacles.remove(obstacle)
            score += 1  # Augmenter le score lorsque l'obstacle est franchi

    # Détection des collisions
    for obstacle in obstacles:
        if joueur_x < obstacle[0] + obstacle_largeur and joueur_x + joueur_size > obstacle[0] and joueur_y + joueur_size > obstacle[1]:
            jeu_actif = False

    # Dessiner le joueur
    pygame.draw.rect(window, NOIR, (joueur_x, joueur_y, joueur_size, joueur_size))

    # Affichage du score
    texte_score = police.render("Score: " + str(score), True, NOIR)
    window.blit(texte_score, (10, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
