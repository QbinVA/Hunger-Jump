#Importo pygame y sistema
import pygame, sys
#Importo la pantalla
import pygame.display
from pygame.locals import *
from button import Button
import constantes
import menuplay
import sound
import starter
import dificultad

#Inicializo pygame
pygame.init()

#Creo y seteo valores a la pantalla
pantalla = pygame.display.set_mode((500, 750))
pygame.display.set_caption("Hungry Jump") #Titulo de la ventana

#Declaro e inserto el icono de la ventana
icono = pygame.image.load("assets/images/items/banana0.png")
pygame.display.set_icon(icono)

#Fondo del menu
menuBg = pygame.image.load("assets/images/fondos/menuBg.png")

#Fuente
def get_font(size):
    return pygame.font.Font("assets/Font/font.ttf", size)


def levels_p():

    #Función de la pantalla play
    def jugar():
        menuplay.play() #mando llamar la funcion play del archivo menuplay

    #Función de la pantalla opciones    
    def options():
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            pantalla.fill("white")

            OPTIONS_TEXT = get_font(25).render("This is the OPTIONS screen.", True, "Black")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(200, 300))
            pantalla.blit(OPTIONS_TEXT, OPTIONS_RECT)

            OPTIONS_BACK = Button(image=None, pos=(400, 600), 
                                text_input="BACK", font=get_font(25), base_color="Black", hovering_color="Green")

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(pantalla)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        levels_menu()

            pygame.display.update()

    #Funcion del menu principal
    def levels_menu():
        # Variables para el desplazamiento del fondo
        x = 0  # Posición inicial del fondo
        velocidad_fondo = 1  # Velocidad de desplazamiento del fondo

        # Llama a la función sonido del archivo sound
        sound.sound_menu() # Reproduce el soundtrack del primer nivel

        while True:
            # Desplazamiento horizontal del fondo
            x -= velocidad_fondo  # Mueve el fondo hacia la izquierda

            # Calcula la posición relativa del fondo para hacer un bucle infinito
            x_relativa = x % menuBg.get_rect().width
            pantalla.blit(menuBg, (x_relativa - menuBg.get_rect().width, 0))
            pantalla.blit(menuBg, (x_relativa, 0))

            # Dibujar el titulo en pantalla
            #pantalla.blit(tituloS, tituloPos)

            # Después de dibujar el fondo, ahora se dibujan los botones y el texto
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = get_font(25).render("", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(200, 300))

            PLAY_BUTTON = Button(image=pygame.image.load("assets/images/menu/btnPausa.png"), pos=(250, 200), 
                                text_input="", font=get_font(20), base_color="#d7fcd4", hovering_color="White")
            OPTIONS_BUTTON = Button(image=pygame.image.load("assets/images/menu/btnPausa.png"), pos=(250, 350), 
                                text_input="", font=get_font(25), base_color="#d7fcd4", hovering_color="White")
            LEVEL3_BUTTON = Button(image=pygame.image.load("assets/images/menu/btnPausa.png"), pos=(250, 500), 
                                text_input="", font=get_font(25), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(image=pygame.image.load("assets/images/menu/btnPausa.png"), pos=(70, 680), 
                                text_input="", font=get_font(22), base_color="#d7fcd4", hovering_color="White")

            pantalla.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, OPTIONS_BUTTON, LEVEL3_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(pantalla)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        jugar()
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        options()
                    if LEVEL3_BUTTON.checkForInput(MENU_MOUSE_POS):
                        options()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        back()

            pygame.display.update()

    def back():
        dificultad.difi()

    levels_menu()