import pygame

from Controlador import Constantes

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, x, y, animacion_moverse, direccion):
        # Animacion de movimiento
        self.x = x
        self.y = y
        self.animacion_moverse = animacion_moverse
        self.imagen_actual = self.animacion_moverse[0]
        self.rect = self.imagen_actual.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.frame = 0
        self.direccion = direccion

    def mover(self):
        # El enemigo se mueve hacia el jugador
        self.x -= Constantes.VELOCIDAD_ENEMIGO # Se mueve a la izquierda
        self.rect.x = self.x # Actualizamos la posicion del enemigo

    def actualizar(self):
        self.frame += 0.1 # Cambiar el valor para ajustar la velocidad de la animación
        if self.frame >= len(self.animacion_moverse):
            self.frame = 0
        self.imagen_actual = self.animacion_moverse[int(self.frame)]

    def draw(self, ventana):
        ventana.blit(self.imagen_actual, self.rect)