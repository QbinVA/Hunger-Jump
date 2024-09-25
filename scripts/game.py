import pygame
import sys

from scripts.utils import load_image, load_images
from scripts.entidades import PhysicsEntity
from scripts.tilemap import Tilemap

# Clase para cosas básicas del juego
class Game:
    def __init__(self):

        # Inicializamos pygame
        pygame.init()

        pygame.display.set_caption('Hunger Jump!') # Insertamos nombre a la ventana
        self.screen = pygame.display.set_mode((500, 750)) # Creamos la pantalla

        # La superficie es la mitad de la pantalla pero en negro
        self.display = pygame.Surface((250, 375)) # Las cosas de renderizaran en el display y de ahí se escalan en la pantalla



        self.clock = pygame.time.Clock() # Reloj

        # Indice de movimientos
        self.movement = [False, False] 

        # Importamos la imagen
        self.assets = {
            'decor': load_image('fondos/sueloPasto.png'),
            'player': load_image('personajes/niño01.png')
        }

        
        # Personaje
        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))

        self.tilemap = Tilemap(self, tile_size=16)


    def run(self):
        # Bucle
        while True:
            # Rellenemos con color la pantalla
            self.display.fill((14, 219, 248))

            self.tilemap.render(self.display)

            # Actualiza el personaje
            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.display) # Lo renderiza


            # Ciclo For para los eventos
            for event in pygame.event.get():
                # Evento para salir
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()

                # Evento para teclas presionadas
                if event.type == pygame.KEYDOWN:
                    # Si presionamos la flecha UP
                    if event.key == pygame.K_LEFT: 
                        self.movement[0] = True # Convierte True al indice 0 de self.movement
                    # Si presionamos la flecha DOWN
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True # Convierte True al indice 1 de self.movement
                if event.type == pygame.KEYUP:
                    # Si dejamos de presionar la flecha UP
                    if event.key == pygame.K_LEFT: 
                        self.movement[0] = False # Convierte False al indice 0 de self.movement
                    # Si dejamos de presionar la flecha DOWN
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False # Convierte False al indice 1 de self.movement
                    


            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            # Actualizamos la pantalla
            pygame.display.update()
            # Seteamos los fps (60)
            self.clock.tick(90)

Game().run()