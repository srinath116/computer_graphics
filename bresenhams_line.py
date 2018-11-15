
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

        self.DISPSURF = pygame.display.set_mode((800, 1500))
        pygame.display.set_caption(title)

        # Fill the background with a color
        self.DISPSURF.fill(self.WHITE)


    def correct_order(self,x1, y1, x2, y2):
        """
            our assumption in Algo is x2 > x1.  If not swap the two coordinates
        """

        if x1 > x2:
            return  x2, y2, x1, y1
        return x1, y1, x2, y2


    def bresenhams_line(self,x1, y1, x2, y2):
        x1, y1, x2, y2 = self.correct_order(x1, y1, x2, y2)
        m_new = 2 * (y2 - y1)
        slope_error_new = m_new - (x2 - x1)
        y = y1
        points = []

        for x in range(x1,x2+1):
            print(x,y)
            points.append((x,y))

            slope_error_new += m_new

            if slope_error_new >= 0:
                y += 1
                slope_error_new  -= 2 * (x2 - x1) 

        return points


    def draw_line(self,x1,y1,x2,y2,color=RCB):
        points = self.bresenhams_line(x1,y1,x2,y2)

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




graphics  = MyBasicGraphics("Bresenhams Line Algo")
graphics.draw_line(4,10,100,100)
pygame.display.update()