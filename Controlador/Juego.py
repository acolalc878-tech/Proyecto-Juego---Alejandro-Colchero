import pygame
from Vista.Principal import ventana, jugador, manejar_eventos
from Controlador import Constantes

def iniciar_juego():
    pygame.init()

    reloj = pygame.time.Clock()

    run = True
    while run:
        reloj.tick(Constantes.FPS)

        # Llenamos el fondo de color
        ventana.fill(Constantes.COLOR_FONDO)

        # Manejamos los eventos del teclado
        run = manejar_eventos()

        # Actualizamos al jugador
        jugador.mover(0,0)
        jugador.actualizar()
        jugador.draw(ventana)

        # Actualizamos la pantalla
        pygame.display.update()

    # Finalizamos
    pygame.quit()