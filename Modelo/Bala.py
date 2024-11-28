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

    # Función para actualizar la posición de la bala
    def mover(self, enemigos):
        # Actualizamos la posición según la dirección
        if self.direccion == "derecha":
            self.rect.x += 10
        elif self.direccion == "izquierda":
            self.rect.x -= 10
        elif self.direccion == "arriba":
            self.rect.y -= 10
        elif self.direccion == "abajo":
            self.rect.y += 10

        # Gestionar las colisiones con los enemigos
        for enemigo in enemigos:
            if self.rect.colliderect(enemigo.rect):
                self.kill()  # Destruimos la bala si colisiona con un enemigo
                enemigo.destruir()

    def dibujar(self, ventana):
        # Dibuja la bala en la ventana
        ventana.blit(self.image, self.rect)

    def colisiones(self, enemigos):
        global puntuacion

        for bala in balas:
            if pygame.sprite.spritecollide(bala, enemigos, True):  # Si la bala colisiona con un enemigo
                puntuacion += 10  # Aumentamos la puntuación en 10
                bala.kill()  # Destruir la bala tras la colisión