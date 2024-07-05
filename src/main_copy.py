import pygame
from settings import *
from personaje import *

# Inicializacion
pygame.init()

# Configuracion pantalla
SCREEN = pygame.display.set_mode(SIZE_SCREEN)

background_image = pygame.image.load("./img/fondo.jpg").convert()
background_rect = background_image.get_rect()

pygame.display.set_caption("Defiende el Universo!")

# Representar y oordenadas del jugador
planet = Planet(WIDTH // 2 - 125, HEIGHT // 2 - 125)
player = Player(WIDTH // 2 - 30, 500)
enemy = Enemy(WIDTH // 2 - 30, HEIGHT // 2 - 30)

# Bucle
is_running = True

clock = pygame.time.Clock()
while is_running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    # Mover player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player.speed
    if keys[pygame.K_RIGHT]:
        player.x += player.speed
    if keys[pygame.K_UP]:
        player.y -= player.speed
    if keys[pygame.K_DOWN]:
        player.y += player.speed

    # Ajustar limites de pantalla player
    if player.x < 0:
        player.x = 0
    if player.x + player.width > WIDTH:
        player.x = WIDTH - player.width
    if player.y < 0:
        player.y = 0
    if player.y + player.height > HEIGHT:
        player.y = HEIGHT - player.height

    # -------------- Mostrar elementos ------------
    # Dibujar fondo
    SCREEN.blit(background_image, background_rect)


    # Dibujar elementos
    planet.draw()

    player.draw()

    enemy.draw()





    # Actualizar pantalla
    pygame.display.flip()

# Para liberar los recursos termino usando:
pygame.quit()
