import pygame
import constantes

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
    ramaD = pygame.image.load("assets/images/fondos/ramaDer.png")
    ramaI = pygame.image.load("assets/images/fondos/ramaIzq.png")

    # Redimensionar imágenes del personaje
    ancho_personaje = 250
    alto_personaje = 250  # Ajusta según sea necesario

    quieto = pygame.image.load("assets/images/personajes/niño0.png")
    quieto = pygame.transform.scale(quieto, (ancho_personaje, alto_personaje))

    saltaDer = [pygame.image.load('assets/images/personajes/niño1.png') for _ in range(4)]
    saltaDer = [pygame.transform.scale(img, (ancho_personaje, alto_personaje)) for img in saltaDer]

    saltaIzq = [pygame.image.load('assets/images/personajes/niño1i.png') for _ in range(4)]
    saltaIzq = [pygame.transform.scale(img, (ancho_personaje, alto_personaje)) for img in saltaIzq]

    # Definir las variables de posicion
    px = 0  # Posicion en el eje x
    py = 470  # Posicion en el eje y

    velocidad = 7
    reloj = pygame.time.Clock()

    # Variables de salto
    salto = True
    cuentaSalto = 20

    # Variables de dirección
    izquierda = False
    derecha = False

    # Pasos
    cuentaPasos = 0

    def recarga_pantalla():
        nonlocal cuentaPasos, izquierda, derecha, px, py, saltaIzq, saltaDer, quieto

        # Contador de pasos
        cuentaPasos = (cuentaPasos + 1) % 4

        # Movimiento a la izquierda
        if izquierda:
            pantalla.blit(saltaIzq[cuentaPasos], (int(px), int(py)))

        # Movimiento a la derecha
        elif derecha:
            pantalla.blit(saltaDer[cuentaPasos], (int(px), int(py)))

        # Personaje quieto
        elif salto:
            pantalla.blit(quieto, (int(px), int(py)))
        else:
            pantalla.blit(quieto, (int(px), int(py)))

    run = True
    y = 0

    while run:
        # Dibujar el fondo
        yRelativa = y % fondo.get_rect().height
        pantalla.blit(fondo, (0, yRelativa - fondo.get_rect().height))
        if yRelativa < constantes.altoVentana:
            pantalla.blit(fondo, (0, yRelativa))
        y += 1

        # Dibujar suelo y ramas
        pantalla.blit(sueloPasto, (0, 360))
        pantalla.blit(ramaD, (310, 430))
        pantalla.blit(ramaI, (-10, 320))

        # Verificar los eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Manejo de teclas
        keys = pygame.key.get_pressed()

        # Tecla LEFT - Movimiento a la izquierda
        if keys[pygame.K_LEFT] and px > -70:  # Permite moverse más allá del borde izquierdo
            px -= velocidad
            izquierda = True
            derecha = False

        # Tecla RIGHT - Movimiento a la derecha
        elif keys[pygame.K_RIGHT] and px < 310:  # Permite moverse más allá del borde derecho
            px += velocidad
            izquierda = False
            derecha = True

        # Personaje quieto
        else:
            izquierda = False
            derecha = False


        # Llamada a la función para actualizar la pantalla
        recarga_pantalla()

        # Actualizar la pantalla
        pygame.display.update()

        # Controlar el frame rate
        reloj.tick(constantes.fps)

    # Salida del juego
    pygame.quit()

if __name__ == "__main__":
    play()
