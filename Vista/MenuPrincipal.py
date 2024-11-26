import pygame
from Controlador import Constantes

class MenuPrincipal:
    def __init__(self, ventana):
        self.ventana = ventana
        self.fuente = pygame.font.Font("fuentes//Super Pixel Personal Use.ttf", 70)
        self.fuente_boton = pygame.font.Font("fuentes//Pixel Times.ttf", 50)
        self.boton_jugar = None
        self.boton_salir = None

        self.fondo = pygame.image.load("assets//images//fondo//fondo_menu_principal.jpg")
        self.fondo = pygame.transform.scale(self.fondo, (Constantes.ANCHO_VENTANA, Constantes.ALTO_VENTANA))

    def detener_musica(self):
        pygame.mixer.music.stop()

    def iniciar_musica(self):
        pygame.mixer.music.play(-1)  # Reproducir en bucle

    def mostrar(self):
        # Dibujamos el fondo
        if self.fondo:
            self.ventana.blit(self.fondo, (0, 0))
        else:
            self.ventana.fill((0, 0, 0))

        # Colores
        color_titulo = (135, 206, 250)  # Azul cielo
        color_boton_normal = (70, 130, 180)  # Azul acero
        color_boton_hover = (100, 149, 237)  # Azul claro
        color_texto = (255, 255, 255)  # Blanco para el texto de los botones

        # Texto del menú
        texto_menu = self.fuente.render("ASTRO SLAYER", True, color_titulo)
        texto_jugar = self.fuente_boton.render("Jugar", True, color_texto)
        texto_salir = self.fuente_boton.render("Salir", True, color_texto)

        # Posición del texto del menú
        self.ventana.blit(texto_menu, (Constantes.ANCHO_VENTANA // 2 - texto_menu.get_width() // 2,
                                       Constantes.ALTO_VENTANA // 4 - texto_menu.get_height() // 2))

        # Crear rectángulos para los botones
        self.boton_jugar = pygame.Rect(Constantes.ANCHO_VENTANA // 2 - texto_jugar.get_width() // 2,
                                       Constantes.ALTO_VENTANA // 2, texto_jugar.get_width() + 20, texto_jugar.get_height() + 10)

        self.boton_salir = pygame.Rect(Constantes.ANCHO_VENTANA // 2 - texto_salir.get_width() // 2,
                                       Constantes.ALTO_VENTANA // 2 + 100, texto_salir.get_width() + 20, texto_salir.get_height() + 10)

        # Dibujar botones
        pygame.draw.rect(self.ventana,
                         color_boton_hover if self.boton_jugar.collidepoint(pygame.mouse.get_pos()) else color_boton_normal,
                         self.boton_jugar)

        pygame.draw.rect(self.ventana,
                         color_boton_hover if self.boton_salir.collidepoint(pygame.mouse.get_pos()) else color_boton_normal,
                         self.boton_salir)

        # Agregar texto a los botones
        self.ventana.blit(texto_jugar, (self.boton_jugar.x + (self.boton_jugar.width - texto_jugar.get_width()) // 2,
                                        self.boton_jugar.y + (self.boton_jugar.height - texto_jugar.get_height()) // 2))

        self.ventana.blit(texto_salir, (self.boton_salir.x + (self.boton_salir.width - texto_salir.get_width()) // 2,
                                        self.boton_salir.y + (self.boton_salir.height - texto_salir.get_height()) // 2))

    def manejar_eventos(self, event):
        # Detectar clic en los botones
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.boton_jugar and self.boton_jugar.collidepoint(event.pos):
                return "Jugar"
            elif self.boton_salir and self.boton_salir.collidepoint(event.pos):
                return "Salir"
        return None
