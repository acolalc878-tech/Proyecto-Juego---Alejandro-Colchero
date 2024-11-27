import pygame
import sys

# Configuración básica
ANCHO_VENTANA = 800
ALTO_VENTANA = 600

COLOR_FONDO_MENU = (0, 0, 0)
COLOR_BOTON = (100, 100, 255)
COLOR_BOTON_HOVER = (150, 150, 255)
COLOR_TEXTO = (255, 255, 255)

# Inicializar Pygame
pygame.init()
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("ASTRO SLAYER")
fuente_menu = pygame.font.Font(None, 50)

# Función para dibujar un botón
def dibujar_boton(ventana, texto, x, y, ancho, alto, color):
    pygame.draw.rect(ventana, color, (x, y, ancho, alto))
    texto_renderizado = fuente_menu.render(texto, True, COLOR_TEXTO)
    texto_rect = texto_renderizado.get_rect(center=(x + ancho // 2, y + alto // 2))
    ventana.blit(texto_renderizado, texto_rect)

# Menú principal
def menu_principal():
    boton_jugar = pygame.Rect(300, 200, 200, 50)  # Botón "Jugar"
    boton_salir = pygame.Rect(300, 300, 200, 50)  # Botón "Salir"

    while True:
        ventana.fill(COLOR_FONDO_MENU)

        # Obtener posición del mouse
        mouse_pos = pygame.mouse.get_pos()

        # Dibujar botones
        if boton_jugar.collidepoint(mouse_pos):
            dibujar_boton(ventana, "Jugar", 300, 200, 200, 50, COLOR_BOTON_HOVER)
        else:
            dibujar_boton(ventana, "Jugar", 300, 200, 200, 50, COLOR_BOTON)

        if boton_salir.collidepoint(mouse_pos):
            dibujar_boton(ventana, "Salir", 300, 300, 200, 50, COLOR_BOTON_HOVER)
        else:
            dibujar_boton(ventana, "Salir", 300, 300, 200, 50, COLOR_BOTON)

        # Manejo de eventos
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

        pygame.display.update()

# Juego principal
def juego():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        ventana.fill((0, 0, 0))  # Color del fondo del juego
        pygame.display.update()

# Función principal
def main():
    opcion = menu_principal()
    if opcion == "Jugar":
        juego()

# Iniciar el programa
if __name__ == "__main__":
    main()
