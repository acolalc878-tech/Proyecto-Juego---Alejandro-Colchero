import pygame
import sys  # Necesario para salir del programa

# Definir colores y fuente
COLOR_FONDO_MENU = (0, 0, 0)  # Negro
COLOR_BOTON = (100, 100, 255)  # Azul
COLOR_BOTON_HOVER = (150, 150, 255)  # Azul más claro
COLOR_TEXTO = (255, 255, 255)  # Blanco
fuente_menu = pygame.font.Font(None, 50)

# Configuración de la ventana
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))


# Función para dibujar botones en el menú
def dibujar_boton(ventana, texto, x, y, ancho, alto, color):
    pygame.draw.rect(ventana, color, (x, y, ancho, alto))
    texto_renderizado = fuente_menu.render(texto, True, COLOR_TEXTO)
    texto_rect = texto_renderizado.get_rect(center=(x + ancho // 2, y + alto // 2))
    ventana.blit(texto_renderizado, texto_rect)


# Función para el menú principal
def menu_principal():
    boton_jugar = pygame.Rect(300, 200, 200, 50)  # Botón "Jugar"
    boton_salir = pygame.Rect(300, 300, 200, 50)  # Botón "Salir"

    while True:
        ventana.fill(COLOR_FONDO_MENU)

        # Detectar si el mouse está sobre un botón
        mouse_pos = pygame.mouse.get_pos()
        if boton_jugar.collidepoint(mouse_pos):
            dibujar_boton(ventana, "Jugar", 300, 200, 200, 50, COLOR_BOTON_HOVER)
        else:
            dibujar_boton(ventana, "Jugar", 300, 200, 200, 50, COLOR_BOTON)

        if boton_salir.collidepoint(mouse_pos):
            dibujar_boton(ventana, "Salir", 300, 300, 200, 50, COLOR_BOTON_HOVER)
        else:
            dibujar_boton(ventana, "Salir", 300, 300, 200, 50, COLOR_BOTON)

        # Eventos del menú
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.collidepoint(event.pos):
                    return "Jugar"
                elif boton_salir.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()  # Actualizar la pantalla


# Función principal para el juego
def main():
    pygame.init()
    pygame.display.set_caption("ASTRO SLAYER")

    # Mostrar el menú principal
    opcion = menu_principal()

    # Si el usuario selecciona "Jugar", iniciamos el juego
    if opcion == "Jugar":
        print("Inicia el juego")
        # Aquí va el bucle principal del juego o la lógica específica