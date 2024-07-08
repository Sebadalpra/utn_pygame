from paquete.enemys import enemy_list

# Verificar colisiones
def collisions_player_enemy(player, sound):
    """
    Verifica y maneja las colisiones entre el jugador y los enemigos.

    Args:
        player (obj): Objeto del jugador que contiene la posición y dimensiones.
        sound (pygame.mixer.Sound): Sonido a reproducir al producirse una colisión.
    """
    for enemy in enemy_list[:]:
        # Obtener las coordenadas y dimensiones del enemigo
        ex, ey, ew, eh = enemy.x, enemy.y, enemy.width, enemy.height
        # Obtener las coordenadas y dimensiones del jugador
        px, py, pw, ph = player.x, player.y, player.width, player.height

        # Verificar si hay colisión
        if (px < ex + ew and px + pw > ex and py < ey + eh and py + ph > ey):
            sound.play()
            enemy_list.remove(enemy)
            player.health -= 10  # Restar vida al jugador
            break

def collisions_bullet_enemy(player, sound):
    """
    Verifica y maneja las colisiones entre las balas del jugador y los enemigos.

    Args:
        player (obj): Objeto del jugador que contiene las balas y los enemigos.
        sound (pygame.mixer.Sound): Sonido a reproducir al producirse una colisión.
    """
    for enemy in enemy_list[:]:
        enemy.move()
        
        # Obtener las coordenadas y dimensiones del enemigo
        ex, ey, ew, eh = enemy.x, enemy.y, enemy.width, enemy.height
        for bullet in player.bullets[:]:
            # Obtener las coordenadas y dimensiones de la bala
            bx, by, bw, bh = bullet.x, bullet.y, bullet.width, bullet.height
            
            # Verificar si hay colisión
            if (bx < ex + ew and bx + bw > ex and by < ey + eh and by + bh > ey):
                sound.play()
                enemy_list.remove(enemy)
                player.score += 1
                player.bullets.remove(bullet)
                break

