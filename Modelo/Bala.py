import pygame

from Controlador import Constantes
from Recursos import IMAGEN_BALA, balas

# Clase Bala
class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y, direccion):
        super().__init__()  # Inicializa el sprite

        self.x = x
        self.y = y
        self.direccion = direccion
        self.image = IMAGEN_BALA  # Asegúrate de que imagen_bala esté cargada
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        # Agregar al grupo de balas automáticamente
        balas.add(self)

    def update(self):
        # Actualizar la posición de la bala según su dirección
        if self.direccion == "derecha":
            self.rect.x += 10  # Mueve la bala a la derecha
        elif self.direccion == "izquierda":
            self.rect.x -= 10  # Mueve la bala a la izquierda

        # Eliminar la bala si sale de la pantalla
        if self.rect.right < 0 or self.rect.left > Constantes.ANCHO_VENTANA:
            self.kill()
