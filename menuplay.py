import pygame
import random
import constantes
import sound
from personaje import player
from items import aitems  # Importar los ítems
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
    imagen_final = pygame.image.load("assets/images/fondos/gameover.jpg").convert()
    imagen_final = pygame.transform.scale(imagen_final, (constantes.anchoVentana, constantes.altoVentana))
    imagen_final.set_colorkey(constantes.blanco)

    boton_pausa = pygame.image.load("assets/images/menu/btnPausa.png").convert_alpha()
    boton_pausa_rect = boton_pausa.get_rect(center=(452, 55))

    # Llama a la función sonido del archivo sound
    sound.sound_lvl_1()

    reloj = pygame.time.Clock()

    # Grupo de sprites, instanciación del objeto jugador
    sprites = pygame.sprite.Group()
    ramas = pygame.sprite.Group()

    # Añade las ramas alternando entre izquierda y derecha
    for i in range(20):  # Generar 20 ramas como ejemplo
        if i % 2 == 0:
            rama = Rama(-10, 500 - i * 120, "assets/images/fondos/ramaDer.png")  # Rama derecha
        else:
            rama = Rama(331, 500 - i * 120, "assets/images/fondos/ramaIzq.png")  # Rama izquierda
        ramas.add(rama)
        sprites.add(rama)

    jugador = player(ramas)
    sprites.add(jugador)

    # Añadir ítems a las ramas (un ítem por rama como máximo)
    items = pygame.sprite.Group()
    ramas_con_items = set()  # Para rastrear qué ramas ya tienen un ítem
    for rama in ramas:
        if random.randint(0, 1) and rama not in ramas_con_items:  # Probabilidad de 50% y verificar si la rama ya tiene un ítem
            item = aitems(rama.rect)  # Coloca el ítem en la rama
            items.add(item)
            sprites.add(item)
            ramas_con_items.add(rama)  # Marcar que esta rama ya tiene un ítem

    # Contador para almacenar la cantidad de ítems recogidos
    cantidad_items_recogidos = 0

    # Temporizador
    tiempo_total = 30
    tiempo_restante = tiempo_total
    fuente = pygame.font.SysFont(None, 40)

    en_pausa = False

    run = True
    desplazamiento_y = 0
    y = 0  # Asegúrate de inicializar 'y' para el desplazamiento del fondo

    while run:
        # Bucle de fondo en constante movimiento
        yRelativa = y % fondo.get_rect().height
        pantalla.blit(fondo, (0, yRelativa - fondo.get_rect().height))
        if yRelativa < constantes.altoVentana:
            pantalla.blit(fondo, (0, yRelativa))
        y += 1

        pantalla.blit(sueloPasto, (0, 360))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if boton_pausa_rect.collidepoint(mouse_pos):
                    en_pausa = not en_pausa
                    print("Pausa:", en_pausa)

        if not en_pausa:
            # Controlar el movimiento del jugador
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                jugador.velocidad_x = -5
            elif keys[pygame.K_RIGHT]:
                jugador.velocidad_x = 5
            else:
                jugador.velocidad_x = 0
            
            # Actualiza el personaje
            jugador.update()

            # Desplazamiento en y cuando el jugador sube
            if jugador.rect.top <= constantes.altoVentana // 4:
                desplazamiento_y = constantes.altoVentana // 4 - jugador.rect.top

                # Mueve todos los sprites hacia abajo cuando el jugador sube
                for sprite in sprites:
                    sprite.rect.y += desplazamiento_y

            # Detectar colisiones entre el jugador y los ítems
            items_colisionados = pygame.sprite.spritecollide(jugador, items, True)
            for item in items_colisionados:
                cantidad_items_recogidos += 1  # Incrementa el contador

            # Actualiza el temporizador solo si no está en pausa
            if tiempo_restante > 0:
                tiempo_restante -= 1 / constantes.fps

        # Dibujar el fondo ajustado al desplazamiento
        pantalla.blit(fondo, (0, desplazamiento_y % constantes.altoVentana - constantes.altoVentana))
        pantalla.blit(fondo, (0, desplazamiento_y % constantes.altoVentana))

        # Dibuja el suelo y las ramas
        pantalla.blit(sueloPasto, (0, 360 + desplazamiento_y))

        # Actualización de sprites
        if not en_pausa:
            sprites.update()

        # Dibuja al personaje y los sprites en pantalla
        sprites.draw(pantalla)

        # Mostrar el botón de pausa
        pantalla.blit(boton_pausa, boton_pausa_rect.topleft)

        # Si está en pausa, dibuja un rectángulo oscuro sobre la pantalla
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
    
        pantalla.blit(texto_tiempo, (10, 10))

        # Mostrar la cantidad de ítems recogidos en la parte inferior de la pantalla
        texto_cantidad = fuente.render(f'Ítems recogidos: {cantidad_items_recogidos}', True, constantes.blanco)
        pantalla.blit(texto_cantidad, (10, 50))

        # Actualizar la pantalla
        pygame.display.update()

        # Controlar el frame rate
        reloj.tick(constantes.fps)

    pygame.quit()

# Ejecutar el juego
if __name__ == "__main__":
    play()
