# Importo pygame y sistema
import pygame
import sys
from pygame.locals import *
from button import Button
import sound
import constantes

# Inicializo pygame
pygame.init()

# comentario

# Fuente
def get_font(size):
    return pygame.font.Font("assets/Font/PressStart2P-Regular.ttf", size)

# Pantalla de niveles
def settings():

    # Creo y seteo valores a la pantalla
    pantalla = pygame.display.set_mode((500, 750))
    pygame.display.set_caption("Hungry Jump")  # Título de la ventana

    # Declaro e inserto el icono de la ventana
    icono = pygame.image.load("assets/images/items/banana0.png")
    pygame.display.set_icon(icono)

    # Fondo del menú
    menuBg = pygame.image.load("assets/images/fondos/menuBg.png")

    español_image = pygame.image.load("assets/images/idiomas/mexico.jpg").convert()
    español_image = pygame.transform.scale(español_image, (140, 110))

    usaSelected = pygame.image.load("assets/images/idiomas/usaselected.jpg").convert()
    usaSelected = pygame.transform.scale(usaSelected, (160, 130))

    backArrow = pygame.image.load("assets/images/menu/backArrow.png")
    backArrow = pygame.transform.scale(backArrow, (230, 160))

    def español():
        from sound import sound_Button
        sound_Button()
        from configuracion import configuracion
        configuracion()

    def ingles():
        from sound import sound_Button
        sound_Button()
        
    def creditos():
        from sound import sound_Button
        sound_Button()
        from creditos import instrucciones
        instrucciones()

    def back():
        from sound import sound_clic1
        sound_clic1()
        from startere import main_menu
        main_menu()

    # Menú de niveles
    def levels_menu():
        x = 0  # Posición inicial del fondo
        velocidad_fondo = 1

        sound.sound_menu()

        while True:
            x -= velocidad_fondo
            x_relativa = x % menuBg.get_rect().width
            pantalla.blit(menuBg, (x_relativa - menuBg.get_rect().width, 0))
            pantalla.blit(menuBg, (x_relativa, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            PLAY_BUTTON = Button(image=español_image, pos=((constantes.anchoVentana // 2 - 100), 300), 
                                 text_input="", font=get_font(20), base_color="#d7fcd4", hovering_color="White")
            OPTIONS_BUTTON = Button(image=usaSelected, pos=((constantes.anchoVentana // 2 + 100), 300), 
                                    text_input="", font=get_font(25), base_color="#d7fcd4", hovering_color="White")
            LEVEL3_BUTTON = Button(image=None, pos=(250, 500), 
                                    text_input="Credits", font=get_font(30), base_color="white", hovering_color=constantes.ocre,  hover_effect=False, border_color="black")
            QUIT_BUTTON = Button(image=backArrow, pos=(95, 680), 
                                 text_input="", font=get_font(22), base_color="#d7fcd4", hovering_color="White")

            for button in [PLAY_BUTTON, OPTIONS_BUTTON, LEVEL3_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.hoverEffect(MENU_MOUSE_POS)
                button.update(pantalla)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        español()
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        ingles()
                    if LEVEL3_BUTTON.checkForInput(MENU_MOUSE_POS):
                        creditos()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        back()

            pygame.display.update()

    levels_menu()
