
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
    RCB = (17,184,168)

    def __init__(self,title):
        pygame.init()

        self.DISPSURF = pygame.display.set_mode((500, 500))
        pygame.display.set_caption(title)

        # Fill the background with a color
        self.DISPSURF.fill(self.RCB)





    def dda(self,x1, y1, x2, y2):
        
        m = float((y2-y1)) / float((x2 - x1))
        print("Slope is ",m)
        points = []
        x , y = x1 ,y1
        points.append((int(round(x)),int(round(y))))
       
        while((x < x2) or (y < y2)):

            x += 1
            y += m
            points.append((int(round(x)),int(round(y))))



        return points


    def draw_line(self,x1,y1,x2,y2,color=WHITE):
        points = self.dda(x1,y1,x2,y2)

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




x=raw_input("enter x and y co-ordinates seperated by ','").split(",")
x1=int(x[0])
y1=int(x[1])
x2=int(x[2])
y2=int(x[3])
#print(x1,x2,y1,y2)
graphics  = MyBasicGraphics("DDA line drawing Algo")

graphics.draw_line(x1,y1,x2,y2)