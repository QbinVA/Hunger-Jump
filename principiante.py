#Importo pygame y sistema
import pygame, sys
#Importo la pantalla
import pygame.display
from pygame.locals import *
from button import Button
import constantes
import sound
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

btnLevel1 = pygame.image.load("assets/images/menu/btnlevel1.png")
btnLevel1 = pygame.transform.scale(btnLevel1, (250, 150))

btnLevel2 = pygame.image.load("assets/images/menu/btnlevel2.png")
btnLevel2 = pygame.transform.scale(btnLevel2, (250, 150))

btnLevel3 = pygame.image.load("assets/images/menu/btnlevel3.png")
btnLevel3 = pygame.transform.scale(btnLevel3, (250, 150))

backArrow = pygame.image.load("assets/images/menu/backArrow.png")
backArrow = pygame.transform.scale(backArrow, (230, 160))


#Fuente
def get_font(size):
    return pygame.font.Font("assets/Font/font.ttf", size)


def levels_p():

    #Función de la pantalla play
    def jugar():
        from characters import characters
        characters() #mando llamar la funcion play del archivo menuplay

    #Función de la pantalla opciones    
    def jugar2():
        from characters2 import characters
        characters() #mando llamar la funcion

    def jugar3():
        from characters2 import characters
        characters() #mando llamar la funcion

    def back():
        from dificultad import difi
        difi()
        

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

            PLAY_BUTTON = Button(image=btnLevel1, pos=(250, 200), 
                                text_input="", font=get_font(20), base_color="#d7fcd4", hovering_color="White")
            OPTIONS_BUTTON = Button(image=btnLevel2, pos=(250, 350), 
                                text_input="", font=get_font(25), base_color="#d7fcd4", hovering_color="White")
            LEVEL3_BUTTON = Button(image=btnLevel3, pos=(250, 500), 
                                text_input="", font=get_font(25), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(image=backArrow, pos=(95, 680), 
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
                        jugar2()
                    if LEVEL3_BUTTON.checkForInput(MENU_MOUSE_POS):
                        jugar3()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        back()

            pygame.display.update()

    levels_menu()