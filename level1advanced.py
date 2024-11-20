import pygame
import random
import constantes
import sound
from personaje import player
from itemavanzado import SaludableItem, ChatarraItem
from rama import Rama

# Función para cargar la fuente estilo pixel
def get_pixel_font(size):
    return pygame.font.Font("assets/Font/PressStart2P-Regular.ttf", size)

# Función para renderizar texto con borde
def render_text_with_outline(font, text, text_color, outline_color, position, surface):
    x, y = position
    offsets = [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, -1), (0, 1), (-1, 0), (1, 0)]
    for dx, dy in offsets:
        outline_surface = font.render(text, True, outline_color)
        surface.blit(outline_surface, (x + dx, y + dy))
    main_surface = font.render(text, True, text_color)
    surface.blit(main_surface, (x, y))

def play():
    # Define la cantidad de ítems necesarios para ganar
    OBJETIVO_ITEMS = 20

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
    game_over_image = pygame.image.load("assets/images/fondos/gameoverniño.png").convert()
    victory_image = pygame.image.load("assets/images/fondos/gameoverniño.png").convert()
    boton_pausa = pygame.image.load("assets/images/menu/btnPausa.png").convert_alpha()
    boton_pausa_rect = boton_pausa.get_rect(center=(452, 55))

    # Carga de imágenes para los botones
    boton_reintentar_image = pygame.image.load("assets/images/menu/reiniciar.png").convert_alpha()
    boton_salir_image = pygame.image.load("assets/images/menu/home.png").convert_alpha()
    boton_reintentar_rect = boton_reintentar_image.get_rect(center=(constantes.anchoVentana // 2, 270))
    boton_salir_rect = boton_salir_image.get_rect(center=(constantes.anchoVentana // 2, 500))

    # Llama a la función sonido del archivo sound
    sound.sound_lvl_1()

    reloj = pygame.time.Clock()

    # Grupo de sprites e instanciación de jugador
    sprites = pygame.sprite.Group()
    ramas = pygame.sprite.Group()
    items = pygame.sprite.Group()

    # Generación de ramas e ítems
    items_generados = 0
    i = 0
    while items_generados < OBJETIVO_ITEMS:
        x_pos = -10 if i % 2 == 0 else 331
        rama = Rama(
            x_pos,
            500 - i * 120,
            "assets/images/fondos/ramaDer.png" if i % 2 == 0 else "assets/images/fondos/ramaIzq.png"
        )
        ramas.add(rama)
        sprites.add(rama)

        # Generar ítem con mayor probabilidad de ser saludable
        if random.randint(0, 1) == 1:
            if random.randint(0, 9) < 7:  # 70% probabilidad de ítem saludable
                item = SaludableItem(rama.rect)
            else:  # 30% probabilidad de ítem chatarra
                item = ChatarraItem(rama.rect)
            items.add(item)
            sprites.add(item)
            items_generados += 1

        i += 1

    jugador = player(ramas)
    sprites.add(jugador)

    cantidad_items_recogidos = 0
    tiempo_total = 25
    tiempo_restante = tiempo_total

    en_pausa = False
    game_over = False
    victory = False
    run = True
    desplazamiento_y = 0
    y = 0
    suelo_y = 360

    while run:
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
                if game_over or victory:
                    if boton_reintentar_rect.collidepoint(mouse_pos):
                        sound.sound_clic2()
                        play()
                    elif boton_salir_rect.collidepoint(mouse_pos):
                        sound.sound_clic1()
                        from avanzado import levels_a
                        levels_a()
                        return

        if not en_pausa and not game_over and not victory:
            keys = pygame.key.get_pressed()
            jugador.velocidad_x = -5 if keys[pygame.K_LEFT] else 5 if keys[pygame.K_RIGHT] else 0
            jugador.update()

            if jugador.rect.bottom >= constantes.altoVentana:
                if not game_over:
                    sound.sound_game_over()
                game_over = True

            if jugador.rect.top <= constantes.altoVentana // 4:
                desplazamiento_y = constantes.altoVentana // 4 - jugador.rect.top
                for sprite in sprites:
                    sprite.rect.y += desplazamiento_y
                suelo_y += desplazamiento_y

            items_colisionados = pygame.sprite.spritecollide(jugador, items, True)
            for item in items_colisionados:
                item.reproducir_sonido()
                if isinstance(item, SaludableItem):
                    cantidad_items_recogidos += 1
                    tiempo_restante += 1
                    if tiempo_restante > tiempo_total:
                        tiempo_restante = tiempo_total
                elif isinstance(item, ChatarraItem):
                    tiempo_restante -= 4
                    if tiempo_restante < 0:
                        tiempo_restante = 0

            if cantidad_items_recogidos == 10:
                victory = True
                sound.sound_win1()

            if tiempo_restante > 0:
                tiempo_restante -= 1 / constantes.fps
            else:
                tiempo_restante = 0
                if not victory and not game_over:
                    sound.sound_game_over()
                game_over = True

        if suelo_y < constantes.altoVentana:
            pantalla.blit(sueloPasto, (0, suelo_y))

        if game_over or victory:
            if game_over:
                pantalla.blit(game_over_image, (0, 0))
            elif victory:
                pantalla.blit(victory_image, (0, 0))
            render_text_with_outline(
                get_pixel_font(20),
                '¡Sigue comiendo bien!' if victory else '¡Trata de comer mejor!',
                constantes.blanco,
                constantes.negro,
                (constantes.anchoVentana // 2 - 225, 30),
                pantalla
            )

            pantalla.blit(boton_reintentar_image, boton_reintentar_rect)
            pantalla.blit(boton_salir_image, boton_salir_rect)
        else:
            sprites.update()
            sprites.draw(pantalla)
            pantalla.blit(boton_pausa, boton_pausa_rect.topleft)
            items_recogidos_text = f"{cantidad_items_recogidos}/10"
            render_text_with_outline(
                get_pixel_font(22),
                items_recogidos_text,
                constantes.ocre,
                constantes.negro,
                (10, 40),
                pantalla
            )
            tiempo_formateado = f"Tiempo:{int(tiempo_restante)}"
            render_text_with_outline(
                get_pixel_font(22),
                tiempo_formateado,
                constantes.ocre,
                constantes.negro,
                (10, 10),
                pantalla
            )

        pygame.display.update()
        reloj.tick(constantes.fps)
