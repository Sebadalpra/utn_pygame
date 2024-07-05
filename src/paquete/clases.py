import pygame
from settings import *

class Player:
    def __init__(self, x, y) -> None:    
        self.x = x
        self.y = y
        self.width = 60
        self.height = 70
        self.speed = 5
        self.health = 100
        self.image = pygame.image.load("img/robot.png")
        self.bullets = []

    def draw(self):  
        SCREEN.blit(self.image, (self.x, self.y))
        for bullet in self.bullets:
            bullet.draw(SCREEN)

    def shoot(self):
        bullet = Bullet(self.x + self.width // 2, self.y)
        self.bullets.append(bullet)
                    
class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.speed = 2
        self.health = 100
        self.image = pygame.image.load("img/alien.png").convert_alpha()
        self.enemy_list = []

    def draw(self):
        SCREEN.blit(self.image, (self.x, self.y))

class Planet:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.width = 250
        self.height = 250
        self.image = pygame.image.load("img/marte.png")

    def draw(self):
        SCREEN.blit(self.image, (self.x, self.y))

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 10
        self.width = 5
        self.height = 10
        self.color = WHITE

    def move(self):
        self.y -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))