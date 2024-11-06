import pygame
import random
import constantes
import sound
from personaje import player
from items import aitems  # Importar los ítems
from rama import Rama  # Asegúrate de importar la clase Rama
from personajef import playerf  # Importar el personaje femenino

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

    # Imágenes de estado final del juego
    imagen_final = pygame.image.load("assets/images/fondos/gameover.jpg").convert()
    imagen_final = pygame.transform.scale(imagen_final, (constantes.anchoVentana, constantes.altoVentana))
    imagen_win = pygame.image.load("assets/images/fondos/youwin.jpg").convert()
    imagen_win = pygame.transform.scale(imagen_win, (constantes.anchoVentana, constantes.altoVentana))

    boton_pausa = pygame.image.load("assets/images/menu/btnPausa.png").convert_alpha()
    boton_pausa_rect = boton_pausa.get_rect(center=(452, 55))

    # Llama a la función sonido del archivo sound
    sound.sound_lvl_1()

    reloj = pygame.time.Clock()

    # Grupo de sprites e instanciación de jugador
    sprites = pygame.sprite.Group()
    ramas = pygame.sprite.Group()
    items = pygame.sprite.Group()

    # Generación de ramas e ítems
    ramas_con_items = 0
    items_generados = 0
    i = 0
    while items_generados < 12:
        x_pos = -10 if i % 2 == 0 else 331
        rama = Rama(x_pos, 500 - i * 120, "assets/images/fondos/ramaDer.png" if i % 2 == 0 else "assets/images/fondos/ramaIzq.png")
        ramas.add(rama)
        sprites.add(rama)

        if random.randint(0, 1) == 1 and items_generados < 12:
            item = aitems(rama.rect)
            items.add(item)
            sprites.add(item)
            items_generados += 1
            ramas_con_items += 1
        i += 1

    jugador = playerf(ramas)
    sprites.add(jugador)

    cantidad_items_recogidos = 0
    tiempo_total = 30
    tiempo_restante = tiempo_total
    fuente = pygame.font.SysFont(None, 40)

    en_pausa = False
    run = True
    desplazamiento_y = 0
    y = 0

    # Posición inicial fija para el suelo
    suelo_y = 360

    while run:
        # Fondo en constante movimiento
        yRelativa = y % fondo.get_rect().height
        pantalla.blit(fondo, (0, yRelativa - fondo.get_rect().height))
        if yRelativa < constantes.altoVentana:
            pantalla.blit(fondo, (0, 0))
        y += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if boton_pausa_rect.collidepoint(mouse_pos):
                    en_pausa = not en_pausa
                    print("Pausa:", en_pausa)

        if not en_pausa:
            # Control de movimiento del jugador
            keys = pygame.key.get_pressed()
            jugador.velocidad_x = -5 if keys[pygame.K_LEFT] else 5 if keys[pygame.K_RIGHT] else 0
            
            # Actualiza el personaje
            jugador.update()

            # Verificar si el jugador ha tocado el margen inferior de la pantalla
            if jugador.rect.bottom >= constantes.altoVentana:  # Si el personaje cae al fondo de la pantalla
                pantalla.blit(imagen_final, (0, 0))  # Muestra imagen de Game Over
                pygame.display.update()
                pygame.time.delay(3000)  # Pausa breve antes de finalizar
                run = False  # Finaliza el juego

            # Desplazamiento vertical cuando el jugador sube
            if jugador.rect.top <= constantes.altoVentana // 4:
                desplazamiento_y = constantes.altoVentana // 4 - jugador.rect.top
                for sprite in sprites:
                    sprite.rect.y += desplazamiento_y

                # Mueve el suelo hacia abajo con el desplazamiento
                suelo_y += desplazamiento_y

            # Colisiones entre el jugador y los ítems
            items_colisionados = pygame.sprite.spritecollide(jugador, items, True)
            for item in items_colisionados:
                cantidad_items_recogidos += 1

            if cantidad_items_recogidos == 10:
                pantalla.blit(imagen_win, (0, 0))
                pygame.display.update()
                pygame.time.delay(5000)
                run = False

            # Actualiza el temporizador si no está en pausa
            if tiempo_restante > 0:
                tiempo_restante -= 1 / constantes.fps

        # Dibujar suelo ajustado a la posición variable
        if suelo_y < constantes.altoVentana:  # Solo dibuja el suelo si está visible en pantalla
            pantalla.blit(sueloPasto, (0, suelo_y))

        # Actualización de sprites
        if not en_pausa:
            sprites.update()

        # Dibuja el personaje y los sprites
        sprites.draw(pantalla)

        # Mostrar el botón de pausa
        pantalla.blit(boton_pausa, boton_pausa_rect.topleft)

        # Si está en pausa, muestra una sombra sobre la pantalla
        if en_pausa:
            sombra = pygame.Surface((constantes.anchoVentana, constantes.altoVentana))
            sombra.set_alpha(128)
            sombra.fill((0, 0, 0))
            pantalla.blit(sombra, (0, 0))

            # Mostrar mensaje de pausa
            fuente_pausa = pygame.font.SysFont(None, 75)
            texto_pausa = fuente_pausa.render('PAUSA', True, constantes.blanco)
            texto_rect = texto_pausa.get_rect(center=(constantes.anchoVentana // 2, constantes.altoVentana // 2))
            pantalla.blit(texto_pausa, texto_rect)

        # Muestra pantalla de Game Over si el tiempo se acaba
        if tiempo_restante <= 0:
            pantalla.blit(imagen_final, (0, 0))
            pygame.display.update()
            pygame.time.delay(5000)
            run = False

        # Formato del tiempo restante
        minutos, segundos = divmod(int(tiempo_restante), 60)
        tiempo_formateado = f'{minutos:02}:{segundos:02}'
        texto_tiempo = fuente.render(tiempo_formateado, True, constantes.blanco)
        pantalla.blit(texto_tiempo, (10, 10))

        # Mostrar la cantidad de ítems recogidos
        texto_cantidad = fuente.render(f'Items: {cantidad_items_recogidos}', True, constantes.blanco)
        pantalla.blit(texto_cantidad, (10, 50))

        # Actualizar pantalla y controlar frame rate
        pygame.display.update()
        reloj.tick(constantes.fps)

    pygame.quit()

# Ejecutar el juego
if __name__ == "__main__":
    play()
