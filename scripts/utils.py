import pygame
import os

# Ruta base de las imagenes
BASE_IMG_PATH = 'assets/images/'

# Funcion para cargar las imagenes
def load_image(path):
    # Importamos la imagen y la convertimos al formato de pygame para una mejor renderizacion
    img = pygame.image.load(BASE_IMG_PATH + path)
    #img.set_colorkey((255, 255, 255))
    return img

def load_images(path):
    images = []
    for img_name in os.listdir(BASE_IMG_PATH + path):
        images.append(load_image(path + '/' + img_name))
    return images