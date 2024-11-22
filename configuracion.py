# Importo pygame y sistema
import pygame
import sys
from pygame.locals import *
from button import Button
import sound
import constantes

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

españolSelected = pygame.image.load("assets/images/idiomas/mexicoselected.jpg").convert()
españolSelected = pygame.transform.scale(españolSelected, (160, 130))

usa = pygame.image.load("assets/images/idiomas/usa.jpg").convert()
usa = pygame.transform.scale(usa, (140, 110))

backArrow = pygame.image.load("assets/images/menu/backArrow.png")
backArrow = pygame.transform.scale(backArrow, (230, 160))

# Fuente
def get_font(size):
    return pygame.font.Font("assets/Font/PressStart2P-Regular.ttf", size)

# Pantalla de niveles
def configuracion():

    def español():
        from sound import sound_Button
        sound_Button()

    def ingles():
        from sound import sound_Button
        sound_Button()
        from characters2 import characters
        characters()

    def creditos():
        from sound import sound_Button
        sound_Button()
        from characters3 import characters
        characters()

    def back():
        from sound import sound_clic1
        sound_clic1()
        from starter import main_menu
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

            PLAY_BUTTON = Button(image=españolSelected, pos=((constantes.anchoVentana // 2 - 100), 200), 
                                 text_input="", font=get_font(20), base_color="#d7fcd4", hovering_color="White")
            OPTIONS_BUTTON = Button(image=usa, pos=((constantes.anchoVentana // 2 + 100), 200), 
                                    text_input="", font=get_font(25), base_color="#d7fcd4", hovering_color="White")
            LEVEL3_BUTTON = Button(image=None, pos=(250, 500), 
                                    text_input="Créditos", font=get_font(30), base_color="white", hovering_color=constantes.ocre,  hover_effect=False, border_color="black")
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
