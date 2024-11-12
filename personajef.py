import pygame
import constantes
import sound  # Asegúrate de importar el archivo de sonido

class playerf(pygame.sprite.Sprite):
    def __init__(self, ramas):
        super().__init__()

        # Carga la imagen del personaje
        self.imagen_estatica = pygame.image.load('assets/images/personajes/niña0.png').convert_alpha()
        self.imagen_estatica = pygame.transform.scale(self.imagen_estatica, (constantes.anchoPersonaje, constantes.altoPersonaje))

        # Carga las imágenes para las animaciones
        self.imagen_derecha = pygame.image.load('assets/images/personajes/niña1.png').convert_alpha()
        self.imagen_izquierda = pygame.image.load('assets/images/personajes/niña1i.png').convert_alpha()

        self.imagen_derecha = pygame.transform.scale(self.imagen_derecha, (constantes.anchoPersonaje, constantes.altoPersonaje))
        self.imagen_izquierda = pygame.transform.scale(self.imagen_izquierda, (constantes.anchoPersonaje, constantes.altoPersonaje))

        self.image = self.imagen_estatica
        self.rect = self.image.get_rect()

        # Posiciona al jugador en el centro horizontal y en el suelo
        self.rect.x = constantes.anchoVentana // 2
        self.rect.y = constantes.altoVentana - 70

        self.velocidad_x = 0
        self.velocidad_y = 0
        self.fuerza_salto = -18
        self.gravedad = 1
        self.en_rama = False
        self.puede_saltar = True  # Controla si el jugador puede saltar o no
        self.ha_subido_400px = False  # Verifica si el jugador ya subió 400 píxeles

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
            self.puede_saltar = False  # Desactivar salto hasta que toque el suelo o la rama
            sound.sound_jump()  # Reproducir el sonido del salto

        # Aplica gravedad
        self.velocidad_y += self.gravedad
        self.rect.y += self.velocidad_y

        # Verificar si ha subido 400 píxeles
        if not self.ha_subido_400px and self.rect.y <= constantes.altoVentana - 300:
            self.ha_subido_400px = True  # Activa la capacidad de salir de los bordes

        # Colisiones con las ramas
        colisiones = pygame.sprite.spritecollide(self, self.ramas, False)
        if colisiones:
            if self.velocidad_y > 0 and self.rect.bottom <= colisiones[0].rect.bottom:
                self.rect.bottom = colisiones[0].rect.top
                self.velocidad_y = 0
                self.puede_saltar = True  # Permite saltar de nuevo
                self.en_rama = True
        else:
            self.en_rama = False

        # Limitar movimiento dentro de la pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > constantes.anchoVentana:
            self.rect.right = constantes.anchoVentana

        # Asegurarse de que no salga del suelo si no ha subido 400 px
        if not self.ha_subido_400px:
            if self.rect.bottom >= constantes.altoVentana - 70:
                self.rect.bottom = constantes.altoVentana - 70
                self.velocidad_y = 0
                self.puede_saltar = True

        # Verificar si el jugador cae por debajo del margen inferior de la pantalla
        if self.ha_subido_400px and self.rect.top > constantes.altoVentana:
            self.kill()  # Elimina al jugador para que pierda el nivel
