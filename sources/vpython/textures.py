# Textures
# nach Hans-Bernhard Woyand: Python für Ingenieure und Naturwissenschaftler, S. 235

from vpython import *

WIDTH = 400
HEIGHT = 400

scene1 = canvas(align = "left", width = WIDTH, height = HEIGHT)
scene1.title = "<hr />\t\t\t\t<b>Holzklotz</b>\t\t\t\t\t\t\t\t\t<b>Erde</b><hr /><p>"
scene1.background = color.white

scene1.select()
p1 = vector(0, 0, 0)
a1 = vector(0, 1, 1)
a = box(pos = p1,  axis = a1, texture = {"file":textures.wood})

scene2 = canvas(align = "left", width = WIDTH, height = HEIGHT)
scene2.background = color.black

scene2.select()
p2 = vector(0, 0, 0)
a2 = vector(0, 1, 0)
b = sphere(pos = p2, texture = {"file":textures.earth})
while True:
    b.rotate(angle = pi/120, axis = a2)
    rate(12)