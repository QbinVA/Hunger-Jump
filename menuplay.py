import pygame
import random
import constantes
import sound
from personaje import player
from items import aitems

def play():
    # Inicializa Pygame
    pygame.init()

    # Configura la pantalla
    pantalla = pygame.display.set_mode((constantes.anchoVentana, constantes.altoVentana))
    pygame.display.set_caption('Hungry Jump')

    # Carga imágenes
    icono = pygame.image.load("assets/images/items/banana0.png") #Importo el icono de la ventana
    pygame.display.set_icon(icono) #Lo despliego

    #Importo el fondo del nivel
    fondo = pygame.image.load("assets/images/fondos/lvl 1.png").convert()

    #Importo la imagen del suelo
    sueloPasto = pygame.image.load("assets/images/fondos/sueloPasto.png")

    #Importo las imagenes de las ramas
    ramaD = pygame.image.load("assets/images/fondos/ramaDer.png") # Rama derecha
    ramaI = pygame.image.load("assets/images/fondos/ramaIzq.png") # Rama izquierda

    # Llama a la función sonido del archivo sound
    sound.sound_lvl_1() # Reproduce el soundtrack del primer nivel

    reloj = pygame.time.Clock()

    # Grupo de sprites, instanciación del objeto jugador
    sprites = pygame.sprite.Group()

    for x in range(random.randrange(5) + 1):
        alimento = aitems()
        sprites.add(alimento)

    # Instancioamos jugador
    jugador = player()
    sprites.add(jugador)

    # Mantiene el bucle
    run = True
    y = 0

    while run:

        # Bucle de fondo en constante movimiento, se mueve hacia arriba sumandole pixeles a y
        yRelativa = y % fondo.get_rect().height
        pantalla.blit(fondo, (0, yRelativa - fondo.get_rect().height))
        if yRelativa < constantes.altoVentana:
            pantalla.blit(fondo, (0, yRelativa))
        y += 1

        # Dibujo el suelo
        pantalla.blit(sueloPasto, (0, 360))
        pantalla.blit(ramaD, (310, 430)) # Dibujo la rama derecha
        pantalla.blit(ramaI, (-10, 320)) # Dibujo la rama izquierda

        # Verificar los eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Cierra la ventana
                run = False

        # Actualizacion de sprites
        sprites.update()

        # Dibuja al personaje en pantalla
        sprites.draw(pantalla)

        # Actualizar la pantalla
        pygame.display.update()

        # Controlar el frame rate
        reloj.tick(constantes.fps)

    # Salida del juego
    pygame.quit()

# No sé que hace
if __name__ == "__main__":
    play()
