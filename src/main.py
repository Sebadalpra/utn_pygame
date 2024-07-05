import pygame
from settings import *
from paquete.clases import *
import random

# Inicializacion
pygame.init()

# Configuracion pantalla
SCREEN = pygame.display.set_mode(SIZE_SCREEN)

background_image = pygame.image.load("./img/fondo.jpg").convert()
background_rect = background_image.get_rect()

pygame.display.set_caption("Defiende el Universo!")

# Representar y coordenadas de clases
planet = Planet(WIDTH // 2 - 125, HEIGHT // 2 - 125)
player = Player(WIDTH // 2 - 30, 500)

enemies = []

# Función para generar enemigos
def generate_enemy():
    x = planet.x + planet.width // 2
    y = planet.y + planet.height // 2
    angle = random.uniform(0, 2 * math.pi)
    direction = (math.cos(angle), math.sin(angle))
    enemy = Enemy(x, y, direction)
    enemies.append(enemy)

# Bucle principal
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

    # Generar enemigos cada cierto tiempo
    if random.randint(0, 100) < 2:  # Aproximadamente 2% de probabilidad por cuadro
        generate_enemy()

    # Mover y dibujar enemigos
    for enemy in enemies:
        enemy.move()
        if enemy.x < 0 or enemy.x > WIDTH or enemy.y < 0 or enemy.y > HEIGHT:
            enemies.remove(enemy)

    # Mover balas
    for bullet in player.bullets[:]:  # Iterar sobre una copia de la lista de balas
        bullet.move()  # Mover cada bala hacia arriba
        if bullet.y < 0:  # Si la bala sale de la pantalla (y < 0)
            player.bullets.remove(bullet)  # Eliminar la bala de la lista original

    # -------------- Mostrar elementos ------------
    # Dibujar fondo
    SCREEN.blit(background_image, background_rect)

    # Dibujar elementos
    planet.draw()
    player.draw()

    for enemy in enemies:
        enemy.draw()

    # Actualizar pantalla
    pygame.display.flip()

# Para liberar los recursos
pygame.quit()
