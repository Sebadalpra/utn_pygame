import pygame
import sys

# Inicializa Pygame
pygame.init()

# Configura las dimensiones de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Colores
black = (0, 0, 0)
white = (255, 255, 255)

# Frames per second
fps = 60
clock = pygame.time.Clock()

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 100)

    def draw(self):
        pygame.draw.rect(screen, white, self.rect)

    def move(self, y_change):
        self.rect.y += y_change
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height

class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 15, 15)
        self.x_velocity = 5
        self.y_velocity = 5

    def draw(self):
        pygame.draw.rect(screen, white, self.rect)

    def move(self):
        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity

        if self.rect.top < 0 or self.rect.bottom > screen_height:
            self.y_velocity *= -1

        if self.rect.left < 0 or self.rect.right > screen_width:
            self.x_velocity *= -1

        if self.rect.colliderect(player_paddle.rect) or self.rect.colliderect(opponent_paddle.rect):
            self.x_velocity *= -1

# Inicializa los objetos
player_paddle = Paddle(screen_width - 20, screen_height // 2 - 50)
opponent_paddle = Paddle(10, screen_height // 2 - 50)
ball = Ball(screen_width // 2, screen_height // 2)

# Variables de control
player_speed = 0
opponent_speed = 5

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed = -5
            if event.key == pygame.K_DOWN:
                player_speed = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_speed = 0

    # Movimiento de las paletas
    player_paddle.move(player_speed)

    if opponent_paddle.rect.top < ball.rect.y:
        opponent_paddle.move(opponent_speed)
    if opponent_paddle.rect.bottom > ball.rect.y:
        opponent_paddle.move(-opponent_speed)

    # Movimiento de la pelota
    ball.move()

    # Dibuja todo en la pantalla
    screen.fill(black)
    player_paddle.draw()
    opponent_paddle.draw()
    ball.draw()

    pygame.display.flip()
    clock.tick(fps)
