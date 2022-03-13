import turtle as t
import random

SIZE  = 600
SIZE2 = 275

t.setup(width = SIZE, height = SIZE, startx = 50, starty = 50)
t.colormode(255)
win = t.Screen()
win.bgcolor(235, 215, 182)
win.title("Kacheln mit der Schildkröte")

alice = t.Turtle()
alice.pensize(3)


def tiling(x, y, s, l):
    
    if l == 0:
        
        if random.random() < 0.5:
            alice.penup()
            alice.goto(x, y - s)
            alice.pendown()
            alice.goto(x, y + s)
        else:
            alice.penup()
            alice.goto(x - s, y)
            alice.pendown()
            alice.goto(x + s, y)
    else:
        s /= 2
        l -= 1
        tiling(x - s, y + s, s, l)
        tiling(x + s, y + s, s, l)
        tiling(x - s, y - s, s, l)
        tiling(x + s, y - s, s, l)
        
            
alice.hideturtle()
win.tracer(False)
tiling(0, 0, SIZE2, 5)
win.tracer(True)
t.exitonclick()