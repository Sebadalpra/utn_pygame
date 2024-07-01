from settings import *
""" 
class Personaje:
    def __init__(self, nombre_pj) -> None:
        self.nombre = nombre_pj

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}")
    

personaje1 = Personaje("Marolio")
personaje1.saludar()
 """

player_x = WIDTH // 2
player_y = HEIGHT // 2
player_size = 50
player_speed = 5

personaje = (player_x, player_y, player_size, player_size)

# Recordar que si estoy adentro de una funcion no puedo usar cosas externas, entonces...
# usamos self, que guarda cosas en si mismo y nos permite utilziarlas afuera de esa misma funcion.
# En resumen self, guarda la direccion de memoria de la funcion para q pueda usarse externamente