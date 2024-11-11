import pygame
from pygame.examples.cursors import image

from Principal import animacion_salto


class Personaje:
    def __init__(self, x, y, animacion_quieto, animacion_movimiento, animacion_disparo_quieto, animacion_disparo_movimiento, animacion_salto):
        self.animacion_quieto = animacion_quieto
        self.animacion_movimiento = animacion_movimiento
        self.animacion_disparo_quieto = animacion_disparo_quieto
        self.animacion_disparo_movimiento = animacion_disparo_movimiento
        self.animacion_salto = animacion_salto


        self.voltear = False
        self.frames_indice_movimiento = 0
        self.frames_indice_disparo = 0
        self.frames_indice_saltos = 0
        self.actualizar_tiempo_movimiento = pygame.time.get_ticks()
        self.actualizar_tiempo_disparo = pygame.time.get_ticks()
        self.image = self.animacion_quieto[0]  # Imagen inicial, personaje quieto
        self.forma = pygame.Rect(0, 0, self.image.get_width(), self.image.get_height())
        self.forma.center = (x, y)
        self.en_movimiento = False
        self.disparando = False
        self.saltando = False
        self.velocidad_salto = -15
        self.velocidad_gravedad = 0.5
        self.salto_en_progreso = False

    # Función para mover al personaje
    def mover(self, delta_x, delta_y):
        if delta_x < 0:
            self.voltear = True  # Mover izquierda
        elif delta_x > 0:
            self.voltear = False  # Mover derecha
        # Actualiza la posición
        self.forma.x += delta_x  # Usamos self.forma.x en lugar de self.x
        self.forma.y += delta_y  # Usamos self.forma.y en lugar de self.y
        # Actualiza el estado de movimiento
        self.en_movimiento = delta_x != 0 or delta_y != 0


    def cargar_animaciones(self):
        from Principal import animacion_disparo_movimiento
        # Aquí va el código que usa animacion_disparo
        return animacion_disparo_movimiento

    def actualizar(self):
        tiempoEspera = 100
        tiempo_disparo = 80

        # Actualizar animación de movimiento
        if self.en_movimiento:
            if pygame.time.get_ticks() - self.actualizar_tiempo_movimiento >= tiempoEspera:
                self.frames_indice_movimiento = (self.frames_indice_movimiento + 1) % len(self.animacion_movimiento)
                self.actualizar_tiempo_movimiento = pygame.time.get_ticks()
            self.image = self.animacion_movimiento[self.frames_indice_movimiento]
        else:
            self.frames_indice_movimiento = 0
            self.image = self.animacion_quieto[0]  # Quieto, primer frame de la animación quieto

        # Animación de salto
        if self.salto_en_progreso:
            self.image = self.animacion_salto[self.frames_indice_salto % len(self.animacion_salto)]
            self.frames_indice_salto += 1

            # Si se han reproducido todos los frames de la animación de salto
            if self.frames_indice_salto >= len(self.animacion_salto):
                self.frames_indice_salto = 0
                self.salto_en_progreso = False

        # Actualizar animación de disparo
        if self.disparando:
            if pygame.time.get_ticks() - self.actualizar_tiempo_disparo >= tiempo_disparo:
                self.frames_indice_disparo += 1
                self.actualizar_tiempo_disparo = pygame.time.get_ticks()

            # Selecciona la animación de disparo dependiendo si está en movimiento o no
            if self.en_movimiento:
                self.image = self.animacion_disparo_movimiento[
                    self.frames_indice_disparo % len(self.animacion_disparo_movimiento)]
            else:
                self.image = self.animacion_disparo_quieto[
                    self.frames_indice_disparo % len(self.animacion_disparo_quieto)]

            if self.frames_indice_disparo >= len(self.animacion_disparo_quieto):
                self.frames_indice_disparo = 0
                self.disparando = False

    def saltar(self):
        if not self.salto_en_progreso:
            self.salto_en_progreso = True
            self.frames_indice_salto = 0

    def draw(self, ventana):
        voltear_imagen = pygame.transform.flip(self.image, self.voltear, False)
        ventana.blit(voltear_imagen, self.forma)

         # Si el personaje está disparando, lo dibujamos
        if self.disparando:
            # Si está disparando mientras se mueve, usamos la animacion de disparo en movimiento
            if self.en_movimiento:
                imagen_disparo = self.animacion_disparo_movimiento[self.frames_indice_disparo]
            else:
                # Si está quieto, usamos la animacion pero quieto
                imagen_disparo = self.animacion_disparo_quieto[self.frames_indice_disparo]

            voltear_imagen_disparo = pygame.transform.flip(imagen_disparo, self.voltear, False)
            ventana.blit(voltear_imagen_disparo, self.forma)

    def disparar(self):
        if not self.disparando:
            self.disparando = True
            self.frames_indice_disparo = 0
