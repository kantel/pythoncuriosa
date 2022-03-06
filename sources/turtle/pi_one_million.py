import turtle
from mpmath import mp    # Für die Ziffern von Pi

pieter = turtle.Turtle()
mp.dps = 1000

pi = (f"{(mp.pi)}")
digits = [int(s) for s in pi if s != "."]

for m in digits:
    if m == 0:
        pieter.forward(10)
    if m == 1:
        pieter.right(90)
        pieter.forward(10)
    if m == 2:
        pieter.left(90)
        pieter.forward(10)
    if m == 3:
        pieter.left(180)
        pieter.forward(10)
    if m == 4:
        pieter.right(270)
        pieter.forward(10)
    if m == 5:
        pieter.right(45)
        pieter.forward(10)
    if m == 6:
        pieter.left(45)
        pieter.forward(100)
    if m == 7:
        pieter.right(60)
        pieter.forward(10)
    if m == 8:
        pieter.left(60)
        pieter.forward(10)
    if m == 9:
        pieter.left(30)
        pieter.forward(10)

