import pygame
from Recursos import IMAGEN_BALA, balas

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

    # Función para actualizar la posicion de la bala
    def update(self, enemigos):  # Pasamos enemigos como argumento
        # Actualizamos la posición según la dirección
        if self.direccion == "derecha":
            self.rect.x += 10  # Aumentar la posición en x para mover hacia la derecha
        elif self.direccion == "izquierda":
            self.rect.x -= 10  # Reducir la posición en x para mover hacia la izquierda
        elif self.direccion == "arriba":
            self.rect.y -= 10  # Reducir la posición en y para mover hacia arriba
        elif self.direccion == "abajo":
            self.rect.y += 10  # Aumentar la posición en y para mover hacia abajo

        # Gestionar las colisiones con los enemigos
        for enemigo in enemigos:
            if self.rect.colliderect(enemigo.rect):
                self.kill()  # Destruir la bala si colisiona con un enemigo
                enemigo.destruir()
