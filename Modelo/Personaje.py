import pygame

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
        self.forma.x += delta_x  # Usamos self.forma.x en lugar de self.x
        self.forma.y += delta_y  # Usamos self.forma.y en lugar de self.y
        # Actualiza el estado de movimiento
        self.en_movimiento = delta_x != 0 or delta_y != 0


    def cargar_animaciones(self):
        from Vista.Principal import animacion_disparo_movimiento
        # Aquí va el código que usa animacion_disparo
        return animacion_disparo_movimiento


    def actualizar(self):
        # Variables de tiempo
        tiempoEspera = 100
        tiempo_disparo = 125

        # Comprobamos que la lista de animación de movimiento no esté vacía
        if len(self.animacion_movimiento) > 0:
            # Actualizar animación de movimiento solo si el personaje está en movimiento
            if self.en_movimiento:
                # Si ha pasado el tiempo necesario para cambiar el frame de la animación
                if pygame.time.get_ticks() - self.actualizar_tiempo_movimiento >= tiempoEspera:
                    # Actualizamos el índice del frame para la animación de movimiento
                    self.frames_indice_movimiento = (self.frames_indice_movimiento + 1) % len(self.animacion_movimiento)
                    self.actualizar_tiempo_movimiento = pygame.time.get_ticks()
                self.image = self.animacion_movimiento[
                    self.frames_indice_movimiento]  # Establecemos la imagen de la animación
            else:
                # Si no está en movimiento, mostramos el primer frame de la animación de "quieto"
                self.frames_indice_movimiento = 0
                self.image = self.animacion_quieto[0]
        else:
            # Si no hay animaciones de movimiento, mostramos el primer frame de la animación de "quieto"
            self.frames_indice_movimiento = 0
            self.image = self.animacion_quieto[0]

        # Animación de disparo
        if self.disparando:
            if pygame.time.get_ticks() - self.actualizar_tiempo_disparo >= tiempo_disparo:
                self.frames_indice_disparo += 1
                self.actualizar_tiempo_disparo = pygame.time.get_ticks()

            # Selecciona la animación de disparo dependiendo si está en movimiento o no
            if self.en_movimiento:
                if len(self.animacion_disparo_movimiento) > 0:
                    self.image = self.animacion_disparo_movimiento[
                        self.frames_indice_disparo % len(self.animacion_disparo_movimiento)]
            else:
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
        if not self.disparando:
            self.disparando = True
            self.frames_indice_disparo = 0