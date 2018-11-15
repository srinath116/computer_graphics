from turtle import *

def snowflake(lengthSide, depth):
    if depth == 0:
        forward(lengthSide)
        return
    lengthSide /= 3.5
    snowflake(lengthSide, depth-1)
    left(60)
    snowflake(lengthSide, depth-1)
    right(120)
    snowflake(lengthSide, depth-1)
    left(60)
    snowflake(lengthSide, depth-1)

if __name__ == "__main__":

    speed(100)
    length = 750

    penup()

    backward(length/2.0)

    pendown()

    for i in range(3):
        snowflake(length, 4)
        right(120)

    mainloop()
