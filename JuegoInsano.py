#Importo pygame y sistema
import pygame
import sys
#Importo la pantalla
import pygame.display
from pygame.locals import *

#Inicializo pygame
pygame.init()

#Declaro colores
blanco = (255,255,255)
negro = (0,0,0)
rojo = (255,0,0)
azul = (0,0,255)
verde = (0,255,0)
hc74225 = (199,66,37)
h61cd35 = (97,205,53)

#Declaro la variable pantalla con sus respectivos valores
pantalla = pygame.display.set_mode((500, 750))
#Inserto un caption
pygame.display.set_caption('Juego insano')

#Inserto color en la pantalla
pantalla.fill(blanco)

#Declaro un rectangulo (donde, color, posicion, tamaño)
rect1 = pygame.draw.rect(pantalla, rojo, (100, 50, 100, 50))

#Declaro una linea (donde, color, (inicio y fin, inclinacion), grosor)
line1 = pygame.draw.line(pantalla, verde, (100, 104), (199,104), 10)

#Deckaro un circulo (donde, color, (eje x, eje y), radio, relleno)
circle1 = pygame.draw.circle(pantalla, negro, (122, 250), 20, 0)

#Declaro un elipse (donde, color, (eje x, eje y, tamaño x, tamaño y), relleno)
elipse1 = pygame.draw.ellipse(pantalla, h61cd35, (275, 200, 40, 80), 10)

#declaro puntos
puntos = [(100,300),(100,100),(150,100)]
#los uso para crear una figura
pygame.draw.polygon(pantalla, (0,150, 255), puntos, 8)


#Ciclo infinito
while True:
    for event in pygame.event.get():
        if event.type == quit:
            pygame.quit()
            sys.exit()
    pygame.display.update() #Se actualiza la pantalla