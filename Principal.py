# Importamos las librerias necesarias para hacer nuestro juego

import pygame
import random

from Personaje import Personaje
import Constantes

# Inicializamos pygame
pygame.init()

# Creamos la ventana
ventana = pygame.display.set_mode((Constantes.ANCHO_VENTANA, Constantes.ALTO_VENTANA))

# Actualizamos
pygame.display.update()

# Cambiamos el titulo de la ventana del juego
pygame.display.set_caption("Videojuego por turnos")

imagen_jugador = pygame.image.load("assets//images//character//player//player-run1.png ")

# Creamos una instancia del jugador
jugador = Personaje(50,50, imagen_jugador)


# Definimos variables de movimiento del jugador
mover_arriba = False
mover_abajo = False
mover_derecha = False
mover_izquierda = False

# Controlamos los Frames por segundo
reloj = pygame.time.Clock()

# Bucle del juego
run = True
while run:

    # Va a ir a 60 fps
    reloj.tick(Constantes.FPS)

    # Le asignamos color al fondo de la ventana
    ventana.fill(Constantes.COLOR_FONDO)

    # Calcular movimiento jugador
    delta_x = 0
    delta_y = 0

    if mover_derecha == True:
        delta_x = Constantes.VELOCIDAD_PERSONAJE
    if mover_izquierda == True:
        delta_x = -Constantes.VELOCIDAD_PERSONAJE
    if mover_arriba == True:
        delta_y = -Constantes.VELOCIDAD_PERSONAJE
    if mover_abajo == True:
        delta_y = Constantes.VELOCIDAD_PERSONAJE

    jugador.movimiento(delta_x, delta_y)

# Hacemos que salga el cuadrado en la ventana
    jugador.draw(ventana)

# Capturamos los eventos producidos
    for event in pygame.event.get():
        # Si hacemos click en la X se cierra la ventana
        if event.type == pygame.QUIT: run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
               mover_abajo = True

        # Evento para cuando soltemos la tecla dejemos de movernos
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_s:
                mover_abajo = False

# Permite actualizar la pantalla para que se vean los cambios
    pygame.display.update()

pygame.quit()