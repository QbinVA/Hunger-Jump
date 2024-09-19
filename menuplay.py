import pygame
import constantes

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

    # Redimensionar imágenes del personaje
    ancho_personaje = 250  # Ancho del personaje
    alto_personaje = 250  # Altura del personaje

    quieto = pygame.image.load("assets/images/personajes/niño0.png") # Importo la imagen del niño quieto
    quieto = pygame.transform.scale(quieto, (ancho_personaje, alto_personaje)) # La escalo al tamaño preestablecido

    saltaDer = [pygame.image.load('assets/images/personajes/niño1.png') for _ in range(4)] # Importo la imagen del niño saltando a la derecha
    saltaDer = [pygame.transform.scale(img, (ancho_personaje, alto_personaje)) for img in saltaDer] # La escalo al tamaño preestablecido

    saltaIzq = [pygame.image.load('assets/images/personajes/niño1i.png') for _ in range(4)] # Importo la imagen del niño saltando a la izquierda
    saltaIzq = [pygame.transform.scale(img, (ancho_personaje, alto_personaje)) for img in saltaIzq] # La escalo al tamaño preestablecido

    # Definir las variables de posicion
    px = 0  # Posicion en el eje x
    py = 510  # Posicion en el eje y

    # Velocidad a la que se mueve el personaje
    velocidad = 7
    reloj = pygame.time.Clock()

    # Variables de salto
    en_salto = True # Salto siempre habilitado
    cuentaSalto = 30 # Pixeles que salta por cada segundo
    velocidad_salto = 6 # Velocidad de salto
    direccion_salto = -1  # -1 para subir, 1 para bajar

    # Variables de dirección
    izquierda = False # Falso para que no esté en movimiento continuo
    derecha = False # Falso para que no esté en movimiento continuo

    # Cuenta los pasos para cambiar las imagenes de movimiento
    cuentaPasos = 0

    def recarga_pantalla():
        # Declara variables
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
        elif en_salto:
            pantalla.blit(quieto, (int(px), int(py)))
        else:
            pantalla.blit(quieto, (int(px), int(py)))

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

        # Manejo de teclas
        keys = pygame.key.get_pressed() # Verifica si alguna tecla está presionada

        # Tecla LEFT - Movimiento a la izquierda
        if keys[pygame.K_LEFT] and px > -70:  # Margen izquierdo del personaje
            px -= velocidad
            izquierda = True
            derecha = False

        # Tecla RIGHT - Movimiento a la derecha
        elif keys[pygame.K_RIGHT] and px < 310:  # Margen derecho del personaje
            px += velocidad
            izquierda = False
            derecha = True

        # Personaje quieto
        else:
            izquierda = False
            derecha = False

        # Lógica del salto
        if en_salto:
            py += velocidad_salto * direccion_salto
            cuentaSalto -= 1

            if cuentaSalto <= 0:
                # Cambio de dirección al llegar al punto más alto del salto
                direccion_salto *= -1
                cuentaSalto = 30  # Pixeles que salta

            if py >= 470:
                # Volver al suelo
                py = 470
                en_salto = False
                cuentaSalto = 30  # Pixeles que baja

        # Alternar salto
        if not en_salto:
            en_salto = True
            cuentaSalto = 30 # Pixeles que salta


        # Llamada a la función
        recarga_pantalla()

        # Actualizar la pantalla
        pygame.display.update()

        # Controlar el frame rate
        reloj.tick(constantes.fps)

    # Salida del juego
    pygame.quit()


if __name__ == "__main__":
    play()
