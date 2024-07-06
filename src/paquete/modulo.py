import pygame
from settings import *
from paquete.clases import *
from random import randint

enemy_list = []

def enemy_generator():
    if randint(0, 100) <= 1:
        enemy = Enemy(randint(0, WIDTH - 30), randint(-30, -10))
        enemy_list.append(enemy)