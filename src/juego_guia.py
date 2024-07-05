import pygame
import random
import math

# Inicializar Pygame
pygame.init()

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Dimensiones de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Defiende el Planeta")

# Planeta
planet_img = pygame.Surface((50, 50), pygame.SRCALPHA)
pygame.draw.circle(planet_img, BLUE, (25, 25), 25)

# Jugador
player_img = pygame.Surface((10, 10), pygame.SRCALPHA)
pygame.draw.circle(player_img, GREEN, (5, 5), 5)
player_pos = [WIDTH // 2, HEIGHT - 30]
player_speed = 5
player_health = 100

# Alien
alien_img = pygame.Surface((20, 20), pygame.SRCALPHA)
pygame.draw.circle(alien_img, RED, (10, 10), 10)

# Balas
bullet_img = pygame.Surface((5, 5), pygame.SRCALPHA)
pygame.draw.circle(bullet_img, WHITE, (2, 2), 2)
bullets = []
bullet_speed = 7

# Aliens
aliens = []
alien_speed = 2
aliens_killed = 0
aliens_to_win = 20

# Función para disparar
def shoot(x, y):
    bullets.append([x, y])

# Función para generar aliens
def generate_alien():
    angle = random.randint(0, 10)
    aliens.append([WIDTH // 2, HEIGHT // 2, angle])

# Bucle principal
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shoot(player_pos[0], player_pos[1])

    # Mover jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH:
        player_pos[0] += player_speed
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN] and player_pos[1] < HEIGHT:
        player_pos[1] += player_speed

    # Mover balas
    for bullet in bullets:
        bullet[1] -= bullet_speed
    bullets = [bullet for bullet in bullets if bullet[1] > 0]

    # Generar aliens
    if random.randint(1, 30) == 1:  # Incrementa la frecuencia de aparición
        generate_alien()

    # Mover aliens
    for alien in aliens:
        alien[0] += math.cos(alien[2]) * alien_speed
        alien[1] += math.sin(alien[2]) * alien_speed

    # Colisiones entre balas y aliens
    for alien in aliens:
        for bullet in bullets:
            if math.hypot(alien[0] - bullet[0], alien[1] - bullet[1]) < 15:
                aliens.remove(alien)
                bullets.remove(bullet)
                aliens_killed += 1
                break

    # Colisiones entre aliens y jugador
    for alien in aliens:
        if math.hypot(alien[0] - player_pos[0], alien[1] - player_pos[1]) < 20:
            player_health -= 20
            aliens.remove(alien)

    # Aliens fuera de la pantalla
    for alien in aliens:
        if alien[0] < 0 or alien[0] > WIDTH or alien[1] < 0 or alien[1] > HEIGHT:
            player_health -= 1
            aliens.remove(alien)

    # Dibujar
    screen.fill(BLACK)
    screen.blit(planet_img, (WIDTH // 2 - 25, HEIGHT // 2 - 25))
    screen.blit(player_img, player_pos)
    for bullet in bullets:
        screen.blit(bullet_img, bullet)
    for alien in aliens:
        screen.blit(alien_img, (alien[0] - 10, alien[1] - 10))

    # Mostrar vida del jugador
    font = pygame.font.SysFont(None, 36)
    health_text = font.render(f'Vida: {player_health}', True, WHITE)
    screen.blit(health_text, (10, 10))

    # Mostrar cantidad de aliens matados
    aliens_text = font.render(f'Aliens matados: {aliens_killed}', True, WHITE)
    screen.blit(aliens_text, (10, 50))

    pygame.display.flip()
    clock.tick(60)

    # Verificar si el jugador ha perdido
    if player_health <= 0:
        running = False

    # Verificar si el jugador ha ganado
    if aliens_killed >= aliens_to_win:
        running = False

pygame.quit()

# Mostrar mensaje de victoria o derrota
if player_health <= 0:
    print("¡Has perdido!")
else:
    print("¡Has ganado!")
 