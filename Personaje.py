# Constructor de la clase Personaje
from random import random

import pygame.font
from pygame.examples.cursors import image

import Constantes

class Personaje:
    def __init__(self, x, y, image):
        self.image = image
        # Con Rect() creamos un rectangulo en la coordenada 0.0 y de tamaño 20 px por lado
        self.forma = pygame.Rect(0, 0, Constantes.ANCHO_PERSONAJE, Constantes.ALTO_PERSONAJE)
        self.forma.center = (x, y)

    def draw (self, ventana):
        ventana.blit(self.image, self.forma)
        pygame.draw.rect(ventana, Constantes.COLOR, self.forma)

    def movimiento(self, delta_x, delta_y):
        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y + delta_y