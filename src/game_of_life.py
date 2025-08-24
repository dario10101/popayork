import pygame
import numpy as np 
import time
import sys

#dibujar un poligono en la cuadricula
def draw_polygon(x,y,game_state_info, fill):
    # dibijamos el poligono de la celula
    polygon_info = [( (x)     * sizeX, (y)     * sizeY),
                    ( (x + 1) * sizeX, (y)     * sizeY),
                    ( (x + 1) * sizeX, (y + 1) * sizeY),
                    ( (x)     * sizeX, (y + 1) * sizeY) ]

    if(game_state_info[x, y] == 0):
        pygame.draw.polygon(screen, death_cell_color, polygon_info, fill)
    else:
        pygame.draw.polygon(screen, cell_color, polygon_info, 0) 


def draw_circle(x, y, game_state_info, fill):
    # centro de la celda en píxeles
    center = (int((x + 0.5) * sizeX), int((y + 0.5) * sizeY))
    
    # radio (un poco menor que la mitad para que no se "toquen" los círculos vecinos)
    radius = int(min(sizeX, sizeY) / 2) - 1

    if game_state_info[x, y] == 0:
        pygame.draw.circle(screen, death_cell_color, center, radius, 0)  # celda muerta
    else:
        pygame.draw.circle(screen, cell_color, center, radius, 0)        # celda viva


pygame.init()
pygame.display.set_caption('Game of life')

#colores
#background_color = 238, 238, 0
background_color = 25, 25, 25
cell_color = 255, 255, 255
death_cell_color = 128, 128, 128

# tamaño del lienzo
width = 600
height = 600
screen  = pygame.display.set_mode((width, height))

#pintar fondo
screen.fill(background_color)

#numero de celdas en el eje X y en el Y
ncX = 40
ncY = 40

#tamaño de celdas en el eje x
sizeX = width / ncX
sizeY = height / ncY

#matriz de estados
game_state = np.zeros((ncX, ncY))

# automata 1
game_state[2, 33] = 1
game_state[2, 34] = 1
game_state[2, 35] = 1

# automata 2
game_state[33, 3] = 1
game_state[33, 4] = 1
game_state[33, 5] = 1

# automata 2
game_state[1, 1] = 1
game_state[2, 2] = 1
game_state[2, 3] = 1
game_state[1, 3] = 1
game_state[0, 3] = 1

# automata 2
game_state[35, 35] = 1
game_state[35, 36] = 1
game_state[35, 37] = 1
game_state[36, 35] = 1
game_state[37, 36] = 1

paused = False

while True:
    #eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        # pausar y despausar la ejecucion con una tecla         
        if event.type == pygame.KEYDOWN:
            paused = not paused

    # Funcionalidades del flujo normal del programa
    if not paused:

        #colorear el fondo, limpiar la pantalla
        screen.fill(background_color)
        time.sleep(0.1)

        #copia de la matriz para hacer los cambios
        game_state_aux = np.copy(game_state)

        # Dibujo de la cuadricula
        for y in range(0, ncY):
            for x in range(0, ncX):            

                # numero de vecinos cercanos, con el % hacemos que cuando se salga de los limites, regrese por el otro lado
                n_neigh = game_state[ (x - 1) % ncX, (y - 1) % ncY ] + \
                        game_state[ (x)     % ncX, (y - 1) % ncY ] + \
                        game_state[ (x + 1) % ncX, (y - 1) % ncY ] + \
                        game_state[ (x - 1) % ncX, (y)     % ncY ] + \
                        game_state[ (x + 1) % ncX, (y)     % ncY ] + \
                        game_state[ (x - 1) % ncX, (y + 1) % ncY ] + \
                        game_state[ (x)     % ncX, (y + 1) % ncY ] + \
                        game_state[ (x + 1) % ncX, (y + 1) % ncY ]

                # una celula muerta con 3 vivas al rededor, revive 
                if game_state[x, y] == 0 and n_neigh == 3:
                    game_state_aux[x, y] = 1

                # una celula viva solo sigue viva si tiene 2 o 3 vecinas vivas
                elif(game_state[x, y] == 1 and (n_neigh < 2 or n_neigh > 3)):
                    game_state_aux[x, y] = 0

                draw_polygon(x,y,game_state_aux, 1)              

                
        #mostrar los cambios en la pantalla   
        pygame.display.flip()   

        # guardamos la matriz nueva
        game_state = np.copy(game_state_aux) 

    # funcionalidades de control del usuario (simulacion pausada)
    else:
        #vector que indica cual de las 3 teclas del mouse se presionó
        mouse_click = pygame.mouse.get_pressed()

        if(sum(mouse_click) > 0):
            #posicion del mouse
            posX, posY = pygame.mouse.get_pos()

            #celda que selecciona el mouse
            celX, celY = int(np.floor(posX / sizeX)), int(np.floor(posY / sizeY))

            # click izquierdo
            if(mouse_click[0] == 1):
                game_state[celX][celY] = 1

            # click derecho
            if(mouse_click[2] == 1):
                game_state[celX][celY] = 0

            draw_polygon(celX, celY, game_state, 0)

            #mostrar los cambios en la pantalla   
            pygame.display.flip() 





