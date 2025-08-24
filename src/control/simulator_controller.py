import pygame
import numpy as np 
import time
import sys

from src.draw_utils.shapes import *

class SimulatorController():

    def __init__(self, width, height, cells_x, cells_y):
        pygame.init()
        pygame.display.set_caption('Game of life')
        self.screen  = pygame.display.set_mode((width, height))

        self.background_color = 25, 25, 25

        self.cells_x = cells_x
        self.cells_y = cells_y
        self.width = width
        self.height = height
        self.size_x = width / cells_x
        self.size_y = height / cells_y

        self.shapes = Shapes(pygame, self.screen, width, height, cells_x, cells_y)
        
        self.game_state = np.zeros((cells_x, cells_y))
        self.paused = False

    
    def run(self):
        while True:
            self._configure_events(pygame)
            
            # Funcionalidades del flujo normal del programa
            if not self.paused: 
                self._sumulation_running()               
            # funcionalidades de control del usuario (simulacion pausada)
            else:
                self._simulation_paused()
                

    def _configure_events(self, pygame):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()

            # pausar y despausar la ejecucion con una tecla         
            if event.type == pygame.KEYDOWN:
                self.paused = not self.paused

    
    def _sumulation_running(self):
        #colorear el fondo, limpiar la pantalla
        self.screen.fill(self.background_color)
        time.sleep(0.1)

        #copia de la matriz para hacer los cambios
        game_state_aux = np.copy(self.game_state)

        # Dibujo de la cuadricula
        for y in range(0, self.cells_y):
            for x in range(0, self.cells_x):            

                # numero de vecinos cercanos, con el % hacemos que cuando se salga de los limites, regrese por el otro lado
                n_neigh = \
                        self.game_state[ (x - 1) % self.cells_x, (y - 1) % self.cells_y ] + \
                        self.game_state[ (x)     % self.cells_x, (y - 1) % self.cells_y ] + \
                        self.game_state[ (x + 1) % self.cells_x, (y - 1) % self.cells_y ] + \
                        self.game_state[ (x - 1) % self.cells_x, (y)     % self.cells_y ] + \
                        self.game_state[ (x + 1) % self.cells_x, (y)     % self.cells_y ] + \
                        self.game_state[ (x - 1) % self.cells_x, (y + 1) % self.cells_y ] + \
                        self.game_state[ (x)     % self.cells_x, (y + 1) % self.cells_y ] + \
                        self.game_state[ (x + 1) % self.cells_x, (y + 1) % self.cells_y ]

                # una celula muerta con 3 vivas al rededor, revive 
                if self.game_state[x, y] == 0 and n_neigh == 3:
                    game_state_aux[x, y] = 1

                # una celula viva solo sigue viva si tiene 2 o 3 vecinas vivas
                elif self.game_state[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    game_state_aux[x, y] = 0

                self.shapes.draw_polygon(x,y,game_state_aux, 1)              

                
        #mostrar los cambios en la pantalla   
        pygame.display.flip()   

        # guardamos la matriz nueva
        self.game_state = np.copy(game_state_aux) 

    
    def _simulation_paused(self):
        #vector que indica cual de las 3 teclas del mouse se presionó
        mouse_click = pygame.mouse.get_pressed()

        if(sum(mouse_click) > 0):
            #posicion del mouse
            posX, posY = pygame.mouse.get_pos()

            #celda que selecciona el mouse
            celX, celY = int(np.floor(posX / self.size_x)), int(np.floor(posY / self.size_y))

            # click izquierdo
            if(mouse_click[0] == 1):
                self.game_state[celX][celY] = 1

            # click derecho
            if(mouse_click[2] == 1):
                self.game_state[celX][celY] = 0

            self.shapes.draw_polygon(celX, celY, self.game_state, 0)

            #mostrar los cambios en la pantalla   
            pygame.display.flip() 