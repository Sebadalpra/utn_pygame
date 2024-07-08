import pygame
from settings import *
from random import randint

class Player:
    def __init__(self, x, y) -> None:    
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.speed = 5
        self.health = 100
        self.score = 0
        self.image = pygame.image.load("./src/assets/img/robot.png")
        self.bullets = []

    def create_bullet(self):
        bullet = Bullet(self.x + self.width // 2, self.y)
        self.bullets.append(bullet)
                    
    def draw(self):  
        SCREEN.blit(self.image, (self.x, self.y))
        for bullet in self.bullets:
            bullet.draw()

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.dir_x = randint(-2, 2)  
        self.dir_y = randint(1, 2)  
        self.image = pygame.image.load("./src/assets/img/alien.png").convert_alpha()
        self.bullets = []

    def move(self):
        self.y += self.dir_y
        self.x += self.dir_x

    def draw(self):
        SCREEN.blit(self.image, (self.x, self.y))
        

class Planet:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.width = 250
        self.height = 250
        self.image = pygame.image.load("./src/assets/img/marte.png")

    def draw(self):
        SCREEN.blit(self.image, (self.x, self.y))

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 10
        self.width = 10
        self.height = 10
        self.image = pygame.image.load("./src/assets/img/laserRed06.png")

    def move(self):
        self.y -= self.speed

    def draw(self):
        SCREEN.blit(self.image, (self.x - self.width // 2, self.y))

class Star:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.image = pygame.image.load("./src/assets/img/star_gold.png").convert_alpha()
        self.bullets = []

    def draw(self):
        SCREEN.blit(self.image, (self.x, self.y))
