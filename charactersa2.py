# Importo pygame y sistema
import pygame, sys
from pygame.locals import *
from button import Button
import constantes
import sound

# Inicializo pygame
pygame.init()

# Creo y seteo valores a la pantalla
pantalla = pygame.display.set_mode((500, 750))
pygame.display.set_caption("Hungry Jump")  # Título de la ventana

# Declaro e inserto el icono de la ventana
icono = pygame.image.load("assets/images/items/banana0.png")
pygame.display.set_icon(icono)

# Fondo del menú
menuBg = pygame.image.load("assets/images/fondos/menuBg.png")

iNiño = pygame.image.load("assets/images/personajes/niño0.png").convert()
iNiño = pygame.transform.scale(iNiño, (120, 170))
iNiño.set_colorkey(constantes.blanco)

iNiña = pygame.image.load("assets/images/personajes/niña0.png").convert()
iNiña = pygame.transform.scale(iNiña, (120, 170))
iNiña.set_colorkey(constantes.blanco)

backArrow = pygame.image.load("assets/images/menu/backArrow.png")
backArrow = pygame.transform.scale(backArrow, (230, 160))

# Fuente
def get_font(size):
    return pygame.font.Font("assets/Font/font.ttf", size)

def characters():

    # Función de la pantalla play
    def niño():
        from sound import sound_clic2
        sound_clic2()  # Reproduce el sonido del botón
        from instruccionesa2 import instrucciones
        instrucciones()  # Mando llamar la función play del archivo menuplay

    # Función de la pantalla opciones    
    def niña():
        from sound import sound_clic2
        sound_clic2()  # Reproduce el sonido del botón
        from instruccionesafa2 import instrucciones
        instrucciones()  # Mando llamar la función play del archivo menuplay

    def back():
        from sound import sound_clic1
        sound_clic1()  # Reproduce el sonido del botón
        from avanzado import levels_a
        levels_a()

    # Función del menú principal
    def characters_menu():
        # Variables para el desplazamiento del fondo
        x = 0  # Posición inicial del fondo
        velocidad_fondo = 1  # Velocidad de desplazamiento del fondo

        # Llama a la función sonido del archivo sound
        sound.sound_menu()  # Reproduce el soundtrack del primer nivel

        while True:
            # Desplazamiento horizontal del fondo
            x -= velocidad_fondo  # Mueve el fondo hacia la izquierda

            # Calcula la posición relativa del fondo para hacer un bucle infinito
            x_relativa = x % menuBg.get_rect().width
            pantalla.blit(menuBg, (x_relativa - menuBg.get_rect().width, 0))
            pantalla.blit(menuBg, (x_relativa, 0))

            # Después de dibujar el fondo, ahora se dibujan los botones y el texto
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = get_font(25).render("", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(200, 300))

            PLAY_BUTTON = Button(image=iNiño, pos=(170, 375), 
                                text_input="", font=get_font(20), base_color="#d7fcd4", hovering_color="White")
            OPTIONS_BUTTON = Button(image=iNiña, pos=(330, 375), 
                                text_input="", font=get_font(25), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(image=backArrow, pos=(95, 680), 
                                text_input="", font=get_font(22), base_color="#d7fcd4", hovering_color="White")

            pantalla.blit(MENU_TEXT, MENU_RECT)

            # Agregar hoverEffect para los botones
            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.hoverEffect(MENU_MOUSE_POS)  # Aplicar el efecto de hover
                button.update(pantalla)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        niño()
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        niña()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        back()

            pygame.display.update()

    characters_menu()
