import pygame
import constantes

class player(pygame.sprite.Sprite):
    def __init__(self, ramas):
        super().__init__()

        # Carga la imagen del personaje
        self.imagen_estatica = pygame.image.load('assets/images/personajes/niño0.png').convert_alpha()
        self.imagen_estatica = pygame.transform.scale(self.imagen_estatica, (constantes.anchoPersonaje, constantes.altoPersonaje))

        # Carga las imágenes para las animaciones
        self.imagen_derecha = pygame.image.load('assets/images/personajes/niño1.png').convert_alpha()
        self.imagen_izquierda = pygame.image.load('assets/images/personajes/niño1i.png').convert_alpha()

        self.imagen_derecha = pygame.transform.scale(self.imagen_derecha, (constantes.anchoPersonaje, constantes.altoPersonaje))
        self.imagen_izquierda = pygame.transform.scale(self.imagen_izquierda, (constantes.anchoPersonaje, constantes.altoPersonaje))

        self.image = self.imagen_estatica
        self.rect = self.image.get_rect()

        # Posiciona al jugador en el centro horizontal y en una posición específica del eje Y
        self.rect.x = constantes.anchoVentana // 2  # Mantiene la posición horizontal centrada
        self.rect.y = constantes.altoVentana - 150  # Ajusta este valor para modificar la ubicación inicial en el eje Y

        self.velocidad_x = 0
        self.velocidad_y = 0
        self.fuerza_salto = -18
        self.gravedad = 1
        self.en_rama = False
        self.puede_saltar = True  # Controla si el jugador puede saltar o no

        self.ramas = ramas

    def update(self):
        teclas = pygame.key.get_pressed()

        # Movimiento horizontal
        if teclas[pygame.K_LEFT]:
            self.velocidad_x = -6
            self.image = self.imagen_izquierda
        elif teclas[pygame.K_RIGHT]:
            self.velocidad_x = 6
            self.image = self.imagen_derecha
        else:
            self.velocidad_x = 0
            self.image = self.imagen_estatica

        self.rect.x += self.velocidad_x

        # Salto controlado por el jugador
        if (teclas[pygame.K_SPACE] or teclas[pygame.K_UP]) and self.puede_saltar:
            self.velocidad_y = self.fuerza_salto
            self.puede_saltar = False

        # Aplicar gravedad
        self.velocidad_y += self.gravedad
        self.rect.y += self.velocidad_y

        # Verificar colisiones con las ramas
        colisiones = pygame.sprite.spritecollide(self, self.ramas, False)
        if colisiones:
            # Verifica si está cayendo y toca la rama
            if self.velocidad_y > 0 and self.rect.bottom <= colisiones[0].rect.bottom:
                self.rect.bottom = colisiones[0].rect.top
                self.velocidad_y = 0
                self.puede_saltar = True  # Permite que el jugador vuelva a saltar
                self.en_rama = True
        else:
            self.en_rama = False

        # Limitar movimiento dentro de la pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > constantes.anchoVentana:
            self.rect.right = constantes.anchoVentana

        # Asegurarse de que no salga del suelo
        if self.rect.bottom >= constantes.altoVentana - 70:  # Cambié el margen inferior a -50
            self.rect.bottom = constantes.altoVentana - 70  # Ajusta esto según la altura del suelo
            self.velocidad_y = 0
            self.puede_saltar = True  # Asegura que pueda volver a saltar desde el suelo

