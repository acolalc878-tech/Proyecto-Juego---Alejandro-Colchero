import pygame
from Modelo.Bala import Bala
from Recursos import balas

class Personaje:
    def __init__(self, x, y, animacion_quieto, animacion_movimiento, animacion_disparo_quieto, animacion_disparo_movimiento):
        # Animaciones
        self.animacion_quieto = animacion_quieto
        self.animacion_movimiento = animacion_movimiento
        self.animacion_disparo_quieto = animacion_disparo_quieto
        self.animacion_disparo_movimiento = animacion_disparo_movimiento

        self.voltear = False  # Controla la dirección de la imagen (mirar a la izquierda o derecha)
        self.frames_indice_movimiento = 0  # Índice para animación de movimiento
        self.frames_indice_disparo = 0  # Índice para animación de disparo
        self.actualizar_tiempo_movimiento = pygame.time.get_ticks()  # Última vez que se actualizó la animación
        self.actualizar_tiempo_disparo = pygame.time.get_ticks()

        # Inicializa 'rect' aquí, que es donde se define la posición y tamaño del personaje
        self.image = self.animacion_quieto[0]
        self.rect = self.image.get_rect()  # Crea el rectángulo a partir de la imagen
        self.rect.center = (x, y)  # Inicializa el centro del personaje en las coordenadas (x, y)

        # Estados de movimiento y disparo
        self.en_movimiento = False
        self.disparando = False

        self.vida = 3  # Vida del personaje
        self.direccion = "derecha"

        self.colisiones_con_enemigos = 0  # Contador de colisiones con enemigos
        self.muerto = False  # Estado del personaje (si está muerto o no)

# --------------------------------------------------------------------------------------------------------------------------------

    def mover(self, delta_x, delta_y):
        if delta_x < 0:
            self.voltear = True  # Mover izquierda
        elif delta_x > 0:
            self.voltear = False  # Mover derecha
        self.rect.x += delta_x
        self.rect.y += delta_y
        self.en_movimiento = delta_x != 0 or delta_y != 0

# --------------------------------------------------------------------------------------------------------------------------------

    def cargar_animaciones(self):
        # Debería retornar las animaciones cargadas
        return self.animacion_disparo_movimiento

# --------------------------------------------------------------------------------------------------------------------------------

    def actualizar(self):
        if self.muerto:
            return  # Si está muerto, no actualiza más

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

            if self.en_movimiento:
                if len(self.animacion_disparo_movimiento) > 0:
                    self.image = self.animacion_disparo_movimiento[ self.frames_indice_disparo % len(self.animacion_disparo_movimiento)]
            else:
                if len(self.animacion_disparo_quieto) > 0:
                    self.image = self.animacion_disparo_quieto[ self.frames_indice_disparo % len(self.animacion_disparo_quieto)]

            if self.frames_indice_disparo >= len(self.animacion_disparo_quieto):
                self.frames_indice_disparo = 0
                self.disparando = False

# --------------------------------------------------------------------------------------------------------------------------------

    def draw(self, ventana):
        if self.muerto:
            return

        voltear_imagen = pygame.transform.flip(self.image, self.voltear, False)
        ventana.blit(voltear_imagen, self.rect)

# --------------------------------------------------------------------------------------------------------------------------------

    def disparar(self):
        self.disparando = True
        if self.voltear:
            # Aquí cambiamos 'forma' por 'rect'
            bala = Bala(self.rect.left, self.rect.centery, "izquierda")
        else:
            # Aquí cambiamos 'forma' por 'rect'
            bala = Bala(self.rect.right, self.rect.centery, "derecha")
        balas.add(bala)


# --------------------------------------------------------------------------------------------------------------------------------

    def colisiones(self, enemigos):
        for enemigo in enemigos:
            if self.rect.colliderect(enemigo.rect):  # Verifica si el jugador toca al enemigo
                self.vida -= 1  # El jugador pierde vida al tocar al enemigo
                if self.vida <= 0:
                    self.muerto = True  # El jugador muere después de 3 colisiones
                    break  # Termina el ciclo de colisiones si el jugador muere

                enemigo.destruir()


    def recibir_danio(self):
        self.vida -= 1
        if self.vida <= 0:
            self.muerto = True  # El personaje muere si su vida llega a 0
