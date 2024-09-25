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
    ramaD = pygame.image.load("assets/images/fondos/ramaDer.png")
    ramaI = pygame.image.load("assets/images/fondos/ramaIzq.png")

    # Carga la imagen que se mostrará al finalizar el tiempo
    imagen_final = pygame.image.load("assets/images/fondos/gameover.jpg").convert()  # Asegúrate de que esta imagen existe
    imagen_final = pygame.transform.scale(imagen_final, (constantes.anchoVentana, constantes.altoVentana))  # Escala la imagen al tamaño de la ventana
    imagen_final.set_colorkey(constantes.blanco)

    boton_pausa = pygame.image.load("assets/images/menu/btnPausa.png").convert_alpha()
    boton_pausa_rect = boton_pausa.get_rect(center=(constantes.anchoVentana // 2, 50))  # Coloca el botón en la parte superior derecha

    # Llama a la función sonido del archivo sound
    sound.sound_lvl_1()

    reloj = pygame.time.Clock()

    # Grupo de sprites, instanciación del objeto jugador
    sprites = pygame.sprite.Group()
    ramas = pygame.sprite.Group()

    # Ejemplo de posiciones de las ramas (ajusta según tu diseño)
    posiciones_ramas = [340, 450]  # Alturas Y de las ramas (ajusta según tus imágenes)

    # Crea un ítem en cada posición de rama
    for posicion in posiciones_ramas:
        alimento = aitems(posicion)
        sprites.add(alimento)

    # Instanciar ramas y agregarlas al grupo de ramas
    ramaD = Rama(310, 430, "assets/images/fondos/ramaDer.png")
    ramaI = Rama(-10, 320, "assets/images/fondos/ramaIzq.png")
    ramas.add(ramaD, ramaI)
    sprites.add(ramaD, ramaI)

    jugador = player(ramas)
    sprites.add(jugador)

    # Temporizador
    tiempo_total = 30
    tiempo_restante = tiempo_total
    fuente = pygame.font.SysFont(None, 40)

    en_pausa = False

    run = True
    desplazamiento_y = 0

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
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if boton_pausa_rect.collidepoint(mouse_pos):
                    en_pausa = not en_pausa
                    print("Pausa:", en_pausa)  # Mensaje de depuración para verificar si se detecta el clic

        if not en_pausa:
            # Desplazamiento en y cuando el jugador sube
            if jugador.rect.top <= constantes.altoVentana // 4:
                desplazamiento_y = constantes.altoVentana // 4 - jugador.rect.top

                # Mover todos los sprites hacia abajo cuando el jugador sube
                for sprite in sprites:
                    sprite.rect.y += desplazamiento_y

            # Actualiza el temporizador solo si no está en pausa
            if tiempo_restante > 0:
                tiempo_restante -= 1 / constantes.fps

        # Dibujar el fondo ajustado al desplazamiento
        pantalla.blit(fondo, (0, desplazamiento_y % constantes.altoVentana - constantes.altoVentana))
        pantalla.blit(fondo, (0, desplazamiento_y % constantes.altoVentana))

        # Dibujo el suelo y las ramas
        pantalla.blit(sueloPasto, (0, 360 + desplazamiento_y))
        pantalla.blit(ramaD, (331, 450 + desplazamiento_y))
        pantalla.blit(ramaI, (-10, 340 + desplazamiento_y))

        # Mostrar el botón de pausa
        pantalla.blit(boton_pausa, boton_pausa_rect.topleft)

        # Actualización de sprites
        if not en_pausa:  # Solo actualizar los sprites si no está en pausa
            sprites.update()

        # Dibuja al personaje y los sprites en pantalla
        sprites.draw(pantalla)

        # Si está en pausa, dibuja un rectángulo oscuro sobre la pantalla
        if en_pausa:
            # Crear un rectángulo negro semi-transparente
            sombra = pygame.Surface((constantes.anchoVentana, constantes.altoVentana))
            sombra.set_alpha(128)  # Ajustar la transparencia (0-255)
            sombra.fill((0, 0, 0))  # Color negro
            pantalla.blit(sombra, (0, 0))

            # Mostrar mensaje de pausa
            fuente_pausa = pygame.font.SysFont(None, 75)
            texto_pausa = fuente_pausa.render('PAUSA', True, constantes.blanco)
            texto_rect = texto_pausa.get_rect(center=(constantes.anchoVentana // 2, constantes.altoVentana // 2))
            pantalla.blit(texto_pausa, texto_rect)

        # Si el temporizador llega a cero, muestra la pantalla de Game Over
        if tiempo_restante <= 0:
            pantalla.blit(imagen_final, (0, 0))
            pygame.display.update()
            pygame.time.delay(5000)
            run = False

        # Calcular minutos y segundos
        minutos = int(tiempo_restante // 60)
        segundos = int(tiempo_restante % 60)

        # Formatear el tiempo como MM:SS
        tiempo_formateado = f'{minutos:02}:{segundos:02}'

        # Mostrar el tiempo restante en pantalla en la esquina superior derecha
        texto_tiempo = fuente.render(tiempo_formateado, True, constantes.blanco)
        pantalla.blit(texto_tiempo, (constantes.anchoVentana - 100, 10))  # Ajusta la posición del temporizador

        # Actualizar la pantalla
        pygame.display.update()

        # Controlar el frame rate
        reloj.tick(constantes.fps)

    pygame.quit()

# Ejecutar el juego
if __name__ == "__main__": # Si el archivo es ejecutado directamente
    play() # Llama a la función play
