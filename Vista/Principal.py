import random

import pygame

from Modelo.Enemigo import Enemigo
from Modelo.Personaje import Personaje
from Controlador import Constantes

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ventana = pygame.display.set_mode((Constantes.ANCHO_VENTANA, Constantes.ALTO_VENTANA))
pygame.display.set_caption("ASTRO SLAYER")


# Cargar imágenes
def escalar_imagen(image, scale):
    w = image.get_width()
    h = image.get_height()
    return pygame.transform.scale(image, (w * scale, h * scale))


# Cargar animaciones del jugador
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

# Cargar las animaciones del jugador
animacion_quieto, animacion_movimiento, animacion_disparo_quieto, animacion_disparo_movimiento = cargar_animaciones()

# Crear al jugador
jugador = Personaje(350, 320, animacion_quieto, animacion_movimiento, animacion_disparo_quieto,
                    animacion_disparo_movimiento)


# Cargar animaciones de los enemigos
def cargar_animaciones_enemigos():
    animacion_movimiento_enemigo = [
        escalar_imagen(pygame.image.load(f"assets//images//character//enemies//cangrejo//crab-walk{i}.png"),
                       Constantes.ESCALA_ENEMIGO) for i in range(6)]  # Animación de caminar del enemigo

    animacion_movimiento_enemigo_2 = [
        escalar_imagen(pygame.image.load(f"assets//images//character//enemies//ojo volador//fly-eye{i}.png"),
                       Constantes.ESCALA_ENEMIGO) for i in range(4)]

    return animacion_movimiento_enemigo, animacion_movimiento_enemigo_2


# Cargar las animaciones de enemigos
animacion_movimiento_enemigo, animacion_movimiento_enemigo_2 = cargar_animaciones_enemigos()

# Crear a los enemigos
enemigos = pygame.sprite.Group()  # Agrupamos a todos los enemigos


# Cargar animaciones enemigo 2



# Variables del juego
mover_arriba = mover_abajo = mover_derecha = mover_izquierda = False
reloj = pygame.time.Clock()


# Lista de enemigos
enemigos = []


# Función para cargar música de fondo
def musica_fondo():
    try:
        pygame.mixer.music.load("assets/music/musica.mp3")  # Cambia esta ruta a la correcta de tu archivo de música
        pygame.mixer.music.set_volume(0.5)  # Ajustar el volumen
        pygame.mixer.music.play(-1, 0.0)  # Reproducir música en bucle
        print("Música cargada y reproduciéndose")
    except pygame.error as e:
        print(f"Error al cargar la música: {e}")


# Función para cargar el fondo
def cargar_fondo():
    try:
        fondo = pygame.image.load("assets/images/fondo/suelo-astroslayer.jpg")  # Cambia esta ruta si es necesario
        fondo = pygame.transform.scale(fondo, (
        Constantes.ANCHO_VENTANA, Constantes.ALTO_VENTANA))  # Escalar el fondo a toda la pantalla
        return fondo
    except pygame.error as e:
        print(f"Error al cargar el fondo: {e}")
        return None

# Cargamos el fondo
fondo = cargar_fondo()

# Reproducir música de fondo
musica_fondo()



# Función para manejar los eventos
def manejar_eventos():
    global mover_izquierda, mover_derecha, mover_arriba, mover_abajo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
                jugador.direccion = "izquierda"  # Actualiza la dirección del jugador
            if event.key == pygame.K_d:
                mover_derecha = True
                jugador.direccion = "derecha"  # Actualiza la dirección del jugador
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True
            if event.key == pygame.K_e:
                jugador.disparar()  # Activar la animación de disparo
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_s:
                mover_abajo = False
    return True

# Inicializamos ala variable para la aparición de enemigos
enemigos_aparicion_tiempo = pygame.time.get_ticks()

# Función para generar enemigos desde los bordes de la pantalla
def generar_enemigos():
    global enemigos_aparicion_tiempo  # Aseguramos que la variable global se utilice

    if pygame.time.get_ticks() - enemigos_aparicion_tiempo >= 3000:  # Cada 3 segundos
        # Enemigo 1 desde la izquierda
        x_izquierda = -100  # Enemigo que aparece desde el borde izquierdo
        y_izquierda = random.randint(0, Constantes.ALTO_VENTANA)
        enemigo_izquierda = Enemigo(x_izquierda, y_izquierda, animacion_movimiento_enemigo, "derecha")

        # Enemigo 2 desde la derecha
        x_derecha = Constantes.ANCHO_VENTANA + 100  # Enemigo que aparece desde el borde derecho
        y_derecha = random.randint(0, Constantes.ALTO_VENTANA)
        enemigo_derecha = Enemigo(x_derecha, y_derecha, animacion_movimiento_enemigo_2, "izquierda")

        # Agregar los enemigos a la lista de enemigos
        enemigos.append(enemigo_izquierda)
        enemigos.append(enemigo_derecha)

        # Actualizar el tiempo de aparición de enemigos
        enemigos_aparicion_tiempo = pygame.time.get_ticks()


# Bucle principal del juego
run = True
while run:
    reloj.tick(Constantes.FPS)

    # Rellenar la ventana con el fondo (si se cargó correctamente)
    ventana.fill(Constantes.COLOR_FONDO)
    if fondo:  # Solo dibujar el fondo si se cargó correctamente
        ventana.blit(fondo, (0, 0))  # Dibujar fondo en la ventana

    # Manejo de eventos
    run = manejar_eventos()

    # Generar enemigos aleatorios
    generar_enemigos()

    # Mover y dibujar enemigos
    for enemigo in enemigos[:]: # Iterar sobre una copia de la lista para evitar modificarla mientras la recorres
        enemigo.mover()
        enemigo.actualizar()
        enemigo.draw(ventana)

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

    # Dibujar al jugador
    jugador.draw(ventana)

    # Actualizar la pantalla
    pygame.display.update()

# Salir de Pygame
pygame.quit()
