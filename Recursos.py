import pygame
from Controlador.Constantes import ESCALA_BALA

def escalar_imagen(image, scale):
    w = image.get_width()
    h = image.get_height()
    return pygame.transform.scale(image, (w * scale, h * scale))

# Imagen de la bala (cargada una vez para todos)
IMAGEN_BALA = escalar_imagen(pygame.image.load(f"assets//images//character//player//player-shoott.png"), ESCALA_BALA)

balas = pygame.sprite.Group()