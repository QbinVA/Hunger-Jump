import pygame
from pygame.locals import *

pygame.init()

# Personaje
quieto = pygame.image.load('assets/images/items/banana.png')
caminaDer = [pygame.image.load('assets/images/items/cherry.png')]  # Solo una imagen por ahora
caminaIzq = [pygame.image.load('assets/images/items/cherry.png')]  # Solo una imagen por ahora
salta = [pygame.image.load('assets/images/items/banana.png'),
         pygame.image.load('assets/images/items/banana.png')]

# Posición y tamaño del personaje
px = 400
py = 500
ancho = 10
velocidad = 10

# Variables de salto
salto = True  # El personaje está saltando al principio
cuentaSalto = 20  # Aumentamos este valor para controlar la altura del salto

# Variables de dirección
izquierda = False
derecha = False
cuentaPasos = 0

# Duración del salto (1.5 segundos a 90 FPS)
duracion_salto = 1.5 * fps  # Total de frames para completar un salto

def recarga_pantalla():
    global cuentaPasos
    global y  # Ahora usamos `y` para el movimiento vertical del fondo

    # Mueve el fondo hacia arriba solo si el personaje está saltando
    if salto:
        y += 1  # Mueve el fondo hacia arriba cuando el personaje salta

    # Calcula la posición relativa del fondo
    y_relativa = y % fondo.get_rect().height
    pantalla.blit(fondo, (0, y_relativa - fondo.get_rect().height))  # Desplaza el fondo verticalmente
    if y_relativa < H:
        pantalla.blit(fondo, (0, y_relativa))

    # Control de animación del personaje
    if cuentaPasos + 1 >= 1:
        cuentaPasos = 0

    if izquierda:
        pantalla.blit(caminaIzq[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1
    elif derecha:
        pantalla.blit(caminaDer[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1
    elif salto + 1 >= 2:
        pantalla.blit(salta[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1
    else:
        pantalla.blit(quieto, (int(px), int(py)))

ejecuta = True

while ejecuta:
    reloj.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecuta = False

    keys = pygame.key.get_pressed()

    # Movimiento a la izquierda
    if keys[pygame.K_LEFT] and px > velocidad:
        px -= velocidad
        izquierda = True
        derecha = False
    # Movimiento a la derecha
    elif keys[pygame.K_RIGHT] and px < W - velocidad - ancho:
        px += velocidad
        izquierda = False
        derecha = True
    else:
        izquierda = False
        derecha = False
        cuentaPasos = 0

    # Ciclo continuo de salto con mayor altura pero manteniendo 1.5 segundos
    if salto:
        if cuentaSalto >= -20:
            # Aumentamos el multiplicador para saltar más alto sin cambiar la duración total
            py -= (cuentaSalto * abs(cuentaSalto)) * 0.05  
            cuentaSalto -= 1
        else:
            cuentaSalto = 20  # Reinicia el ciclo de salto
    else:
        salto = True  # Siempre se está en modo de salto

    pygame.display.update()
    recarga_pantalla()

pygame.quit()