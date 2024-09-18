import pygame
import constantes
from personaje import Personaje

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