from pygame import *
from settings import *
from paquete.clases import *
from paquete.player import *
from paquete.enemys import *
from paquete.collisions import *
from paquete.modulo import *
from random import randint
import sys

# Inicializacion
pygame.init()

# ---- Musica y sonidos ----
pygame.mixer.init()

pygame.mixer.music.load("./src/assets/music/interestellar_music.mp3")  
pygame.mixer.music.play(-1)  
pygame.mixer.music.set_volume(0.3)  
playing_music = True

shoot_sound = pygame.mixer.Sound("./src/assets/sounds/sfx_laser2.ogg") 
colision_sound = pygame.mixer.Sound("./src/assets/sounds/collision.ogg")
confirmation_sound = pygame.mixer.Sound("./src/assets/sounds/confirmation.ogg")

# ---- Configuracion pantalla ----
SCREEN = pygame.display.set_mode(SIZE_SCREEN)

# Cargar y escalar la imagen de fondo

BACKGROUND_IMAGE, rect_game = cargar_y_escalar_imagen("./src/assets/img/background-purple.png")


pygame.display.set_caption("Defiende el Universo!")

# Img enemigos
enemy2 = pygame.image.load("./src/assets/img/astronave.png").convert_alpha()
enemy3 = pygame.image.load("./src/assets/img/astronave2.png").convert_alpha()

# Representar y coordenadas de clases
planet = Planet(WIDTH // 2 - 128, HEIGHT // 2 - 280)
player = Player(WIDTH // 2 - 15, 500)

# Bucle
is_running = True

clock = pygame.time.Clock()

level = 1

confirmation_played = False

main_menu(confirmation_sound)

while is_running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.create_bullet()
                shoot_sound.play()

            elif event.key == pygame.K_m:
                if playing_music:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                playing_music = not playing_music
                
    
    # ------ Funcionalidades

    # Mover player
    player_movement(player)

    # Ajustar limites de pantalla player
    limit_player_screen(player)

    # Disparar
    shoot(player)
    

    # Generar enemigos según el nivel
    if player.score >= 5:
        enemy.image = enemy2
        enemy_creator(2) 
        level = 2
    if player.score >= 10:
        enemy.image = enemy3
        enemy_creator(3) 
        level = 3  
    else: 
        enemy_creator(1)


    # ---- Colisiones ----
    collisions_bullet_enemy(player, colision_sound)

    collisions_player_enemy(player, colision_sound)

    # Restar vida cada vez que sale un enemigo de la screen
    enemy_out_screen(player)

    # -------- Dibujar elementos ------------
    # Fondo
    SCREEN.blit(BACKGROUND_IMAGE, rect_game)

    # Planeta
    planet.draw()

    # Player
    player.draw()

    # Enemigos
    for enemy in enemy_list:
        enemy.draw()


    if not playing_music:
        text_creator("Sonido: MUTE", 36, GREEN, (10, 550))

    text_creator(f"Vida: {player.health}", 36, WHITE, (10, 10))
    text_creator(f"Score: {player.score}", 36, WHITE, (10, 40))
    text_creator(f"Nivel: {level}", 36, WHITE, (10, 70))
    pygame.display.flip()

    if player.score >= 15 or player.health <= 0:
        is_running = False

game_over_screen(player)

pygame.quit()
