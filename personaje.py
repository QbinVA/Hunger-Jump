import pygame
import constantes

class Personaje():
    def __init__(self, x, y, animacionX):
        self.flip = False #voltea la imagen
        self.animaciones = animacionX
        #imagen de la animacion que se esta mostrando actualmente
        self.frame_index = 0
        #aqui se almacena la hora actual en milisegundos desde que se inicio pygame
        self.update_time = pygame.time.get_ticks()
        self.image = animacionX[self.frame_index]
        self.forma = pygame.Rect(0, 0, constantes.anchoPersonaje, constantes.altoPersonaje)
        self.forma.center = (x,y)

    def update(self):
        cooldown_animacion = 500 #tiempo en que tarda en cambiar la imagen del personaje
        self.image = self.animaciones[self.frame_index]
        #Sumamos 1 al indice para que cambie de imagen
        if pygame.time.get_ticks() - self.update_time >= cooldown_animacion:
            self.frame_index = self.frame_index + 1
            self.update_time = pygame.time.get_ticks()
        #Regresamos el indice a cero
        if self.frame_index >= len(self.animaciones):
            self.frame_index = 0

    def dibujar(self, interfaz):
        imagen_flip = pygame.transform.flip(self.image, self.flip, False)
        interfaz.blit(imagen_flip, self.forma)
        #pygame.draw.rect(interfaz, constantes.rojo, self.forma, 1)

    def movimiento(self, delta_x, delta_y):
        #Si el movimiento en el eje x es negativo, da vuelta a la izquierda
        if delta_x < 0:
            self.flip = True
        #Si el movimiento en el eje x es positivo, va havia la derecha
        if delta_x > 0:
            self.flip = False

        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y + delta_y