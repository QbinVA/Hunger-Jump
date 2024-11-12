import pygame
import random
import cv2
import numpy as np
from sound import sound_item  # Asegúrate de que el archivo de sonidos esté correctamente importado

class aitems(pygame.sprite.Sprite):
    def __init__(self, posicion_rama, tamaño=(50, 50)):
        super().__init__()

        # Lista de ítems (imágenes y video)
        self.imagenes_items = [
            'assets/images/items/banana0.png',
            'assets/images/items/cherry.png',
            'assets/images/items/brocoli.mp4',
            'assets/images/items/coca.mp4',
            'assets/images/items/fresa.mp4',
            'assets/images/items/helado.mp4',
            'assets/images/items/galleta.mp4',
            'assets/images/items/pizza.mp4',
            'assets/images/items/naranja.mp4',
            'assets/images/items/sandia.mp4',
            'assets/images/items/zanahoria.mp4',
            'assets/images/items/paleta.mp4',
            'assets/images/items/soda.mp4',
            'assets/images/items/zanahoria.mp4',
        ]

        # Selecciona un ítem aleatorio
        self.item_seleccionado = random.choice(self.imagenes_items)

        # Inicializa las variables de video
        self.video = None
        self.frames = []
        self.current_frame = 0

        # Variables para el control de la velocidad
        self.last_update_time = pygame.time.get_ticks()
        self.frame_interval = 250  # Intervalo en milisegundos

        # Coordenadas para la posición
        self.rect = pygame.Rect(0, 0, *tamaño)
        self.rect.x = posicion_rama.x + 20
        self.rect.y = posicion_rama.y - 45

        # Verifica si el ítem seleccionado es un video
        if self.item_seleccionado.endswith('.mp4'):
            self.load_video(self.item_seleccionado)
            if self.frames:
                self.image = self.frames[self.current_frame]
            else:
                self.image = pygame.Surface(tamaño)
        else:
            # Carga una imagen estática
            self.image = pygame.image.load(self.item_seleccionado).convert_alpha()
            self.image = pygame.transform.scale(self.image, tamaño)

    def load_video(self, video_path):
        """Carga todos los fotogramas del video y aplica transparencia al fondo negro."""
        self.video = cv2.VideoCapture(video_path)
        if not self.video.isOpened():
            print(f"Error al abrir el video: {video_path}")
            return

        while True:
            ret, frame = self.video.read()
            if not ret:
                break
            
            # Convierte el color del fotograma y escala al tamaño del rectángulo
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, self.rect.size)
            
            # Convierte el fondo negro en transparencia usando una máscara
            frame_rgba = cv2.cvtColor(frame, cv2.COLOR_RGB2RGBA)
            black_pixels = np.all(frame[:, :, :] == [0, 0, 0], axis=-1)
            frame_rgba[black_pixels] = [0, 0, 0, 0]

            # Convierte a Surface de Pygame y ajusta la rotación si es necesario
            frame_surface = pygame.surfarray.make_surface(frame_rgba[:, :, :3].swapaxes(0, 1))
            frame_surface.set_colorkey((0, 0, 0))  # Define el fondo como transparente
            frame_surface = pygame.transform.rotate(frame_surface, 360)  
            
            # Almacena cada frame en la lista
            self.frames.append(frame_surface)

        self.video.set(cv2.CAP_PROP_POS_FRAMES, 0)

    def update(self):
        """Actualiza el fotograma actual del video si es necesario."""
        current_time = pygame.time.get_ticks()

        if current_time - self.last_update_time > self.frame_interval:
            if self.frames:
                self.current_frame = (self.current_frame + 1) % len(self.frames)
                self.image = self.frames[self.current_frame]
                self.last_update_time = current_time

    def stop_video(self):
        """Libera el recurso de video cuando ya no se necesita."""
        if self.video:
            self.video.release()

    def reproducir_sonido(self):
        """Reproduce el sonido cuando se recolecta el ítem."""
        sound_item()  # Llama a la función que reproduce el sonido del ítem
