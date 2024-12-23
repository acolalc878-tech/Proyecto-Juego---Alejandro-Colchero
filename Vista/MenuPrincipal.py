import pygame
from Controlador import Constantes

# Clase que diseña el Menu Principal del juego
class MenuPrincipal:
    def __init__(self, ventana):
        self.ventana = ventana
        self.fuente = pygame.font.Font("fuentes//Super Pixel Personal Use.ttf", 70) # Diseño de la letra del titulo
        self.fuente_boton = pygame.font.Font("fuentes//Pixel Times.ttf", 50) # Diseño de letra de los botones
        self.boton_jugar = None
        self.boton_salir = None

        # Mostramos una imagen de fondo
        try:
            self.fondo = pygame.image.load("assets/images/fondo/FONDO_JUEGO_MENU.png")
            self.fondo = pygame.transform.scale(self.fondo, (Constantes.ANCHO_VENTANA, Constantes.ALTO_VENTANA))
        except pygame.error as e:
            print(f"Error al cargar el fondo del menú: {e}")
            self.fondo = None

        # Ponemos una musica de fondo al menu principal
        try:
            pygame.mixer.music.load("assets/music/musica_menu_principal.mp3")
            pygame.mixer.music.set_volume(0.5)
        except pygame.error as e:
            print(f"Error al cargar la música del menú: {e}")

    # Metodo para que la música se inicie al iniciar el menu
    def iniciar_musica(self):
        pygame.mixer.music.play(-1) # Ponemos - 1 para que se repita en bucle

    # Metodo para que cuando le demos a jugar se pare la musica del menu de inicio
    def detener_musica(self):
        pygame.mixer.music.stop()

    # Metodo que muestra lo anteriormente diseñado, fondo, letras, botones, etc...
    def mostrar(self):
        # Fondo
        if self.fondo:
            self.ventana.blit(self.fondo, (0, 0))
        else:
            self.ventana.fill((0, 0, 0)) # En el caso de que no cargara el fondo predeterminado, el fondo sería negro

        # Colores personalizados
        color_titulo = (229, 190, 1)
        color_boton_normal = (255, 128, 0)
        color_boton_hover = (100, 149, 237)
        color_texto = (255, 255, 255)

        # Texto del menú, y botones
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

    # Metodo para hacer click en los botones del menu de inicio
    def manejar_eventos(self, event):
        # Detectar clic en los botones
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.boton_jugar and self.boton_jugar.collidepoint(event.pos):
                return "Jugar"
            elif self.boton_salir and self.boton_salir.collidepoint(event.pos):
                return "Salir"
        return None