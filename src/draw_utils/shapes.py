import pygame

class Shapes():

    def __init__(self, pygame:pygame, screen, width, height, cells_x, cells_y):
        self.pygame = pygame
        self.screen = screen
        self.width = width
        self.height = height
        self.size_x = width / cells_x
        self.size_y = height / cells_y

        self.background_color = 25, 25, 25
        self.cell_color = 255, 255, 255
        self.death_cell_color = 128, 128, 128


    #dibujar un poligono en la cuadricula
    def draw_polygon(self, x,y,game_state_info, fill):
        # dibijamos el poligono de la celula
        polygon_info = [( (x)     * self.size_x, (y)     * self.size_y),
                        ( (x + 1) * self.size_x, (y)     * self.size_y),
                        ( (x + 1) * self.size_x, (y + 1) * self.size_y),
                        ( (x)     * self.size_x, (y + 1) * self.size_y) ]

        if(game_state_info[x, y] == 0):
            self.pygame.draw.polygon(self.screen, self.death_cell_color, polygon_info, fill)
        else:
            self.pygame.draw.polygon(self.screen, self.cell_color, polygon_info, 0) 


    def draw_circle(self, x, y, game_state_info, fill):
        # centro de la celda en píxeles
        center = (int((x + 0.5) * self.size_x), int((y + 0.5) * self.size_y))
        
        # radio (un poco menor que la mitad para que no se "toquen" los círculos vecinos)
        radius = int(min(self.size_x, self.size_y) / 2) - 1

        if game_state_info[x, y] == 0:
            pygame.draw.circle(self.screen, self.death_cell_color, center, radius, 0)  # celda muerta
        else:
            pygame.draw.circle(self.screen, self.cell_color, center, radius, 0) # celda viva