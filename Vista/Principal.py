import random

import pygame
from Controlador import Constantes
from Modelo.Bala import Bala
from Modelo.Enemigo import Enemigo
from Modelo.Personaje import Personaje
from Recursos import escalar_imagen, balas
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
        fondo = pygame.image.load("assets/images/fondo/suelo-astroslayer.jpg")  # Cambia esta ruta si es necesario
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
    global mover_izquierda, mover_derecha, mover_arriba, mover_abajo, run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
                jugador.direccion = "izquierda"
            if event.key == pygame.K_d:
                mover_derecha = True
                jugador.direccion = "derecha"
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True
            if event.key == pygame.K_e:
                jugador.disparar()  # Activar la animación de disparo
            if event.key == pygame.K_r and jugador.muerto:  # Reiniciar el juego si el jugador presiona R
                reiniciar_juego()
                return True

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

def reiniciar_juego():
    global jugador, enemigos
    jugador = Personaje(350, 320, animacion_quieto, animacion_movimiento, animacion_disparo_quieto, animacion_disparo_movimiento)
    enemigos = pygame.sprite.Group()  # Vuelves a crear los enemigos
    print("Juego reiniciado")

#--------------------------------------------------------------------------------------------------------------------------------

def pantalla_game_over(ventana):
    fuente = pygame.font.Font("fuentes//Pixel Times.ttf", 70)

    texto_game_over= fuente.render("GAME OVER", True, (255,0,0))
    ventana.blit(texto_game_over, (
             Constantes.ANCHO_VENTANA // 2 - texto_game_over.get_width() // 2, Constantes.ALTO_VENTANA // 2 - texto_game_over.get_height() // 2))

    fuente_reiniciar = pygame.font.Font("fuentes//Pixel Times.ttf", 40)
    texto_reiniciar = fuente_reiniciar.render("Presione R para reiniciar", True, (255, 255, 255))
    ventana.blit(texto_reiniciar, (
        Constantes.ANCHO_VENTANA // 2 - texto_reiniciar.get_width() // 2, Constantes.ALTO_VENTANA // 2 + 100))

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
    for enemigo in enemigos:
        if self.rect.colliderect(enemigo.rect):
            self.game_over = True
            break

#--------------------------------------------------------------------------------------------------------------------------------
def bucle_juego():
    reloj = pygame.time.Clock()
    corriendo = True

    # Aquí puedes inicializar el jugador y los enemigos
    jugador = Personaje(350, 320, animacion_quieto, animacion_movimiento, animacion_disparo_quieto, animacion_disparo_movimiento)
    enemigos = []  # Inicializa la lista de enemigos

    while corriendo:
        ventana.fill((0, 0, 0))  # Fondo negro
        ventana.blit(fondo, (0, 0))  # Fondo del juego

        # Manejar eventos (movimiento, disparo, etc.)
        if not manejar_eventos():  # Asegúrate de que manejar_eventos devuelva False si se cierra el juego
            corriendo = False

        generar_enemigos(enemigos)

        # Dibuja los enemigos
        for enemigo in enemigos:
            ventana.blit(enemigo.image, enemigo.rect)

        # Dibuja al jugador
        ventana.blit(jugador.image, jugador.rect)

        # Actualizar pantalla
        pygame.display.update()

        reloj.tick(60)  # Limitar FPS a 60

#--------------------------------------------------------------------------------------------------------------------------------
def bucle_juego_inicio(jugador):
    reloj = pygame.time.Clock()
    corriendo = True
    enemigos = pygame.sprite.Group()  # Usar un grupo de sprites para los enemigos

    while corriendo:
        # Manejar eventos
        if not manejar_eventos():
            corriendo = False

        keys = pygame.key.get_pressed()
        delta_x = delta_y = 0

        if keys[pygame.K_LEFT]:
            delta_x = -jugador.velocidad
            jugador.direccion = "izquierda"
        elif keys[pygame.K_RIGHT]:
            delta_x = jugador.velocidad
            jugador.direccion = "derecha"
        else:
            jugador.direccion = "quieto"

        if keys[pygame.K_UP]:
            delta_y = -jugador.velocidad
        elif keys[pygame.K_DOWN]:
            delta_y = jugador.velocidad

        jugador.mover(delta_x, delta_y)  # Mover al jugador
        jugador.actualizar_animacion()  # Actualizar animaciones del jugador

        # Generar y mover enemigos
        generar_enemigos(enemigos)

        # Actualizar la pantalla
        ventana.fill((0, 0, 0))
        ventana.blit(fondo, (0, 0))

        # Dibujar y actualizar enemigos
        for enemigo in enemigos:
            enemigo.actualizar()
            enemigo.actualizar_animacion()
            ventana.blit(enemigo.image, enemigo.rect)

        # Dibujar al jugador
        ventana.blit(jugador.image, jugador.rect)

        pygame.display.update()
        reloj.tick(60)



#--------------------------------------------------------------------------------------------------------------------------------
def bucle_menu():
    corriendo = True
    musica_menu()  # Iniciar música del menú

    while corriendo:
        ventana.fill((0, 0, 0))  # Fondo negro para el menú
        menu.mostrar()  # Mostrar el menú principal
        pygame.display.update()  # Actualizar la ventana

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
                jugador = Personaje(350, 320, animacion_quieto, animacion_movimiento, animacion_disparo_quieto, animacion_disparo_movimiento)  # Asegúrate de que la clase Personaje esté definida
                bucle_juego_inicio(jugador)  # Iniciar el bucle del juego

bucle_menu()