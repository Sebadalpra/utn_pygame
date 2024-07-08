from settings import *
from paquete.clases import *
from random import randint

enemy_list = []
star_list = []

def object_creator(probability_number, list, clase, x, y):
    """
    Crea un enemigo/estrella con una cierta probabilidad.

    Args:
        probability_number (int): Número que determina la probabilidad de creación del enemigo.
        Se compara con un valor aleatorio entre 0 y 200.
    """
    if randint(0, 1000) <= probability_number:
        variable = clase(x, y)
        list.append(variable)

def enemy_out_screen(player):
    """
    Reduce 5 de vida del jugador cuando un enemigo sale de la pantalla.

    Args:
        player (obj): Objeto del jugador que contiene la vida a reducir.
    """
    for enemy in enemy_list[:]:
        if enemy.x + enemy.width < 0 or enemy.x > 800 or enemy.y + enemy.height < 0 or enemy.y > 600:
            player.health -= 5
            enemy_list.remove(enemy)