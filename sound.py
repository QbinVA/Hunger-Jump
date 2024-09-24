import pygame

#Soundtrack del nivel 1
def sound_lvl_1():
    pygame.mixer.music.load('assets/audio/level1.mp3') # Importo el audio
    pygame.mixer.music.play(-1) # Sirve para reproducir la música en bucle infinito
    pygame.mixer.music.set_volume(0.1) # Controla el volumen (el valor máximo es 1 y el valor mínimo 0.0)

#Soundtrack del menu
def sound_menu():
    pygame.mixer.music.load('assets/audio/backgroundsong.mp3') # Importo el audio
    pygame.mixer.music.play(-1) # Sirve para reproducir la música en bucle infinito
    pygame.mixer.music.set_volume(0.4) # Controla el volumen (el valor máximo es 1 y el valor mínimo 0.0)
