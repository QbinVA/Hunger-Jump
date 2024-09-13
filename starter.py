#Importo pygame y sistema
import pygame, sys
#Importo la pantalla
import pygame.display
from pygame.locals import *
from button import Button
import constantes
from personaje import Personaje

#Inicializo pygame
pygame.init()

pantalla = pygame.display.set_mode((500, 750))
pygame.display.set_caption("Hungry Jump")

#Declaro e inserto el icono
icono = pygame.image.load("assets/images/items/banana0.png")
pygame.display.set_icon(icono)

menuBg = pygame.image.load("assets/images/fondos/menuBg.png")


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/Font/font.ttf", size)

def play():
    while True:

        #Declaro la variable pantalla con sus respectivos valores
        pantalla = pygame.display.set_mode((constantes.anchoVentana, constantes.altoVentana))

        #Declaro e inserto el icono
        icono = pygame.image.load("assets/images/items/banana0.png")
        pygame.display.set_icon(icono)

        #Declaro e inserto el fondo
        fondo = pygame.image.load("assets/images/fondos/lvl 1.png").convert()
        y = 0


        #controlar el frame rate
        reloj = pygame.time.Clock()

        #Inserto un caption
        pygame.display.set_caption('Hungry Jump')

        #Imagenes a escala
        def escalar_img(image, scale):
            w = image.get_width()
            h = image.get_height()
            nueva_imagen = pygame.transform.scale(image, (w*scale, h*scale))
            return nueva_imagen

        # Personaje
        animacionX = []
        for i in range (2):
            img = pygame.image.load(f'assets/images/items/banana{i}.png')
            img = escalar_img(img, constantes.escalaPersonaje)
            animacionX.append(img)

        salta = [pygame.image.load('assets/images/items/banana0.png'),
                pygame.image.load('assets/images/items/banana0.png')]

        jugador = Personaje(50, 50, animacionX)


        #Definir las variables de movimiento del jugador
        # Posición y tamaño del personaje
        px = 400
        py = 500
        ancho = 10

        # Variables de salto
        salto = True  # El personaje está saltando al principio
        cuentaSalto = 20  # Aumentamos este valor para controlar la altura del salto

        # Variables de dirección
        izquierda = False
        derecha = False
        cuentaPasos = 0

        run = True
        #Ciclo infinito
        while run == True:

            # Rellenar la pantalla de negro antes de dibujar cualquier cosa
            pantalla.fill(constantes.negro)

            #Calcular el movimiento del jugador
            delta_x = 0
            delta_y = 0

            if izquierda == True:
                delta_x = -constantes.velocidad
            if derecha == True:
                delta_x = constantes.velocidad

            # Mover al jugador
            jugador.movimiento(delta_x, delta_y)
            jugador.update()

            # Dibujar el fondo después de rellenar la pantalla de negro si aún lo quieres visible
            yRelativa = y % fondo.get_rect().height
            pantalla.blit(fondo, (0, yRelativa - fondo.get_rect().height))
            if yRelativa < constantes.altoVentana:
                pantalla.blit(fondo, (0, yRelativa))
            y += 1

            # Dibujar al jugador por encima del fondo
            jugador.dibujar(pantalla)

            # Verificar los eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        izquierda = True
                    if event.key == pygame.K_RIGHT:
                        derecha = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        izquierda = False
                    if event.key == pygame.K_RIGHT:
                        derecha = False

            # Actualizar la pantalla
            pygame.display.update()
            reloj.tick(constantes.fps)

    
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
                    main_menu()

        pygame.display.update()

def main_menu():
    # Variables para el desplazamiento del fondo
    x = 0  # Posición inicial del fondo
    velocidad_fondo = 1  # Velocidad de desplazamiento del fondo

    while True:
        # Desplazamiento horizontal del fondo
        x -= velocidad_fondo  # Mueve el fondo hacia la izquierda

        # Calcula la posición relativa del fondo para hacer un bucle infinito
        x_relativa = x % menuBg.get_rect().width
        pantalla.blit(menuBg, (x_relativa - menuBg.get_rect().width, 0))
        pantalla.blit(menuBg, (x_relativa, 0))

        # Después de dibujar el fondo, ahora se dibujan los botones y el texto
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(25).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(200, 300))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/images/menu/StartButton.png"), pos=(250, 375), 
                            text_input="PLAY", font=get_font(25), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/images/menu/Config.png"), pos=(410, 90), 
                            text_input="OPTIONS", font=get_font(25), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/images/menu/btnPausa.png"), pos=(90, 90), 
                            text_input="QUIT", font=get_font(25), base_color="#d7fcd4", hovering_color="White")

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
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()