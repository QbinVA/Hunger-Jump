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
        self.rect.center = (constantes.anchoVentana // 2, constantes.altoVentana - 100)

        self.velocidad_x = 0
        self.velocidad_y = 0
        self.fuerza_salto = -20
        self.gravedad = 1
        self.en_rama = False

        self.ramas = ramas

    def update(self):
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_LEFT]:
            self.velocidad_x = -5
            self.image = self.imagen_izquierda
        elif teclas[pygame.K_RIGHT]:
            self.velocidad_x = 5
            self.image = self.imagen_derecha
        else:
            self.velocidad_x = 0
            self.image = self.imagen_estatica

        self.rect.x += self.velocidad_x

        self.salto_constante()

        # Verificar colisiones con las ramas
        colisiones = pygame.sprite.spritecollide(self, self.ramas, False)
        if colisiones:
            # Verifica si está cayendo y toca la rama
            if self.velocidad_y > 0 and self.rect.bottom <= colisiones[0].rect.bottom:
                self.rect.bottom = colisiones[0].rect.top
                self.velocidad_y = self.fuerza_salto  # Inicia el salto nuevamente
                self.en_rama = True
        else:
            self.en_rama = False

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > constantes.anchoVentana:
            self.rect.right = constantes.anchoVentana

    def salto_constante(self):
        # Si no está sobre una rama, aplicar la gravedad
        if not self.en_rama:
            if self.rect.bottom >= constantes.altoVentana - 100:
                self.velocidad_y = self.fuerza_salto
            else:
                self.velocidad_y += self.gravedad
            self.rect.y += self.velocidad_y
