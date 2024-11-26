import pygame
from Modelo.Bala import Bala
from Recursos import balas

class Personaje:
    def __init__(self, x, y, animacion_quieto, animacion_movimiento, animacion_disparo_quieto, animacion_disparo_movimiento):
        self.animacion_quieto = animacion_quieto
        self.animacion_movimiento = animacion_movimiento
        self.animacion_disparo_quieto = animacion_disparo_quieto
        self.animacion_disparo_movimiento = animacion_disparo_movimiento

        self.voltear = False
        self.frames_indice_movimiento = 0
        self.frames_indice_disparo = 0
        self.actualizar_tiempo_movimiento = pygame.time.get_ticks()
        self.actualizar_tiempo_disparo = pygame.time.get_ticks()
        self.image = self.animacion_quieto[0]
        self.forma = pygame.Rect(0, 0, self.image.get_width(), self.image.get_height())
        self.forma.center = (x, y)
        self.en_movimiento = False
        self.disparando = False


    # Función para mover al personaje
    def mover(self, delta_x, delta_y):
        if delta_x < 0:
            self.voltear = True  # Mover izquierda
        elif delta_x > 0:
            self.voltear = False  # Mover derecha
        # Actualiza la posición
        self.forma.x += delta_x
        self.forma.y += delta_y
        # Actualiza el estado de movimiento
        self.en_movimiento = delta_x != 0 or delta_y != 0


    def cargar_animaciones(self):
        from Vista.Principal import animacion_disparo_movimiento
        return animacion_disparo_movimiento

    def actualizar(self):
        # Variables de tiempo
        tiempoEspera = 100
        tiempo_disparo = 125

        # Animación de movimiento
        if self.en_movimiento:
            if pygame.time.get_ticks() - self.actualizar_tiempo_movimiento >= tiempoEspera:
                self.frames_indice_movimiento = (self.frames_indice_movimiento + 1) % len(self.animacion_movimiento)
                self.actualizar_tiempo_movimiento = pygame.time.get_ticks()
            self.image = self.animacion_movimiento[self.frames_indice_movimiento]
        else:
            self.image = self.animacion_quieto[0]

        # Animación de disparo
        if self.disparando:
            if pygame.time.get_ticks() - self.actualizar_tiempo_disparo >= tiempo_disparo:
                self.frames_indice_disparo += 1
                self.actualizar_tiempo_disparo = pygame.time.get_ticks()

            # Si está en movimiento, usa la animación de disparo en movimiento
            if self.en_movimiento:
                if len(self.animacion_disparo_movimiento) > 0:
                    self.image = self.animacion_disparo_movimiento[
                        self.frames_indice_disparo % len(self.animacion_disparo_movimiento)]
            else:
                # Si no está en movimiento, usa la animación de disparo quieto
                if len(self.animacion_disparo_quieto) > 0:
                    self.image = self.animacion_disparo_quieto[
                        self.frames_indice_disparo % len(self.animacion_disparo_quieto)]

            if self.frames_indice_disparo >= len(self.animacion_disparo_quieto):
                self.frames_indice_disparo = 0
                self.disparando = False


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
        self.disparando = True
        if self.voltear:
            bala = Bala(self.forma.left, self.forma.centery, "izquierda")
        else:
            bala = Bala(self.forma.right, self.forma.centery, "derecha")
        balas.add(bala)
