import turtle
import random as r

WIDTH, HEIGHT = 640, 400
MIN_X = -WIDTH//2 + 10
MAX_X = WIDTH//2 - 10
MIN_Y = HEIGHT//2 - 10
MAX_Y = -HEIGHT//2 + 10 
BORDERSIZE = 1
STEPSIZE = 15

codingtrain = ["#f05025", "#f89e50", "#f8ef22",
               "#f063a4", "#9252a1", "#817ac6",
               "#62c777", "#31c5f4"]

wn = turtle.Screen()
wn.setup(width = WIDTH + 20, height = HEIGHT + 20)
# wn.colormode(255)
wn.bgcolor("#2a282d")

# Draw Border
border = turtle.Turtle()
border.speed(0)
border.pensize(BORDERSIZE)
border.pencolor("#e6e2cc")
border.penup()
border.hideturtle()
border.goto(MIN_X, MIN_Y)
border.pendown()
border.goto(MAX_X, MIN_Y)
border.goto(MAX_X, MAX_Y)
border.goto(MIN_X, MAX_Y)
border.goto(MIN_X, MIN_Y)

# Start Random Walk
hexi = turtle.Turtle()
hexi.speed(0)
hexi.pensize(2)

def go_home():
    hexi.penup()
    hexi.home()
    hexi.pendown()

for step in range(5000):

    # Set Pencolor
    if step%20 == 0:
        hexi.pencolor(codingtrain[r.randint(0, len(codingtrain) - 1)])

    # Roll Dice and set Angle
    roll = r.randint(0, 5)
    angle = roll*60
    hexi.seth(angle)
    
    # Check Border
    if hexi.xcor() >= MAX_X:
        go_home()
    elif hexi.xcor() <= MIN_X:
        go_home()
    elif hexi.ycor() <= MAX_Y:
        go_home()
    elif hexi.ycor() >= MIN_Y:
        go_home()
    else:
        hexi.fd(STEPSIZE)

print("I did it, Babe!")
wn.mainloop()