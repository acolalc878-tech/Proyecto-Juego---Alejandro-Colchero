import random

import pygame

from Controlador import Constantes
from Modelo.Bala import Bala
from Modelo.Enemigo import Enemigo
from Modelo.Personaje import Personaje
from Recursos import escalar_imagen
from Vista.MenuPrincipal import MenuPrincipal


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

# Cargar animaciones del primer enemigo
def carga_animacion_enemigo_1():
    animacion_movimiento_enemigo = [
        escalar_imagen(pygame.image.load(f"assets//images//character//enemies//cangrejo//crab-walk{i}.png"),
                       Constantes.ESCALA_ENEMIGO) for i in range(6)]  # Animación de caminar del enemigo

    return animacion_movimiento_enemigo

# Cargar las animaciones de enemigos
animacion_movimiento_enemigo = carga_animacion_enemigo_1()

#--------------------------------------------------------------------------------------------------------------------------------

# Cargar animaciones del segundo enemigo
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
def musica_menu():
    try:
            pygame.mixer.music.load("assets/music/musica_menu_principal.mp3")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
            print("La musica se ha cargado y se esta reproduciendo")
    except pygame.error as e:
            print(f"Error al cargar la música: {e}")

#--------------------------------------------------------------------------------------------------------------------------------

def musica_juego_fondo():
    try:
        pygame.mixer.music.load("assets/music/musica.mp3")
        pygame.mixer.music.play(-1)
        print("Musica cargada correctamente")
    except pygame.error as e:
        print(f"Error al cargar la música: {e}")

menu = MenuPrincipal(ventana)

musica_menu()

#--------------------------------------------------------------------------------------------------------------------------------

# Función para cargar el fondo
def cargar_fondo():
    try:
        fondo = pygame.image.load("assets/images/fondo/suelo-astroslayer.jpg").convert() # Cambia esta ruta si es necesario
        fondo = pygame.transform.scale(fondo, (
        Constantes.ANCHO_VENTANA, Constantes.ALTO_VENTANA))
        print("Fondo cargado correctamente")
        return fondo
    except pygame.error as e:
        print(f"Error al cargar el fondo: {e}")
        return None

# Cargamos el fondo
fondo = cargar_fondo()

#--------------------------------------------------------------------------------------------------------------------------------

# Función para manejar los eventos
def manejar_eventos():
    global mover_izquierda, mover_derecha, mover_arriba, mover_abajo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

        # Procesamos las teclas que se presionan
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:  # Mover a la izquierda
                mover_izquierda = True
                if jugador.direccion != "izquierda":  # Solo cambia si no está mirando a la izquierda
                    jugador.direccion = "izquierda"  # Actualiza la dirección a izquierda
            if event.key == pygame.K_d:  # Mover a la derecha
                mover_derecha = True
                if jugador.direccion != "derecha":  # Solo cambia si no está mirando a la derecha
                    jugador.direccion = "derecha"  # Actualiza la dirección a derecha
            if event.key == pygame.K_w:  # Mover hacia arriba
                mover_arriba = True
            if event.key == pygame.K_s:  # Mover hacia abajo
                mover_abajo = True
            if event.key == pygame.K_e:  # Disparar
                jugador.disparar()

        # Procesamos cuando se suelta una tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:  # Dejar de mover a la izquierda
                mover_izquierda = False
            if event.key == pygame.K_d:  # Dejar de mover a la derecha
                mover_derecha = False
            if event.key == pygame.K_w:  # Dejar de mover hacia arriba
                mover_arriba = False
            if event.key == pygame.K_s:  # Dejar de mover hacia abajo
                mover_abajo = False

    # Manejo del movimiento después de los eventos
    delta_x = delta_y = 0
    if mover_izquierda:
        delta_x = -Constantes.VELOCIDAD_PERSONAJE
    if mover_derecha:
        delta_x = Constantes.VELOCIDAD_PERSONAJE
    if mover_arriba:
        delta_y = -Constantes.VELOCIDAD_PERSONAJE
    if mover_abajo:
        delta_y = Constantes.VELOCIDAD_PERSONAJE

    # Actualizamos el estado de movimiento
    if delta_x != 0 or delta_y != 0:
        jugador.en_movimiento = True
    else:
        jugador.en_movimiento = False

    # Si el jugador se mueve horizontalmente, se actualiza la dirección
    if delta_x != 0:
        # Solo actualizamos la dirección si nos movemos horizontalmente
        if delta_x < 0:
            jugador.direccion = "izquierda"
        elif delta_x > 0:
            jugador.direccion = "derecha"

    # Mover al jugador
    jugador.mover(delta_x, delta_y)

    return True


#--------------------------------------------------------------------------------------------------------------------------------

def reiniciar_juego():
    global jugador, enemigos
    jugador = Personaje(350, 320, animacion_quieto, animacion_movimiento, animacion_disparo_quieto, animacion_disparo_movimiento)
    enemigos = pygame.sprite.Group()
    print("Juego reiniciado")


#--------------------------------------------------------------------------------------------------------------------------------

def pantalla_game_over(ventana):
    fuente = pygame.font.Font("fuentes//Pixel Times.ttf", 70)

    while True:
        ventana.fill((0, 0, 0))  # Fondo negro
        texto_game_over = fuente.render("GAME OVER", True, (255, 0, 0))
        ventana.blit(
            texto_game_over,
            (
                Constantes.ANCHO_VENTANA // 2 - texto_game_over.get_width() // 2,
                Constantes.ALTO_VENTANA // 2 - texto_game_over.get_height() // 2,
            ),
        )

        fuente_reiniciar = pygame.font.Font("fuentes//Pixel Times.ttf", 40)
        texto_reiniciar = fuente_reiniciar.render("Presione R para reiniciar", True, (255, 255, 255))
        ventana.blit(
            texto_reiniciar,
            (
                Constantes.ANCHO_VENTANA // 2 - texto_reiniciar.get_width() // 2,
                Constantes.ALTO_VENTANA // 2 + 100,
            ),
        )

        pygame.display.update()  # Actualizar la pantalla

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()  # Salir completamente del programa
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                return

#--------------------------------------------------------------------------------------------------------------------------------

# Variable global para controlar el tiempo de aparición de enemigos
enemigos_aparicion_tiempo = pygame.time.get_ticks()

# Función para generar los enemigos
def generar_enemigos(enemigos):
    tiempo_actual = pygame.time.get_ticks()
    global enemigos_aparicion_tiempo

    if tiempo_actual - enemigos_aparicion_tiempo > 2000:  # Generar enemigos cada 2 segundos
        enemigos_aparicion_tiempo = tiempo_actual
        x_izquierda, y_izquierda = 0, random.randint(50, Constantes.ALTO_VENTANA - 50)
        x_derecha, y_derecha = Constantes.ANCHO_VENTANA, random.randint(50, Constantes.ALTO_VENTANA - 50)

        velocidad_enemigo = Constantes.VELOCIDAD_ENEMIGO

        enemigo_izquierda = Enemigo(x_izquierda, y_izquierda, animacion_movimiento_enemigo, velocidad_enemigo, "derecha")
        enemigo_derecha = Enemigo(x_derecha, y_derecha, animacion_movimiento_enemigo_2, velocidad_enemigo, "izquierda")

        enemigos.add(enemigo_izquierda)
        enemigos.add(enemigo_derecha)


#--------------------------------------------------------------------------------------------------------------------------------

def colisiones(self, enemigos):
    global puntuacion  # Asegúrate de que la puntuación es global
    for enemigo in enemigos:
        if self.rect.colliderect(enemigo.rect):
            self.game_over = True
            break  # Termina el bucle si el jugador choca con un enemigo

#--------------------------------------------------------------------------------------------------------------------------------

def dibujar_puntuacion(ventana):
    from Controlador.Config import puntuacion

    fuente = pygame.font.Font("fuentes//pixel-comic-sans-undertale-sans-font.ttf", 50)

    texto = fuente.render(f"Puntuacion: {puntuacion}", True, (255, 255, 255))

    ventana.blit(texto, (ventana.get_width() - texto.get_width() - 10, 10))


#--------------------------------------------------------------------------------------------------------------------------------

# Bucle que hace que se inicie el juego
def bucle_juego_inicio(jugador):
    reloj = pygame.time.Clock()
    enemigos = pygame.sprite.Group()

    ejecutando = True

    while ejecutando:
        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutando = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:  # Disparo con tecla 'E'
                    jugador.disparar()

        # Mover y actualizar jugador
        keys = pygame.key.get_pressed()
        delta_x = delta_y = 0
        jugador.en_movimiento = False
        jugador.disparando = False

        # Mover hacia la izquierda
        if keys[pygame.K_a]:
            delta_x = -Constantes.VELOCIDAD_PERSONAJE
            jugador.en_movimiento = True
            jugador.voltear = True

        # Mover hacia la derecha
        if keys[pygame.K_d]:
            delta_x = Constantes.VELOCIDAD_PERSONAJE
            jugador.en_movimiento = True
            jugador.voltear = False

        if keys[pygame.K_w]:
            delta_y = -Constantes.VELOCIDAD_PERSONAJE
            jugador.en_movimiento = True

        if keys[pygame.K_s]:
            delta_y = Constantes.VELOCIDAD_PERSONAJE
            jugador.en_movimiento = True

        if keys[pygame.K_e]:
            jugador.disparando = True

        # Actualizar estado del jugador
        jugador.mover(delta_x, delta_y)
        jugador.actualizar_animacion()

        # Generar enemigos
        generar_enemigos(enemigos)

        # Detectar colisiones entre balas y enemigos
        for bala in jugador.balas:
            bala.mover(enemigos)  # Aquí pasas solo los enemigos

        # Dibujar fondo y enemigos
        ventana.blit(fondo, (0, 0))
        for enemigo in enemigos:
            enemigo.actualizar()
            enemigo.actualizar_animacion()
            ventana.blit(enemigo.image, enemigo.rect)

        # Dibujar jugador
        jugador.draw(ventana)

        # Dibujamos la bala en la ventana
        for bala in jugador.balas:
            bala.dibujar(ventana)

        # Usamos el metodo de colisiones para que el jugador pueda tener colisión con los enemigos
        jugador.colisiones(enemigos)

        # Llamamos al metodo para dibujar la puntuacion en la ventana
        dibujar_puntuacion(ventana)

        jugador.draw_corazones(ventana)

        # Detectar si el jugador muere
        if jugador.muerto:
            pantalla_game_over(ventana)
            reiniciar_juego()
            break

        # Actualizar la pantalla
        pygame.display.update()
        reloj.tick(60)  # Limitar FPS a 60


#--------------------------------------------------------------------------------------------------------------------------------

# Bucle que hace que se inicie el menú
def bucle_menu():
    corriendo = True
    musica_menu()  # Aquí iniciamos la música del menú principal

    while corriendo:
        menu.mostrar()  # Mostramos el menú principal
        pygame.display.update()  # Actualizamos la ventana

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False
            accion = menu.manejar_eventos(event)
            if accion == "Jugar":
                print("¡Comienza el juego!")
                corriendo = False  # Salir del menú
                pygame.mixer.music.stop()  # Detener la música del menú
                musica_juego_fondo()  # Reproducir música del juego

                # Crear el jugador en la posición inicial
                jugador = Personaje(
                    350, 320,
                    animacion_quieto,
                    animacion_movimiento,
                    animacion_disparo_quieto,
                    animacion_disparo_movimiento
                )
                bucle_juego_inicio(jugador)  # Iniciar el bucle del juego

bucle_menu() # Mostramos el menu