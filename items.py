import pygame
import constantes
import random

class aitems(pygame.sprite.Sprite):
    # Sprite del enemigo
    def __init__(self):
        # Heredamos el init a la clase Sprite de Pygame
        super().__init__()
        # Rectangulo (jugador)
        self.image = pygame.image.load('assets/images/items/banana0.png') # Sprite del item
        # Escala la imagen del personaje a un tamaño específico
        self.image = pygame.transform.scale(self.image, (100, 100))
        # Obtiene el rectangulo (sprite)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(50) # Se genera en una posición X aleatoria en un ancho de 100px desde la izquierda
        self.rect.y = random.randrange(300) # Se genera en una posición Y aleatoria en un alto de 500px desde arriba