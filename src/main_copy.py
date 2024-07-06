import pygame
from settings import *
from paquete.clases import *
from paquete.modulo import *
from random import randint

# Inicializacion
pygame.init()

# Configuracion pantalla
SCREEN = pygame.display.set_mode(SIZE_SCREEN)

background_image = pygame.image.load("./img/fondo.jpg").convert()
background_rect = background_image.get_rect()

pygame.display.set_caption("Defiende el Universo!")

# Representar y coordenadas de clases
planet = Planet(WIDTH // 2 - 125, HEIGHT // 2 - 125)
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


    # Mover player
    keys = pygame.key.get_pressed()
    #En cada iteracion nos devuelve False hasta que apretamos las teclas
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

    # Balas
    for bullet in player.bullets[:]:  # Itero sobre una copia de la lista de balas pero modifico/borro las balas de la lista original para poder recorrer bien los elementos.
        bullet.move()  # Mover cada bala hacia arriba
        if bullet.y < 0:  # Si la bala sale de la pantalla (y < 0)
            player.bullets.remove(bullet)  # Eliminar la bala de la lista original1

    for bullet in player.bullets:
        print(f"Bullet position: ({bullet.x}, {bullet.y})")
        print(f"Bullet speed: {bullet.color}")


    enemy_generator()


    # -------------- Mostrar elementos ------------
    # Dibujar fondo
    SCREEN.blit(background_image, background_rect)

    # ------ Mostrar vida ------
    font = pygame.font.SysFont(None, 36)
    health_text = font.render(f'Vida: {player.health}', True, WHITE)
    SCREEN.blit(health_text, (10, 10))


    # Dibujar elementos
    planet.draw()

    player.draw()

    # -------------- Enemys -----------------------

    for enemy in enemy_list[:]:
        enemy.draw()
        enemy.y += enemy.speed

    """ 
    if enemy.y > 600 or enemy.y + player.height < 0 or enemy.x + player.width < 0 or enemy.x > 800:
            player.health -= 30 """

    # Actualizar pantalla
    pygame.display.flip()

# Para liberar los recursos termino usando:
pygame.quit()
