import pygame
import constantes

class player(pygame.sprite.Sprite):
    # Sprite del jugador
    def __init__(self):
        # Heredamos el init a la clase Sprite de Pygame
        super().__init__()
        # Rectangulo (jugador)
        self.image = pygame.image.load('assets/images/personajes/niño0.png').convert() # Sprite del personaje
        self.image.set_colorkey(constantes.blanco)
        # Escala la imagen del personaje a un tamaño específico
        self.image = pygame.transform.scale(self.image, (constantes.anchoPersonaje, constantes.altoPersonaje))
        # Obtiene el rectangulo (sprite)
        self.rect = self.image.get_rect()
        # Centra el rectangulo (sprite)
        self.rect.center = (0, 575)

        # Velocidad del personaje inicial
        self.velocidad_x = 0 # Velocidad en el eje x al cargar el personaje
        self.velocidad_y = 0 # Velocidad en el eje y al cargar el personaje


    def update(self):
        # Velocidad predeterminada cada vuelta del bucle si no pulsas nada
        self.velocidad_x = 0
        self.velocidad_y = 0


        # Mantiene las teclas pulsadas
        teclas = pygame.key.get_pressed()

        # Mueve el personaje hacia la izquierda
        if teclas[pygame.K_LEFT]:
            self.velocidad_x = -10 # Pixeles que se mueve el personaje hacia la izquierda
        # Mueve el personaje hacia la derecha
        if teclas[pygame.K_RIGHT]:
            self.velocidad_x = 10 # Pixeles que se mueve el personaje hacia la derecha   

        # Actuliza la posicion del personaje
        self.rect.x += self.velocidad_x

        # Limita el margen izquierdo
        if self.rect.left < 0: # Si el personaje se sale del marco de la pantalla, lo pone en el borde de la izquierda
            self.rect.left = 0
        # Limita el margen derecho
        if self.rect.right > constantes.anchoVentana: # Si el personaje se sale del marco de la pantalla, lo pone en el borde de la derehca
            self.rect.right = constantes.anchoVentana
        
        