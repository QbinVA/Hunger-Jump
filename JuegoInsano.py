#Importo pygame y sistema
import pygame
import sys
#Importo la pantalla
import pygame.display
from pygame.locals import *
from button import Button

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
W,H = 500, 750
pantalla = pygame.display.set_mode((W, H))
fps = 90
reloj = pygame.time.Clock()

#Inserto un caption
pygame.display.set_caption('Hungry Jump')

#Declaro e inserto el icono
icono = pygame.image.load("images/banana.png")
pygame.display.set_icon(icono)

#Declaro e inserto el fondo
fondo = pygame.image.load("images/fondok.jpg").convert()
x = 0

#Ciclo infinito
while True:
    for event in pygame.event.get():
        if event.type == quit:
            pygame.quit()
            sys.exit()
    xRelativa = x % fondo.get_rect().width
    pantalla.blit(fondo, (xRelativa - fondo.get_rect().width, 0))
    if xRelativa < W:
        pantalla.blit(fondo, (xRelativa, 0))
    x -= 1
    pygame.display.update() #Se actualiza la pantalla
    reloj.tick(fps)