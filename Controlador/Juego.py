import pygame
from Modelo.Personaje import Personaje
from Modelo.Bala import Bala
from Modelo.Enemigo import Enemigo
from Controlador import Constantes

class Juego:
    def __init__(self, ventana):
        self.ventana = ventana
        self.reloj = pygame.time.Clock()

    def iniciar(self):
        run = True
        while run:
            self.reloj.tick(Constantes.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False  # Termina el juego
            pygame.display.update()