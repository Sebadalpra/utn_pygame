import pygame
from settings import *
from paquete.clases import *
from random import randint

enemy_list = []

def enemy_generator():
    if randint(0, 100) <= 1:
        enemy = Enemy(WIDTH // 2 - 15, HEIGHT // 2 - 185)
        enemy_list.append(enemy)

    # Verificar colisiones
def collisions(player):
    for enemy in enemy_list[:]:
        enemy.move()

        # Obtener las coordenadas y dimensiones del enemigo
        ex, ey, ew, eh = enemy.x, enemy.y, enemy.width, enemy.height
        for bullet in player.bullets[:]:
            # Obtener las coordenadas y dimensiones de la bala
            bx, by, bw, bh = bullet.x, bullet.y, bullet.width, bullet.height
            
            # Verificar si hay colisión
            if (bx < ex + ew and bx + bw > ex and by < ey + eh and by + bh > ey):
                enemy_list.remove(enemy)
                player.score += 1
                player.bullets.remove(bullet)
                break

def enemy_out_screen(player):
    """Resta 5 de vida cada vez que un enemigo sale de la pantalla
    """
    for enemy in enemy_list[:]:
        if enemy.x + enemy.width < 0 or enemy.x > 800 or enemy.y + enemy.height < 0 or enemy.y > 600:
            player.health -= 5
            enemy_list.remove(enemy)