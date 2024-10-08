import pygame
import constantes
import random

class aitems(pygame.sprite.Sprite):
    # Sprite del item
    def __init__(self, posicion_rama):
        super().__init__()

        # Lista de imágenes de los ítems
        self.imagenes_items = [
            'assets/images/items/banana0.png',
            'assets/images/items/cherry.png'
            ]

        # Carga una imagen aleatoria de la lista
        self.image = pygame.image.load(random.choice(self.imagenes_items)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))

        # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
        
        # Posiciona el ítem directamente sobre la rama
        self.rect.x = posicion_rama + random.randint(-40, 40)  # Permite un pequeño desplazamiento horizontal
        self.rect.y = posicion_rama - 50  # Ajusta la altura sobre la rama
