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

    # Carga la imagen que se mostrará al finalizar el tiempo
    imagen_final = pygame.image.load("assets/images/fondos/gameover.jpg").convert()  # Asegúrate de que esta imagen existe
    imagen_final = pygame.transform.scale(imagen_final, (constantes.anchoVentana, constantes.altoVentana))  # Escala la imagen al tamaño de la ventana
    imagen_final.set_colorkey(constantes.blanco)

    # Carga la imagen del botón de pausa
    boton_pausa = pygame.image.load("assets/images/menu/btnPausa.png").convert_alpha()  # Usa convert_alpha para mantener la transparencia
    boton_pausa_rect = boton_pausa.get_rect(center=(constantes.anchoVentana // 2, 50))  # Centra el botón en la parte superior

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

    # Temporizador
    tiempo_total = 30  # Tiempo total en segundos
    tiempo_restante = tiempo_total  # Tiempo restante
    fuente = pygame.font.SysFont(None, 40)  # Fuente para mostrar el temporizador

    # Estado del juego
    en_pausa = False  # Indica si el juego está en pausa

    # Mantiene el bucle
    run = True
    y = 0

    while run:
        # Bucle de fondo en constante movimiento
        yRelativa = y % fondo.get_rect().height
        pantalla.blit(fondo, (0, yRelativa - fondo.get_rect().height))
        if yRelativa < constantes.altoVentana:
            pantalla.blit(fondo, (0, yRelativa))
        y += 1

        pantalla.blit(sueloPasto, (0, 360))
        
        # Mostrar el botón de pausa
        pantalla.blit(boton_pausa, boton_pausa_rect.topleft)  # Dibuja el botón en la pantalla

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Cierra la ventana
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:  # Verifica si se hace clic con el ratón
                mouse_pos = pygame.mouse.get_pos()  # Obtiene la posición del ratón
                if boton_pausa_rect.collidepoint(mouse_pos):  # Comprueba si se hace clic en el botón
                    en_pausa = not en_pausa  # Cambia el estado de pausa

        if not en_pausa:  # Si el juego no está en pausa
            # Actualización de sprites
            sprites.update()

            # Dibuja al personaje en pantalla
            sprites.draw(pantalla)

            # Actualiza el temporizador
            if tiempo_restante > 0:
                tiempo_restante -= 1 / constantes.fps  # Disminuye el tiempo restante
            else:
                # Si el tiempo se ha terminado, mostrar la imagen final
                pantalla.blit(imagen_final, (0, 0))  # Dibuja la imagen en la pantalla
                pygame.display.update()  # Actualiza la pantalla
                pygame.time.delay(5000)  # Espera 5 segundos antes de terminar
                run = False  # Sal del bucle

            # Calcular minutos y segundos
            minutos = int(tiempo_restante // 60)
            segundos = int(tiempo_restante % 60)

            # Formatear el tiempo como MM:SS
            tiempo_formateado = f'{minutos:02}:{segundos:02}'

            # Mostrar el tiempo restante en pantalla en la esquina superior derecha
            texto_tiempo = fuente.render(tiempo_formateado, True, constantes.blanco)
            pantalla.blit(texto_tiempo, (constantes.anchoVentana - 80, 10))  # Dibuja el texto en la esquina superior derecha

        else:  # Si el juego está en pausa
            # Dibuja un rectángulo semitransparente para oscurecer la pantalla
            overlay = pygame.Surface((constantes.anchoVentana, constantes.altoVentana))
            overlay.set_alpha(128)  # Ajusta la transparencia (0-255)
            overlay.fill((0, 0, 0))  # Color negro
            pantalla.blit(overlay, (0, 0))  # Dibuja el overlay en la pantalla

            # Dibuja los sprites y el temporizador en pausa
            sprites.draw(pantalla)  # Dibuja los sprites (el jugador y los alimentos)
            # Mostrar el tiempo restante en pantalla en la esquina superior derecha
            texto_tiempo = fuente.render(tiempo_formateado, True, constantes.blanco)
            pantalla.blit(texto_tiempo, (constantes.anchoVentana - 80, 10))  # Dibuja el texto en la esquina superior derecha

        # Actualizar la pantalla
        pygame.display.update()

        # Controlar el frame rate
        reloj.tick(constantes.fps)

    # Salida del juego
    pygame.quit()

# Ejecutar el juego
if __name__ == "__main__": # Si el archivo es ejecutado directamente
    play() # Llama a la función play