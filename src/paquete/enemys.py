from settings import *
from paquete.clases import *
from random import randint

enemy_list = []

def enemy_creator(probability_number):
    if randint(0, 200) <= probability_number:
        enemy = Enemy(WIDTH // 2 - 15, HEIGHT // 2 - 185)
        enemy_list.append(enemy)

def enemy_out_screen(player):
    """Resta 5 de vida cada vez que un enemigo sale de la pantalla
    """
    for enemy in enemy_list[:]:
        if enemy.x + enemy.width < 0 or enemy.x > 800 or enemy.y + enemy.height < 0 or enemy.y > 600:
            player.health -= 5
            enemy_list.remove(enemy)