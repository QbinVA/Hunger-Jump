import pygame
import random
import constantes
import sound
from personaje import player
from items import aitems
from rama import Rama  # Asegúrate de importar la clase Rama

def play():
    # Inicializa Pygame
    pygame.init()

    # Configura la pantalla
    pantalla = pygame.display.set_mode((constantes.anchoVentana, constantes.altoVentana))
    pygame.display.set_caption('Hungry Jump')

    # Carga imágenes
    icono = pygame.image.load("assets/images/items/banana0.png")
    pygame.display.set_icon(icono)

    fondo = pygame.image.load("assets/images/fondos/lvl 1.png").convert()
    sueloPasto = pygame.image.load("assets/images/fondos/sueloPasto.png")

    # Llama a la función sonido del archivo sound
    sound.sound_lvl_1()

    reloj = pygame.time.Clock()

    # Grupo de sprites, instanciación del objeto jugador
    sprites = pygame.sprite.Group()
    ramas = pygame.sprite.Group()

    for x in range(random.randrange(5) + 1):
        alimento = aitems()
        sprites.add(alimento)

    # Instanciar ramas y agregarlas al grupo de ramas
    ramaD = Rama(310, 430, "assets/images/fondos/ramaDer.png")
    ramaI = Rama(-10, 320, "assets/images/fondos/ramaIzq.png")
    ramas.add(ramaD, ramaI)
    sprites.add(ramaD, ramaI)

    jugador = player(ramas)
    sprites.add(jugador)

    run = True
    y = 0

    while run:
        yRelativa = y % fondo.get_rect().height
        pantalla.blit(fondo, (0, yRelativa - fondo.get_rect().height))
        if yRelativa < constantes.altoVentana:
            pantalla.blit(fondo, (0, yRelativa))
        y += 1

        pantalla.blit(sueloPasto, (0, 360))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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

# Ejecutar el juego
if __name__ == "__main__": # Si el archivo es ejecutado directamente
    play() # Llama a la función play