import pygame

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, x, y, animacion, velocidad, direccion):
        super().__init__()
        self.x = x
        self.y = y
        self.animacion = animacion  # Lista de imágenes para la animación
        self.velocidad = velocidad
        self.direccion = direccion
        self.image = animacion[0]  # Suponemos que animacion es una lista de imágenes
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Variables para las animaciones del enemigo
        self.frame_index = 0
        self.last_update = pygame.time.get_ticks()  # Tiempo de la última actualización de la animación
        self.frame_duration = 100


    def destruir(self):
        self.kill()  # Eliminar el enemigo de los grupos

    def actualizar(self):
        # Actualizar la posición
        if self.direccion == "derecha":
            self.rect.x += self.velocidad
        elif self.direccion == "izquierda":
            self.rect.x -= self.velocidad

        # Actualizar la animación
        now = pygame.time.get_ticks()
        if now - self.last_update >= self.frame_duration:
            # Ha pasado el tiempo suficiente para cambiar de frame
            self.frame_index = (self.frame_index + 1) % len(self.animacion)  # Cicla entre los frames
            self.image = self.animacion[self.frame_index]  # Cambia la imagen actual
            self.last_update = now  # Actualiza el tiempo de la última actualización

    def draw(self, ventana):
        ventana.blit(self.image, self.rect)

    def colision_jugador(self, jugador):
        # Colisión con el jugador
        if self.rect.colliderect(jugador.rect):
            jugador.recibir_dano()  # El jugador recibe daño
            self.recibir_dano()  # El enemigo recibe daño
            return True
        return False

    def colision_bala(self, bala):
        # Colisión con una bala
        if self.rect.colliderect(bala.rect):
            self.recibir_dano()  # El enemigo recibe daño
            bala.kill()  # La bala se destruye después de la colisión
            return True
        return False

    def recibir_dano(self):
        self.destruir()
