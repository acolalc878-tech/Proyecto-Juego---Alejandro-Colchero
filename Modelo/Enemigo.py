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

    def actualizar(self):
        if self.direccion == "derecha":
            self.rect.x += self.velocidad
        elif self.direccion == "izquierda":
            self.rect.x -= self.velocidad

        now = pygame.time.get_ticks()
        if now - self.last_update >= self.frame_duration:
            # Ha pasado el tiempo suficiente para cambiar de frame
            self.frame_index = (self.frame_index + 1) % len(self.animacion)  # Cicla entre los frames
            self.image = self.animacion[self.frame_index]  # Cambia la imagen actual
            self.last_update = now  # Actualiza el tiempo de la última actualizacióaaaaa

    def draw(self, ventana):
        ventana.blit(self.image, self.rect)
