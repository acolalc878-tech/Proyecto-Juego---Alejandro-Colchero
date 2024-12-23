import pygame
from Controlador import Constantes

class Juego:
    def __init__(self, ventana):
        self.ventana = ventana
        self.reloj = pygame.time.Clock()

    def iniciar(self):
        # Aquí pondrías toda la lógica de tu juego.
        run = True
        while run:
            self.reloj.tick(Constantes.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pygame.display.update()
