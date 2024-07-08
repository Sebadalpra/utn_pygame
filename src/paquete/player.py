import pygame
from settings import *
from paquete.clases import *

# Mover player
# Get_pressed me devuelve True cuando se apreto una flecha
def player_movement(player):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player.speed
    if keys[pygame.K_RIGHT]:
        player.x += player.speed
    if keys[pygame.K_UP]:
        player.y -= player.speed
    if keys[pygame.K_DOWN]:
        player.y += player.speed

# Limitar la pantalla al player
def limit_player_screen(player):
    if player.x < 0:
        player.x = 0
    if player.x + player.width > WIDTH:
        player.x = WIDTH - player.width
    if player.y < 0:
        player.y = 0
    if player.y + player.height > HEIGHT:
        player.y = HEIGHT - player.height

# Mover balas
def shoot(player):
    for bullet in player.bullets[:]:
        bullet.move()
        if bullet.y < 0:
            player.bullets.remove(bullet)


