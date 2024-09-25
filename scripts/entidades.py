import pygame

# Clase para fisicas de las entidades
class PhysicsEntity:
    # Juego, tipo de entidad, posicion, tamaño
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.typye = e_type
        self.pos = list(pos) # Crea una lista para las posiciones de las entidades
        self.size = size
        self.velocity = [0, 0] # Velocidad (cambio de posicion)
    
    def update(self, movement=(0, 0)):
        # Actualiza el movimiento sumando el cambio de posicion al movimiento de los frames
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])
        # Actualiza la posicion
        self.pos[0] += frame_movement[0]
        self.pos[1] += frame_movement[1]

    # Renderizamos el personaje
    def render(self, surf):
        surf.blit(self.game.assets['player'], self.pos)