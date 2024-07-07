import pygame
from settings import *
from paquete.clases import *
from paquete.player import *
from paquete.enemys import *
from random import randint

# Inicializacion
pygame.init()

# Configuracion pantalla
SCREEN = pygame.display.set_mode(SIZE_SCREEN)

background_image = pygame.image.load("./src/assets/img/fondo.jpg").convert()
background_rect = background_image.get_rect()

pygame.display.set_caption("Defiende el Universo!")

# Representar y coordenadas de clases
planet = Planet(WIDTH // 2 - 128, HEIGHT // 2 - 280)
player = Player(WIDTH // 2 - 15, 500)

# Bucle
is_running = True

clock = pygame.time.Clock()
while is_running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # ------ Funcionalidades

    # Mover player
    player_movement(player)

    # Ajustar limites de pantalla player
    limit_player_screen(player)

    # Mover balas
    move_bullets(player)

    # Generar enemigos
    enemy_generator()

    # Colisiones
    collisions(player)

    # Restar vida cada vez que sale un enemigo de la screen
    enemy_out_screen(player)

    # -------- Dibujar elementos ------------
    # Fondo
    SCREEN.blit(background_image, background_rect)

    # Planeta
    planet.draw()

    # Player
    player.draw()

    # Enemigos
    for enemy in enemy_list:
        enemy.draw()

    # Texto Health
    font = pygame.font.SysFont(None, 36)
    health_text = font.render(f'Vida: {player.health}', True, WHITE)
    SCREEN.blit(health_text, (10, 10))

    # Texto Score
    font = pygame.font.SysFont(None, 36)
    health_text = font.render(f'Score: {player.score}', True, WHITE)
    SCREEN.blit(health_text, (10, 30))



    pygame.display.flip()

pygame.quit()
