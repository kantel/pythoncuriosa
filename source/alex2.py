import turtle as t

wn = t.Screen()
wn.bgcolor("green")
wn.setup(width = 640, height = 400)
wn.title("Atari!")

alex = t.Turtle()
alex.pencolor("black")
alex.pensize(2)

def draw_box(n):
    for i in range(n):
        alex.left(90)
        alex.forward(100)

draw_box(4)

print("Schildkröte Alex sagt: »I did it, Babe!« 🐢")

wn.mainloop()
