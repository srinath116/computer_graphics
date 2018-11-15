import pygame
import sys
from pygame import gfxdraw
import numpy as np
from pygame.locals import QUIT

class Graphics:

    # colors definition
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (227, 27, 27)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    RCB = (27, 27, 27)
    BACKGROUND = RCB

    def __init__(self,title):
        
        pygame.init()

        self.DISPSURF = pygame.display.set_mode((320, 250), 0)
        pygame.display.set_caption(title)

        # Fill the background with a color
        self.DISPSURF.fill(self.BACKGROUND)

    def synthesize_image(self,size):
        return np.random.randint(255,size=size)

    def get_baysian_filter_color(self,i,j):
        if i%2 == 0:
            if j%2 == 0:
                return 'R'
            else:
                return 'G'
        else:
            if j%2 == 0:
                return 'G'
            else:
                return 'B'

    def apply_demosacing(self,sensor_matrix):
        red = np.zeros((sensor_matrix.shape[0],sensor_matrix.shape[1] ),dtype = int)
        green = np.zeros(  (sensor_matrix.shape[0],sensor_matrix.shape[1] ),dtype = int)
        blue = np.zeros( (sensor_matrix.shape[0] ,sensor_matrix.shape[1]),dtype = int)

        for i in range(size[0]):
            for j in range(size[1]):
                if i == 0 or j == 0 or i == size[0]-1 or j == size[1] -1: 
                    continue

                color = self.get_baysian_filter_color(i,j)

                if color == 'R':
                    red[i,j] = sensor_matrix[i,j]
                    green[i,j] = (sensor_matrix[i-1,j] + sensor_matrix[i+1,j] + sensor_matrix[i,j-1] + sensor_matrix[i,j+1]) /4
                    blue[i,j] = (sensor_matrix[i-1,j-1] + sensor_matrix[i-1,j+1] + sensor_matrix[i+1,j-1] + sensor_matrix[i+1,j+1]) /4

                elif color == 'G':
                    red[i,j] = (sensor_matrix[i,j-1] + sensor_matrix[i,j+1] ) / 2 
                    green[i,j] = (sensor_matrix[i-1,j-1] + sensor_matrix[i-1,j+1] + sensor_matrix[i+1,j-1] + sensor_matrix[i+1,j+1] + sensor_matrix[i,j] ) /5
                    blue[i,j] = (sensor_matrix[i-1,j] + sensor_matrix[i+1,j]) /2

                elif color == 'B':
                    red[i,j] = (sensor_matrix[i-1,j-1] + sensor_matrix[i-1,j+1] + sensor_matrix[i+1,j-1] + sensor_matrix[i+1,j+1]) /4
                    green[i,j] = (sensor_matrix[i-1,j] + sensor_matrix[i+1,j] + sensor_matrix[i,j-1] + sensor_matrix[i,j+1]) /4
                    blue[i,j] = sensor_matrix[i,j]

        red = red[1:-1,1:-1]
        green = green[1:-1,1:-1]
        blue = blue[1:-1,1:-1]

        return red,green,blue

    def displayRGB(self,red,green,blue):

        for i in range(red.shape[0]):
            for j in range(red.shape[1]):
                color = (int(red[i,j]) , int(green[i,j]) ,int(blue[i,j]))
                gfxdraw.pixel(self.DISPSURF, j , i ,color)
        pygame.display.update()

    def pause(self):

        while True:
            for evt in pygame.event.get():
                if evt.type == QUIT:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


graphics  = Graphics("Demos")
size = (320,250)
sensor_matrix = graphics.synthesize_image(size)

print("Original : \n ",sensor_matrix)
r,g,b = graphics.apply_demosacing(sensor_matrix)

print('RED :'  )
print(r)

print('Green :'  )
print(g)

print('Blue :'  )
print(b)

graphics.displayRGB(r,g,b)
graphics.pause()

