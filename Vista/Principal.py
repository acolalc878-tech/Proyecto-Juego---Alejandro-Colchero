from Modelo.Personaje import Personaje
import pygame
from Controlador import Constantes

# Inicializar Pygame y crear la ventana
pygame.init()
ventana = pygame.display.set_mode((Constantes.ANCHO_VENTANA, Constantes.ALTO_VENTANA))
pygame.display.set_caption("Videojuego por turnos")

# Escalar imágenes
def escalar_imagen(image, scale):
    w = image.get_width()
    h = image.get_height()
    return pygame.transform.scale(image, (w * scale, h * scale))

# Función para cargar las animaciones
def cargar_animaciones():
    animacion_quieto = [escalar_imagen(pygame.image.load(f"assets//images//character//player//player-idle{i}.png"),
                                       Constantes.ESCALA_PERSONAJE) for i in range(1)]
    animacion_movimiento = [escalar_imagen(pygame.image.load(f"assets//images//character//player//player-run{i}.png"),
                                           Constantes.ESCALA_PERSONAJE) for i in range(6)]
    animacion_disparo_quieto = [
        escalar_imagen(pygame.image.load(f"assets//images//character//player//player-shoot{i}.png"),
                       Constantes.ESCALA_PERSONAJE) for i in range(3)]
    animacion_disparo_movimiento = [
        escalar_imagen(pygame.image.load(f"assets//images//armas//player-run-shoott{i}.png"),
                       Constantes.ESCALA_PERSONAJE) for i in range(6)]
    return animacion_quieto, animacion_movimiento, animacion_disparo_quieto, animacion_disparo_movimiento


# Cargamos las animaciones
animacion_quieto, animacion_movimiento, animacion_disparo_quieto, animacion_disparo_movimiento = cargar_animaciones()


# Posición inicial
posicion_inicial_x, posicion_inicial_y = 350, 320


# Creamos al personaje
jugador = Personaje (
    posicion_inicial_x,
    posicion_inicial_y,
    animacion_quieto,
    animacion_movimiento,
    animacion_disparo_quieto,
    animacion_disparo_movimiento
)

# Variables de movimiento y FPS
mover_arriba = mover_abajo = mover_derecha = mover_izquierda = False
estado_movimiento = {
    'izquierda': False,
    'derecha': False,
    'arriba': False,
    'abajo': False
}
reloj = pygame.time.Clock()


# Función para manejar eventos
def manejar_eventos():
    global mover_izquierda, mover_derecha, mover_arriba, mover_abajo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True
            if event.key == pygame.K_e:
                jugador.disparar()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_s:
                mover_abajo = False
    return True  # Continuar el juego

# Bucle principal del juego
run = True
while run:
    reloj.tick(Constantes.FPS)
    ventana.fill(Constantes.COLOR_FONDO)

    # Manejo de eventos
    run = manejar_eventos()

    # Movimiento del jugador
    delta_x = delta_y = 0
    if mover_derecha:
        delta_x = Constantes.VELOCIDAD_PERSONAJE
    if mover_izquierda:
        delta_x = -Constantes.VELOCIDAD_PERSONAJE
    if mover_arriba:
        delta_y = -Constantes.VELOCIDAD_PERSONAJE
    if mover_abajo:
        delta_y = Constantes.VELOCIDAD_PERSONAJE

    jugador.mover(delta_x, delta_y)
    jugador.actualizar()
    jugador.draw(ventana)

    pygame.display.update()

pygame.quit()
