import pygame

from Controlador import Constantes
from Modelo.Bala import Bala


class Personaje:
    def __init__(self, x, y, animacion_quieto, animacion_movimiento, animacion_disparo_quieto, animacion_disparo_movimiento):
        # Animaciones
        self.animacion_quieto = animacion_quieto
        self.animacion_movimiento = animacion_movimiento
        self.animacion_disparo_quieto = animacion_disparo_quieto
        self.animacion_disparo_movimiento = animacion_disparo_movimiento

        self.image = self.animacion_quieto[0]
        self.rect = self.image.get_rect(center=(x, y))
        self.rect.center = (x, y)

        # Estados
        self.en_movimiento = False
        self.disparando = False
        self.voltear = False  # Controla si la imagen debe voltear horizontalmente
        self.muerto = False
        self.vida = 3
        self.direccion = "derecha"  # Dirección inicial: "derecha" o "izquierda"

        # Índices y tiempos para animaciones
        self.frames_indice_movimiento = 0
        self.frames_indice_disparo = 0
        self.actualizar_tiempo_movimiento = pygame.time.get_ticks()
        self.actualizar_tiempo_disparo = pygame.time.get_ticks()

        # Balas
        self.balas = pygame.sprite.Group()
        self.puntos = 0

# --------------------------------------------------------------------------------------------------------------------------------

    def mover(self, delta_x, delta_y):
        self.rect.x += delta_x
        self.rect.y += delta_y

        # Detectar dirección horizontal y actualizar el estado
        if delta_x < 0:  # Moviéndose a la izquierda
            if self.direccion != "izquierda":  # Cambiar dirección si es diferente
                self.voltear = True
                self.direccion = "izquierda"
        elif delta_x > 0:  # Moviéndose a la derecha
            if self.direccion != "derecha":  # Cambiar dirección si es diferente
                self.voltear = False
                self.direccion = "derecha"

        # Determinar si el personaje está en movimiento
        self.en_movimiento = delta_x != 0 or delta_y != 0

        # Evitar que el personaje salga de los límites de la pantalla
        self.rect.clamp_ip(pygame.Rect(0, 0, Constantes.ANCHO_VENTANA, Constantes.ALTO_VENTANA))

# --------------------------------------------------------------------------------------------------------------------------------

    def actualizar_animacion(self):
        tiempo_actual = pygame.time.get_ticks()

        if self.disparando:  # Animación de disparo
            if tiempo_actual - self.actualizar_tiempo_disparo > 100:  # Control de tiempo de animación
                self.actualizar_tiempo_disparo = tiempo_actual
                if self.en_movimiento:  # Disparo en movimiento
                    self.frames_indice_disparo = (self.frames_indice_disparo + 1) % len(
                        self.animacion_disparo_movimiento)
                    self.image = self.animacion_disparo_movimiento[self.frames_indice_disparo]
                else:  # Disparo quieto
                    self.frames_indice_disparo = (self.frames_indice_disparo + 1) % len(self.animacion_disparo_quieto)
                    self.image = self.animacion_disparo_quieto[self.frames_indice_disparo]
        elif self.en_movimiento:  # Animación de movimiento
            if tiempo_actual - self.actualizar_tiempo_movimiento > 100:  # Control de tiempo de animación
                self.actualizar_tiempo_movimiento = tiempo_actual
                self.frames_indice_movimiento = (self.frames_indice_movimiento + 1) % len(self.animacion_movimiento)
                self.image = self.animacion_movimiento[self.frames_indice_movimiento]
        else:  # Animación quieto
            self.image = self.animacion_quieto[0]

# --------------------------------------------------------------------------------------------------------------------------------

    def draw(self, ventana):
        if self.muerto:
            return

        # Volteamos la imagen si 'voltear' es True
        if self.voltear:
            voltear_imagen = pygame.transform.flip(self.image, True, False)
            ventana.blit(voltear_imagen, self.rect)
        else:
            ventana.blit(self.image, self.rect)

# --------------------------------------------------------------------------------------------------------------------------------

    def disparar(self):
        self.disparando = True

        # Crear una bala en función de la dirección del personaje
        if self.direccion == "izquierda":
            bala = Bala(self.rect.left, self.rect.centery, "izquierda")
        else:
            bala = Bala(self.rect.right, self.rect.centery, "derecha")

        self.balas.add(bala)

# --------------------------------------------------------------------------------------------------------------------------------

    def para_disparo(self):
        self.disparando = False

# --------------------------------------------------------------------------------------------------------------------------------

    def colisiones(self, enemigos):
        global puntuacion

        for enemigo in enemigos:
            if self.rect.colliderect(enemigo.rect):  # Verifica si el jugador toca al enemigo
                self.vida -= 1  # El jugador pierde vida al tocar al enemigo
                if self.vida <= 0:
                    self.muerto = True  # El jugador muere después de 3 colisiones
                    break  # Termina el ciclo de colisiones si el jugador muere

                enemigo.destruir()

        for bala in self.balas:
            enemigos_colisionados = pygame.sprite.spritecollide(bala, enemigos, True)
            if enemigos_colisionados:
                puntuacion += 10
                bala.kill()

# --------------------------------------------------------------------------------------------------------------------------------

    def recibir_danio(self):
        self.vida -= 1
        if self.vida <= 0:
            self.muerto = True  # El personaje muere si su vida llega a 0
