import pygame
import sys
import cv2
import numpy as np
import constantes

# Inicializa Pygame
pygame.init()

# Creo y seteo valores a la pantalla
pantalla = pygame.display.set_mode((500, 750))
pygame.display.set_caption("Hungry Jump")  # Título de la ventana

# Declaro e inserto el icono de la ventana
icono = pygame.image.load("assets/images/items/banana0.png")
pygame.display.set_icon(icono)

# Fuente
def get_font(size):
    return pygame.font.Font("assets/Font/font.ttf", size)

def reproducir_video(video_path, audio_path, on_stop_callback):
    cap = cv2.VideoCapture(video_path)
    pygame.mixer.init()
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()

    fps = cap.get(cv2.CAP_PROP_FPS)
    clock = pygame.time.Clock()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Aplicar efecto espejo al cuadro
        frame = cv2.flip(frame, 1)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = np.rot90(frame)
        frame = pygame.surfarray.make_surface(frame)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cap.release()
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                cap.release()
                pygame.mixer.music.stop()
                on_stop_callback()
                return

        pantalla.blit(frame, (0, 0))
        pygame.display.update()
        clock.tick(fps)

    cap.release()
    pygame.mixer.music.stop()

def instrucciones():
    reproducir_video("assets/animations/animacionIngles.mp4", "assets/animations/animacionIngles.mp3", on_stop_callback=dificultad) 

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                from difficulty import difi
                difi()
            if event.type == pygame.MOUSEBUTTONDOWN:
                from difficulty import difi
                difi()

        pygame.display.update()

def dificultad():
    pass

# Llamar a la función instrucciones para probar
instrucciones()