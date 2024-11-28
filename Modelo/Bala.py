import pygame

from Recursos import IMAGEN_BALA, balas
from Controlador import Config

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
                enemigos.remove(enemigo)
                self.kill()
                self.reproducir_impacto()
                Config.puntuacion += 10
                break

    def dibujar(self, ventana):
        # Dibuja la bala en la ventana
        ventana.blit(self.image, self.rect)

    def reproducir_impacto(self):
        sonido_impacto = pygame.mixer.Sound("assets//music//impacto-bala.mp3")
        sonido_impacto.play()