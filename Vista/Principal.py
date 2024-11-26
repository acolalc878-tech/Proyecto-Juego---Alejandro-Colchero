import random

import pygame
from Controlador import Constantes
from Controlador.Constantes import VELOCIDAD_ENEMIGO
from Modelo.Bala import Bala
from Modelo.Enemigo import Enemigo
from Modelo.Personaje import Personaje
from Recursos import escalar_imagen, balas

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ventana = pygame.display.set_mode((Constantes.ANCHO_VENTANA, Constantes.ALTO_VENTANA))
pygame.display.set_caption("ASTRO SLAYER")

# Lista de enemigos
enemigos = []

#--------------------------------------------------------------------------------------------------------------------------------

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

#--------------------------------------------------------------------------------------------------------------------------------

def animacion_bala():
   return escalar_imagen(pygame.image.load(f"assets//images//character//player//player-shoott.png"), 0.5)

bala = Bala(jugador.rect.right, jugador.rect.centery, "derecha")

#--------------------------------------------------------------------------------------------------------------------------------


# Cargar animaciones de los enemigos
def carga_animacion_enemigo_1():
    animacion_movimiento_enemigo = [
        escalar_imagen(pygame.image.load(f"assets//images//character//enemies//cangrejo//crab-walk{i}.png"),
                       Constantes.ESCALA_ENEMIGO) for i in range(6)]  # Animación de caminar del enemigo

    return animacion_movimiento_enemigo

# Cargar las animaciones de enemigos
animacion_movimiento_enemigo = carga_animacion_enemigo_1()

#--------------------------------------------------------------------------------------------------------------------------------


# Cargar animaciones enemigo 2
def carga_animacion_enemigo_2():
    animacion_movimiento_enemigo_2 = [
        escalar_imagen(pygame.image.load(f"assets//images//character//enemies//ojo volador//fly-eye{i}.png"),
                       Constantes.ESCALA_ENEMIGO) for i in range(4)]

    return animacion_movimiento_enemigo_2

# Cargar las animaciones de enemigos
animacion_movimiento_enemigo_2 = carga_animacion_enemigo_2()

# Crear a los enemigos
enemigos = pygame.sprite.Group()  # Crear el grupo de enemigos

# Variables del juego
mover_arriba = mover_abajo = mover_derecha = mover_izquierda = False
reloj = pygame.time.Clock()


#--------------------------------------------------------------------------------------------------------------------------------


# Función para cargar música de fondo
def musica_fondo():
    try:
        pygame.mixer.music.load("assets/music/musica.mp3")  # Cambia esta ruta a la correcta de tu archivo de música
        pygame.mixer.music.set_volume(0.5)  # Ajustar el volumen
        pygame.mixer.music.play(-1, 0.0)  # Reproducir música en bucle
        print("Música cargada y reproduciéndose")
    except pygame.error as e:
        print(f"Error al cargar la música: {e}")


#--------------------------------------------------------------------------------------------------------------------------------


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


#--------------------------------------------------------------------------------------------------------------------------------


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
            if pygame.key.get_pressed()[pygame.K_e]:
                jugador.disparar()  # Activar la animación de disparo
            if pygame.key.get_pressed()[pygame.K_r]:
                jugador = Personaje(350, 320)

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


#--------------------------------------------------------------------------------------------------------------------------------


# Variable global para controlar el tiempo de aparición de enemigos
enemigos_aparicion_tiempo = pygame.time.get_ticks()


# Función para generar los enemigos
def generar_enemigos():
    global enemigos_aparicion_tiempo

    # Generar enemigos cada 2 segundos
    if pygame.time.get_ticks() - enemigos_aparicion_tiempo >= 2000:
        # Generar el primer enemigo (ojo volador) desde el borde izquierdo
        if random.choice([True, False]):
            x_izquierda = -100  # Fuera de la pantalla a la izquierda
            y_izquierda = random.randint(0, Constantes.ALTO_VENTANA)
            enemigo_izquierda = Enemigo(x_izquierda, y_izquierda, animacion_movimiento_enemigo, VELOCIDAD_ENEMIGO, "derecha")
            enemigos.add(enemigo_izquierda)

        # Generar el segundo enemigo (Cangrejo) desde el borde derecho
        if not random.choice([True, False]):
            x_derecha = Constantes.ANCHO_VENTANA + 100  # Fuera de la pantalla a la derecha
            y_derecha = random.randint(0, Constantes.ALTO_VENTANA)
            enemigo_derecha = Enemigo(x_derecha, y_derecha, animacion_movimiento_enemigo_2, VELOCIDAD_ENEMIGO, "izquierda")
            enemigos.add(enemigo_derecha)

        # Actualizar el tiempo de aparición
        enemigos_aparicion_tiempo = pygame.time.get_ticks()


#--------------------------------------------------------------------------------------------------------------------------------

def pantalla_game_over(ventana):
    fuente = pygame.font.Font("fuentes//Pixel Times.ttf", 70)

    texto_game_over= fuente.render("GAMER OVER", True, (255,0,0))
    ventana.blit(texto_game_over, (
             Constantes.ANCHO_VENTANA // 2 - texto_game_over.get_width() // 2, Constantes.ALTO_VENTANA // 2 - texto_game_over.get_height() // 2))

    texto_reiniciar = fuente.render("Presione R para reiniciar", True, (255,255,255))
    ventana.blit(texto_reiniciar, (
    Constantes.ANCHO_VENTANA // 2 - texto_reiniciar.get_width() // 2, Constantes.ALTO_VENTANA // 2 + 100))


#--------------------------------------------------------------------------------------------------------------------------------

def colisiones(self, enemigos):
    for enemigo in enemigos:
        if self.rect.colliderect(enemigo.rect):
            self.game_over = True
            break

#--------------------------------------------------------------------------------------------------------------------------------


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

    enemigos.update()

    # Mover y dibujar enemigos
    for enemigo in enemigos:
        enemigo.actualizar()
        enemigo.draw(ventana)

    jugador.colisiones(enemigos)

    if jugador.game_over:
        pantalla_game_over(ventana)
        pygame.display.flip()

        key= pygame.key.get_pressed()
        if keys[py]

    balas.update()
    balas.draw(ventana)

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
