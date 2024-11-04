# Importamos las librerias necesarias para hacer nuestro juego

import pygame
import random
from Personaje import Personaje
import Constantes

jugador = Personaje(50,50)

# Inicializamos pygame
pygame.init()

# Creamos la ventana
ventana = pygame.display.set_mode((Constantes.ANCHO_VENTANA, Constantes.ALTO_VENTANA))

# Cambiamos el titulo de la ventana del juego
pygame.display.set_caption("Videojuego por turnos")

# Definimos variables de movimiento del jugador
mover_arriba = False
mover_abajo = False
mover_derecha = False
mover_izquierda = False


# Bucle del juego
run = True
while run:

    # Calcular movimiento jugador
    delta_x = 0
    delta_y = 0

    if mover_derecha == True:
        delta_x = 5

    if mover_izquierda == True:
        delta_x = -5

    if mover_arriba == True:
        delta_y = -5

    if mover_abajo == True:
        delta_y = -5

        # Vamos a mover al personaje
        jugador.mover_personaje(delta_x, delta_y)

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



# Permite actualizar la pantalla para que se vean los cambios
    pygame.display.update()

pygame.quit()