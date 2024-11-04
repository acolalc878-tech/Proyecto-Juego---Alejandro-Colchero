# Constructor de la clase Personaje
from random import random

import pygame.font
import Constantes

class Personaje:
    def __init__(self, x, y):
        # Con Rect() creamos un rectangulo en la coordenada 0.0 y de tamaño 20 px por lado
        self.forma = pygame.Rect(0, 0, Constantes.ANCHO_PERSONAJE, Constantes.ALTO_PERSONAJE)
        self.forma.center = (x, y)

    def draw (self, ventana):
        pygame.draw.rect(ventana, Constantes.COLOR, self.forma)

    def mover_personaje(self, delta_x, delta_y):
        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y + delta_y