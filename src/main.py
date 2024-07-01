import pygame
from settings import *
from personaje import *

# Inicializacion de modulos de pygame
# hace que pygame se conecte con el hardware (placa de video, ram etc)
pygame.init()   


# El modulo display de pygame nos crea una pantalla
SCREEN = pygame.display.set_mode((SIZE_SCREEN))
pygame.display.set_caption("Primer juego")



# desenpaquetar nombre y valor en dos variables distintas:


# Bucle -> ya que un juego muestra 60 veces por segundo una pantalla
    # Relevar eventos (los eventos son cosas q suceden en la app)
    # Analizar eventos
    # Actualizar elementos del juego
    # Dibujar pantalla
    # Actualizar pantalla
# Vuelve a empezar el bucle

is_running = True

while is_running:
    # los eventos son cosas q suceden en la app. Ej: evento quit es para salir de la app
    # los eventos en pygame son numeros
    for event in pygame.event.get():
    # esto me trae una lista de eventos debo recorrerla con el for
        # pygame.QUIT me dice que quit es de tipo entero, ya que fue progamada con el numero 256
        if event.type == pygame.QUIT:
            # me permite salir del programa
            is_running = False

    # Obtener el estado de las teclas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Limitar el movimiento del jugador a los bordes de la pantalla
    player_x = max(0, min(WIDTH - player_size, player_x))
    player_y = max(0, min(HEIGHT - player_size, player_y))

    SCREEN.fill((BLUE))
    pygame.draw.rect(SCREEN, RED, (player_x, player_y, player_size, player_size))
    
# previo pinte color en memoria y con el flip lo muestra.
    pygame.display.flip()

    pygame.time.Clock().tick(60)

# Para liberar los recursos termino usando:
pygame.quit()