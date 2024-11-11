from Modelo.Personaje import Personaje
import pygame
import Constantes


# Inicializar Pygame y crear la ventana
pygame.init()
ventana = pygame.display.set_mode((Constantes.ANCHO_VENTANA, Constantes.ALTO_VENTANA))
pygame.display.set_caption("Videojuego por turnos")


# Fuente
font = pygame.font.Font(None, 74)

texto_iniciar = font.render("Jugar", True, Constantes.WHITE)
texto_salir = font.render("Salir", True, Constantes.WHITE)


# Posición de las opciones
play = texto_iniciar.get_rect(center=(Constantes.ANCHO_VENTANA // 2, Constantes.ALTO_VENTANA // 2 - 50))
salir = texto_salir.get_rect(center=(Constantes.ANCHO_VENTANA // 2, Constantes.ALTO_VENTANA // 2 + 50))


# Escalar imágenes
def escalar_imagen(image, scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image, (w * scale, h * scale))
    return nueva_imagen


# Cargamos las animaciones
animacion_quieto = []
animacion_movimiento = []
animacion_disparo_movimiento = []
animacion_disparo_quieto = []

animacion_salto= []


# Frame salto
for i in range(2):
    img = pygame.image.load(f"assets//images//character//player//player-jump{i}.png")
    img = escalar_imagen(img, Constantes.TAMANIO_PERSONAJE)
    animacion_salto.append(img)


# Frame quieto
for i in range(1):
    img = pygame.image.load(f"assets//images//character//player//player-idle{i}.png")
    img = escalar_imagen(img, Constantes.TAMANIO_PERSONAJE)
    animacion_quieto.append(img)


# Frames de movimiento
for i in range(6):
    img = pygame.image.load(f"assets//images//character//player//player-run{i}.png")
    img = escalar_imagen(img, Constantes.TAMANIO_PERSONAJE)
    animacion_movimiento.append(img)


# Frames de disparo cuando está quieto
for i in range(3):
    img = pygame.image.load(f"assets//images//character//player//player-shoot{i}.png")
    img = escalar_imagen(img, Constantes.TAMANIO_PERSONAJE)
    animacion_disparo_quieto.append(img)


# Frames de disparo mientras se mueve
for i in range(6):
    img = pygame.image.load(f"assets//images//armas//player-run-shoott{i}.png")
    img = escalar_imagen(img, Constantes.TAMANIO_PERSONAJE)
    animacion_disparo_movimiento.append(img)

altura_personaje = animacion_movimiento[0].get_height()


# Calculamos la posición inicial en la esquina inferior izquierda
posicion_inicial_x = 0
posicion_inicial_y = Constantes.ALTO_VENTANA - altura_personaje


# Crear el jugador con la posición inicial en la esquina inferior izquierda
jugador = Personaje(
    posicion_inicial_x,
    posicion_inicial_y,
    animacion_quieto,  # Animación cuando está quieto
    animacion_movimiento,  # Animación cuando se mueve
    animacion_disparo_quieto,  # Animación de disparo cuando está quieto
    animacion_disparo_movimiento  # Animación de disparo cuando se mueve
)


# Variables de movimiento y FPS
mover_arriba = mover_abajo = mover_derecha = mover_izquierda = False
reloj = pygame.time.Clock()


# Bucle principal del juego
run = True
while run:
    reloj.tick(Constantes.FPS)
    ventana.fill(Constantes.COLOR_FONDO)

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

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
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
            if event.key == pygame.K_SPACE:
                jugador.saltar()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_s:
                mover_abajo = False

    pygame.display.update()

pygame.quit()
