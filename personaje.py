import pygame
import constantes

class player(pygame.sprite.Sprite):
    # Esta es la clase del personaje
    def __init__(self):
        # Inicializa la clase base de Pygame, para que el personaje sea un sprite
        super().__init__()

        # Carga la imagen del personaje estático (sin movimiento)
        self.imagen_estatica = pygame.image.load('assets/images/personajes/niño0.png').convert()
        self.imagen_estatica.set_colorkey(constantes.blanco)  # Hace transparente el fondo blanco
        self.imagen_estatica = pygame.transform.scale(self.imagen_estatica, (constantes.anchoPersonaje, constantes.altoPersonaje))

        # Carga las imágenes para las animaciones
        self.imagen_derecha = pygame.image.load('assets/images/personajes/niño1.png').convert()
        self.imagen_izquierda = pygame.image.load('assets/images/personajes/niño1i.png').convert()
        
        # Hace transparente el fondo de las imágenes de movimiento
        self.imagen_derecha.set_colorkey(constantes.blanco)
        self.imagen_izquierda.set_colorkey(constantes.blanco)

        # Escala las imágenes de movimiento
        self.imagen_derecha = pygame.transform.scale(self.imagen_derecha, (constantes.anchoPersonaje, constantes.altoPersonaje))
        self.imagen_izquierda = pygame.transform.scale(self.imagen_izquierda, (constantes.anchoPersonaje, constantes.altoPersonaje))

        # Inicializa la imagen actual del personaje como la imagen estática
        self.image = self.imagen_estatica

        # Obtiene un rectángulo (hitbox) alrededor del personaje para controlar su posición y colisiones
        self.rect = self.image.get_rect()

        # Posiciona inicialmente el personaje en la parte inferior de la pantalla
        self.rect.center = (constantes.anchoVentana // 2, constantes.altoVentana - 100)

        # Define la velocidad inicial del personaje en el eje X (horizontal) y Y (vertical)
        self.velocidad_x = 0
        self.velocidad_y = 0

        # Define la fuerza de salto y la gravedad que lo empujará hacia abajo
        self.fuerza_salto = -20  # Velocidad al saltar
        self.gravedad = 1  # Velocidad que se incrementa mientras cae

    def salto_constante(self):
        # Esta función hace que el personaje salte constantemente
        if self.rect.bottom >= constantes.altoVentana - 100:  # Si el personaje toca el "suelo"
            self.velocidad_y = self.fuerza_salto  # Aplica la fuerza de salto
        else:
            self.velocidad_y += self.gravedad  # Aplica la gravedad cuando no está en el suelo

        # Actualiza la posición vertical del personaje con su velocidad
        self.rect.y += self.velocidad_y

    def update(self):
        # Esta función se ejecuta en cada frame para actualizar el estado del personaje
        teclas = pygame.key.get_pressed()  # Obtiene las teclas presionadas

        # Verifica si se presiona la flecha izquierda
        if teclas[pygame.K_LEFT]:
            self.velocidad_x = -5  # Velocidad de movimiento hacia la izquierda
            self.image = self.imagen_izquierda  # Cambia la imagen a la de movimiento a la izquierda
        # Verifica si se presiona la flecha derecha
        elif teclas[pygame.K_RIGHT]:
            self.velocidad_x = 5  # Velocidad de movimiento hacia la derecha
            self.image = self.imagen_derecha  # Cambia la imagen a la de movimiento a la derecha
        else:
            self.velocidad_x = 0  # Si no se presiona ninguna tecla, el personaje no se mueve horizontalmente
            self.image = self.imagen_estatica  # Cambia la imagen a la estática cuando no se mueve

        # Actualiza la posición del personaje en el eje X
        self.rect.x += self.velocidad_x

        # Llama a la función de salto constante para hacer que el personaje salte automáticamente
        self.salto_constante()

        # Asegura que el personaje no salga de los límites de la pantalla en el eje X
        if self.rect.left < 0:  # Si se sale por la izquierda, lo bloquea en 0
            self.rect.left = 0
        if self.rect.right > constantes.anchoVentana:  # Si se sale por la derecha, lo bloquea en el ancho máximo de la pantalla
            self.rect.right = constantes.anchoVentana
