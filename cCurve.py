from turtle import *

def c_curve(x1, y1, x2, y2, level):

    def draw_line(x1, y1, x2, y2):
        up()
        goto(x1,y1)
        down()
        goto(x2,y2)

    if level == 0:
        draw_line(x1, y1, x2, y2)
    else:
        xm = (x1+x2+y1-y2)/2
        ym = (x2+y1+y2-x1)/2
        c_curve(x1, y1, xm, ym, level-1)
        c_curve(xm, ym, x2, y2, level-1)

if __name__ == '__main__':
    c_curve(5, -200, 5, 200, 10)
    mainloop()
