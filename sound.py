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
    pygame.mixer.music.set_volume(0.7) # Controla el volumen (el valor máximo es 1 y el valor mínimo 0.0)

def sound_item():
    item_sound = pygame.mixer.Sound('assets/audio/itemsaludable.mp3')  # Cargar el sonido
    item_sound.set_volume(0.7)  # Ajustar volumen
    item_sound.play()  # Reproducir el sonido

def sound_jump():
    jump_sound = pygame.mixer.Sound('assets/audio/salto.mp3')  # Cargar el sonido
    jump_sound.set_volume(0.4)  # Ajustar volumen
    jump_sound.play()  # Reproducir el sonido

def sound_win1():
    pygame.mixer.music.load('assets/audio/win1.mp3')  # Cargar el sonido
    pygame.mixer.music.set_volume(0.1)  # Ajustar volumen
    pygame.mixer.music.play()  # Reproducir el sonido

def sound_clic1():
    clic_sound = pygame.mixer.Sound('assets/audio/sonidoBoton.wav')  # Cargar el sonido
    clic_sound.set_volume(0.8)  # Ajustar volumen
    clic_sound.play()  # Reproducir el sonido

def sound_clic2():
    clic_sound = pygame.mixer.Sound('assets/audio/sonidoPlay.wav')  # Cargar el sonido
    clic_sound.set_volume(0.8)  # Ajustar volumen
    clic_sound.play()  # Reproducir el sonido

def sound_Button():
    clic_sound = pygame.mixer.Sound('assets/audio/sonidoBtn.mp3')  # Cargar el sonido
    clic_sound.set_volume(0.8)  # Ajustar volumen
    clic_sound.play()  # Reproducir el sonido