from settings import *
import sys

# Texto
def text_creator(name_text, name_screen ,type, height, color):
    font = pygame.font.SysFont(None, 36)
    name_text = font.render(f'{name_screen}: {type}', True, color)
    SCREEN.blit(name_text, (10, height))

def titles(name_text, title, width ,height, color):
    font = pygame.font.SysFont(None, 36)
    name_text = font.render(f"{title}", True, color)
    SCREEN.blit(name_text, (width, height))

def wait_user(tecla):
    flag_start = True
    while flag_start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == tecla:
                    flag_start = False