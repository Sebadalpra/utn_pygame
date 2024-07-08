from settings import *
import sys
import json
import csv


def cargar_y_escalar_imagen(ruta_imagen):
    """
    Carga una imagen desde una ruta y la escala al tamaño especificado.

    Args:
        ruta_imagen (str): Ruta del archivo de imagen.
        tamaño (tuple): Tamaño deseado para la imagen escalada (ancho, alto).

    Returns:
        pygame.Surface: Imagen escalada.
        pygame.Rect: Rectángulo de la imagen escalada.
    """
    imagen = pygame.image.load(ruta_imagen)
    imagen_escalada = pygame.transform.scale(imagen, SIZE_SCREEN)
    rectangulo_imagen = imagen_escalada.get_rect()

    return imagen_escalada, rectangulo_imagen

# Ejemplo de uso para cargar el fondo del inicio
FONDO_PANTALLA_INICIO, rect_inicio = cargar_y_escalar_imagen("./src/assets/img/astro.jpg")

# Ejemplo de uso para cargar el fondo de la pantalla final
FONDO_PANTALLA_FINAL, rect_final = cargar_y_escalar_imagen("./src/assets/img/astro.jpg")

def text_creator(text, font_size, color, position):
    """
    Crea un texto en la pantalla.

    Args:
        text (str): Texto a mostrar.
        font_size (int): Tamaño de la fuente.
        color (tuple): Color del texto en formato RGB.
        position (tuple): Posición (x, y) donde colocar el texto en la pantalla.
    """
    font = pygame.font.SysFont(None, font_size)
    text_surface = font.render(text, True, color)
    SCREEN.blit(text_surface, position)

def main_menu(play_sound):
    """
    Pantalla del menú principal.

    Args:
        play_sound (pygame.mixer.Sound): Sonido a reproducir al hacer clic en "Jugar".
    """
    flag_start = True
    while flag_start:
        SCREEN.blit(FONDO_PANTALLA_INICIO, (0, 0)) 
        text_creator("SALVA EL UNIVERSO!", 36, WHITE, (WIDTH // 2 - 128, HEIGHT - 500))

        play_clicked = draw_button(SCREEN, "Play", WIDTH // 2 - 50, HEIGHT // 2 - 50, 100, 50, GREEN, LIGHT_GREEN)
        exit_clicked = draw_button(SCREEN, "Salir", WIDTH // 2 - 50, HEIGHT // 2 + 50, 100, 50, RED, LIGHT_RED)

        if play_clicked:
            play_sound.play()
            flag_start = False
        if exit_clicked:
            pygame.quit()
            sys.exit()

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def save_score_json(player_name, score):
    """
    Guarda el nombre del jugador y su puntaje en un archivo JSON.

    Args:
        player_name (str): Nombre del jugador.
        score (int): Puntaje del jugador.
    """
    score_data = {"name": player_name, "score": score}
    
    try:
        with open("scores.json", "r") as file:
            scores = json.load(file)
    except FileNotFoundError:
        scores = []
    
    scores.append(score_data)
    scores = sorted(scores, key=lambda x: x["score"], reverse=True)[:3]  # Mantener solo los 3 mejores

    with open("scores.json", "w") as file:
        json.dump(scores, file, indent=4)

def show_scores(top_scores):
    """
    Muestra los mejores puntajes en la pantalla.

    Args:
        top_scores (list): Lista de diccionarios con los puntajes de los mejores jugadores.
    """
    posicion_y_inicial = 400  
    for score in top_scores:
        text_creator(f"{score['name']}: {score['score']}", 30, WHITE, (WIDTH // 2 - 75, posicion_y_inicial))
        posicion_y_inicial += 40

def game_over_screen(player):
    """
    Pantalla de fin de juego donde se guarda el puntaje del jugador.

    Args:
        player (obj): Objeto del jugador que contiene el puntaje.
    """
    game_over = True
    player_name = ""
    
    try:
        with open("scores.json", "r") as file:
            top_scores = json.load(file)
    except FileNotFoundError:
        top_scores = []

    while game_over:
        SCREEN.blit(FONDO_PANTALLA_FINAL, (0, 0)) 
        text_creator("GAME OVER", 36, WHITE, (WIDTH // 2 - 75, HEIGHT - 500))
        
        font = pygame.font.SysFont(None, 36)
        # --- Creación Rectangulo ---
        # Coordenadas, ancho y alto
        input_rect = pygame.Rect(WIDTH // 2 - 100, 200, 200, 50)
        # Dibujo el retangulo
        pygame.draw.rect(SCREEN, WHITE, input_rect, 2)

        # Le paso el nombre a la variable player_name
        name_surface = font.render(player_name, True, WHITE)
        # Posiciono el texto dentro del rectangulo
        SCREEN.blit(name_surface, (input_rect.x + 10, input_rect.y + 10))

        save_clicked = draw_button(SCREEN, "Guardar", WIDTH // 2 - 50, 220 + 60, 100, 50, BLUE, LIGHT_BLUE)
        
        show_scores(top_scores)

        if save_clicked:
            if player_name:
                save_score_json(player_name, player.score)
                game_over = False

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                elif event.key == pygame.K_RETURN:
                    if player_name:
                        save_score_json(player_name, player.score)
                        game_over = False
                else:
                    player_name += event.unicode



def draw_button(screen, text, x, y, width, height, inactive_color, active_color) -> bool:
    """
    Dibuja un botón en la pantalla.

    Args:
        screen (pygame.Surface): Superficie de la pantalla donde dibujar el botón.
        text (str): Texto que mostrar en el botón.
        x (int): Coordenada x del botón.
        y (int): Coordenada y del botón.
        width (int): Ancho del botón.
        height (int): Alto del botón.
        inactive_color (tuple): Color del botón cuando no está activo, en formato RGB.
        active_color (tuple): Color del botón cuando está activo, en formato RGB.

    Returns:
        bool: True si se hace clic en el botón y se pintará, False de lo contrario.
    """
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    button_rect = pygame.Rect(x, y, width, height)

    if button_rect.collidepoint(mouse):
        pygame.draw.rect(screen, active_color, button_rect)
        if click[0] == 1:
            return True
    else:
        pygame.draw.rect(screen, inactive_color, button_rect)

    font = pygame.font.SysFont(None, 36)
    text_surf = font.render(text, True, WHITE)
    text_rect = text_surf.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surf, text_rect)

    return False
