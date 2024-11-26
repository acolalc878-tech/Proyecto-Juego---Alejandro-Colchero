import pygame
from Controlador import Constantes

class Ventana:
    def __init__(self):
        pygame.init()
        self.ventana = pygame.display.set_mode((Constantes.ANCHO_VENTANA, Constantes.ALTO_VENTANA))
        pygame.display.set_caption("AstroSlayer")
        self.reloj = pygame.time.Clock()

    def dibujar_fondo(self):
        self.ventana.fill(Constantes.COLOR_FONDO)

    def actualizar(self):
        pygame.display.update()

    def controlar_fotoramas(self):
        self.reloj.tick(Constantes.FPS)

    def cerrar(self):
        pygame.quit()