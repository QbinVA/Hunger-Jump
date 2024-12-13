#Importo pygame y sistema
import pygame, sys
#Importo la pantalla
import pygame.display
from pygame.locals import *
from button import Button
import constantes
import sound

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
imagen_config = pygame.image.load("assets/images/fondos/menuConfig.png").convert()
imagen_config = pygame.transform.scale(imagen_config, (constantes.anchoVentana, constantes.altoVentana))

#Fuente
def get_font(size):
    return pygame.font.Font("assets/Font/font.ttf", size)

#Función de la pantalla play
def jugar():
    import sound
    sound.sound_clic2() # Reproduce el sonido del botón
    from loree import lore
    lore() #mando llamar la funcion play del archivo menuplay

#Función de la pantalla opciones    
def options():

        # Llama a la función sonido del archivo sound
        sound.sound_menu() # Reproduce el soundtrack del primer nivel

        from settings import settings
        settings()

#Funcion del menu principal
def main_menu():
    # Variables para el desplazamiento del fondo
    x = 0  # Posición inicial del fondo
    velocidad_fondo = 1  # Velocidad de desplazamiento del fondo

    # Carga la imagen con el nombre del juego
    titulo = pygame.image.load("assets/images/menu/Título.png")
    tituloS = pygame.transform.scale(titulo, (int(titulo.get_width() * 0.3), int(titulo.get_height() * 0.3)))  #Escala al 40%
    tituloPos = (95, 200)  # Posición en la pantalla

    tuerca = pygame.image.load("assets/images/menu/Config.png")
    tuerca = pygame.transform.scale(tuerca, (110, 110))

    tuercaSelected = pygame.image.load("assets/images/menu/Config selected.png")

    bPlay = pygame.image.load("assets/images/menu/StartButton.png")
    bPlay = pygame.transform.scale(bPlay, (300, 180))

    bPlaySelected = pygame.image.load("assets/images/menu/StartSelected.png")
    bPlaySelected = pygame.transform.scale(bPlaySelected, (350, 225))

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
        pantalla.blit(tituloS, tituloPos)

        # Después de dibujar el fondo, ahora se dibujan los botones y el texto
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(25).render("", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(200, 300))

        # Cambiar imagen del botón de play según hover
        if 50 < MENU_MOUSE_POS[0] < 400 and 410 < MENU_MOUSE_POS[1] < 630:  # Ajustar las coordenadas según el botón
            PLAY_BUTTON = Button(image=bPlaySelected, pos=(250, 530), 
                                text_input="", font=get_font(20), base_color="#d7fcd4", hovering_color="White")
        else:
            PLAY_BUTTON = Button(image=bPlay, pos=(250, 530), 
                                text_input="", font=get_font(20), base_color="#d7fcd4", hovering_color="White")

        # Cambiar imagen del botón de opciones según hover
        if 400 < MENU_MOUSE_POS[0] < 470 and 30 < MENU_MOUSE_POS[1] < 100:  # Ajustar las coordenadas según el botón
            OPTIONS_BUTTON = Button(image=pygame.transform.scale(tuercaSelected, (130, 130)), pos=(430, 75), 
                                    text_input="", font=get_font(25), base_color="#d7fcd4", hovering_color="White")
        else:
            OPTIONS_BUTTON = Button(image=tuerca, pos=(430, 70), 
                                    text_input="", font=get_font(25), base_color="#d7fcd4", hovering_color="White")
            
        QUIT_BUTTON = Button(image=pygame.image.load("assets/images/menu/botonSalir.png"), pos=(70, 90), 
                            text_input="", font=get_font(22), base_color="#d7fcd4", hovering_color="White")

        pantalla.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
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
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()