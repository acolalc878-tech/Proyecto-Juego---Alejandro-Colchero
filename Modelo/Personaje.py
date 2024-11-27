import pygame

from Controlador import Constantes
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
        self.actualizar_tiempo_movimiento = pygame.time.get_ticks()
        self.actualizar_tiempo_disparo = pygame.time.get_ticks()

        # Inicializamos 'rect', que es donde se define la posición y tamaño del personaje
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
        self.rect.x += delta_x
        self.rect.y += delta_y

        # Evitar que el personaje salga de la pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > Constantes.ANCHO_VENTANA:
            self.rect.right = Constantes.ANCHO_VENTANA
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > Constantes.ALTO_VENTANA:
            self.rect.bottom = Constantes.ALTO_VENTANA

# --------------------------------------------------------------------------------------------------------------------------------

    def cargar_animaciones(self):
        # Debería retornar las animaciones cargadas
        return self.animacion_disparo_movimiento

# --------------------------------------------------------------------------------------------------------------------------------

    def actualizar_animacion(self):
        # Control de animación según el estado
        tiempo_actual = pygame.time.get_ticks()

        # Cambiar animaciones según la acción
        if self.direccion == "izquierda" or self.direccion == "derecha":
            if tiempo_actual - self.last_update > self.frame_duration:
                self.last_update = tiempo_actual
                self.frame_index = (self.frame_index + 1) % len(self.animacion_movimiento)
                self.image = self.animacion_movimiento[self.frame_index]
        elif self.direccion == "disparando":
            if tiempo_actual - self.last_update > self.frame_duration:
                self.last_update = tiempo_actual
                self.frame_index = (self.frame_index + 1) % len(self.animacion_disparo_movimiento)
                self.image = self.animacion_disparo_movimiento[self.frame_index]
        else:  # Animación por defecto (quieto)
            self.image = self.animacion_quieto[0]

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
