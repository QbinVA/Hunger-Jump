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
    game_over = False
    victory = False
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
                
                # Manejo de los botones en la pantalla de Game Over o Victoria
                if game_over or victory:
                    if boton_reintentar_rect.collidepoint(mouse_pos):
                        sound.sound_clic2()  # Reproducir sonido de clic
                        play()  # Reiniciar el juego
                    elif boton_salir_rect.collidepoint(mouse_pos):
                        sound.sound_clic1()  # Reproducir sonido de clic
                        from principiante import levels_p  # Importa solo cuando es necesario
                        levels_p()  # Llama a la pantalla de selección de niveles
                        return  # Salir de la función play actual

        if not en_pausa and not game_over and not victory:
            # Control de movimiento del jugador
            keys = pygame.key.get_pressed()
            jugador.velocidad_x = -5 if keys[pygame.K_LEFT] else 5 if keys[pygame.K_RIGHT] else 0
            
            # Actualiza el personaje
            jugador.update()

            # Verificar si el jugador ha tocado el margen inferior de la pantalla
            if jugador.rect.bottom >= constantes.altoVentana:
                game_over = True

            # Desplazamiento vertical cuando el jugador sube
            if jugador.rect.top <= constantes.altoVentana // 4:
                desplazamiento_y = constantes.altoVentana // 4 - jugador.rect.top
                for sprite in sprites:
                    sprite.rect.y += desplazamiento_y
                suelo_y += desplazamiento_y

            # Colisiones entre el jugador y los ítems
            items_colisionados = pygame.sprite.spritecollide(jugador, items, True)
            for item in items_colisionados:
                cantidad_items_recogidos += 1
                item.reproducir_sonido()

            if cantidad_items_recogidos == 10:
                victory = True
                sound.sound_win1()

            if tiempo_restante > 0:
                tiempo_restante -= 1 / constantes.fps

        # Dibujar suelo ajustado a la posición variable
        if suelo_y < constantes.altoVentana:
            pantalla.blit(sueloPasto, (0, suelo_y))

        # Actualización de sprites
        if not en_pausa:
            sprites.update()

        sprites.draw(pantalla)
        pantalla.blit(boton_pausa, boton_pausa_rect.topleft)

        # Oscurecer pantalla y mostrar mensaje de pausa si está en pausa
        if en_pausa:
            sombra = pygame.Surface((constantes.anchoVentana, constantes.altoVentana))
            sombra.set_alpha(128)
            sombra.fill((0, 0, 0))
            pantalla.blit(sombra, (0, 0))
            texto_pausa = fuente.render("Pausa", True, constantes.blanco)
            pantalla.blit(texto_pausa, texto_pausa.get_rect(center=(constantes.anchoVentana // 2, constantes.altoVentana // 2)))

        # Pantalla de Game Over o Victoria
        if game_over or victory:
            sombra = pygame.Surface((constantes.anchoVentana, constantes.altoVentana))
            sombra.set_alpha(128)
            sombra.fill((0, 0, 0))
            pantalla.blit(sombra, (0, 0))

            fuente_final = pygame.font.SysFont(None, 75)
            texto_final = fuente_final.render('¡Ganaste!' if victory else '¡Perdiste!', True, constantes.blanco)
            pantalla.blit(texto_final, texto_final.get_rect(center=(constantes.anchoVentana // 2, constantes.altoVentana // 2 - 50)))

            # Crear y mostrar botones de reintentar y salir
            boton_reintentar = pygame.Surface((165, 50))
            boton_reintentar.fill((255, 0, 0))
            boton_reintentar_rect = boton_reintentar.get_rect(center=(constantes.anchoVentana // 2 - 100, constantes.altoVentana // 2 + 50))
            pantalla.blit(boton_reintentar, boton_reintentar_rect)
            pantalla.blit(fuente.render('Reintentar', True, constantes.blanco), (boton_reintentar_rect.x + 10, boton_reintentar_rect.y + 10))

            boton_salir = pygame.Surface((165, 50))
            boton_salir.fill((255, 0, 0))
            boton_salir_rect = boton_salir.get_rect(center=(constantes.anchoVentana // 2 + 100, constantes.altoVentana // 2 + 50))
            pantalla.blit(boton_salir, boton_salir_rect)
            pantalla.blit(fuente.render('Salir', True, constantes.blanco), (boton_salir_rect.x + 35, boton_salir_rect.y + 10))

        minutos, segundos = divmod(int(tiempo_restante), 60)
        tiempo_formateado = f'{minutos:02}:{segundos:02}'
        texto_tiempo = fuente.render(tiempo_formateado, True, constantes.blanco)
        pantalla.blit(texto_tiempo, (10, 10))

        texto_cantidad = fuente.render(f'Items: {cantidad_items_recogidos}', True, constantes.blanco)
        pantalla.blit(texto_cantidad, (10, 50))

        pygame.display.update()
        reloj.tick(constantes.fps)

    pygame.quit()

if __name__ == "__main__":
    play()
 