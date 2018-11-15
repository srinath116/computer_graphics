
import pygame
import sys
from pygame import gfxdraw

from pygame.locals import QUIT

class MyBasicGraphics:

    # colors definition
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (227, 27, 27)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    RCB = (27, 27, 27)

    def __init__(self,title):
        pygame.init()

        self.DISPSURF = pygame.display.set_mode((500, 500))
        pygame.display.set_caption(title)

        # Fill the background with a color
        self.DISPSURF.fill(self.RCB)





    def bresenhams_circle(self,radius,center = (0,0)):
        print("Center is ",center)
        x = 0
        y =  radius

        d = 3-2*radius
        points = []
        points.append((center[0] + x, center[1] + y))
        points.append((center[0] + y, center[1] + x))
        points.append((center[0] + y, center[1] - x))
        points.append((center[0] + x, center[1] - y))

        points.append((center[0] - x, center[1] + y))
        points.append((center[0] - y, center[1] + x))
        points.append((center[0] - x, center[1] - y))
        points.append((center[0] - y, center[1] - x))

        while(y >  x):
            x += 1
            if d <= 0:
                d += 4*x + 6
            else:
                
                d += 4*(x-y) + 10
                y -= 1

            points.append((center[0] + x, center[1] + y))
            points.append((center[0] + y, center[1] + x))

            points.append((center[0] + y, center[1] - x))
            points.append((center[0] + x, center[1] - y))

            points.append((center[0] - x, center[1] + y))
            points.append((center[0] - y, center[1] + x))

            points.append((center[0] - x, center[1] - y))
            points.append((center[0] - y, center[1] - x))

        return points
        


    def draw_circle(self,radius,center=(0,0),color =RED):
        points = self.bresenhams_circle(radius,center)

        for pt in points:
            print('ploting point : ',pt)
            gfxdraw.pixel(self.DISPSURF, pt[0] , pt[1],color)
            pygame.display.flip()

        while True:
            for evt in pygame.event.get():
                if evt.type == QUIT:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()




graphics  = MyBasicGraphics("Bresenhams Circle Algo")
graphics.draw_circle(center = (250,250),radius = 25)