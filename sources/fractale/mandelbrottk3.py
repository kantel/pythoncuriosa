from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import numpy as np
import numba as nb
import math, os

left   = -0.61534
right  = -0.41984
bottom = 0.65417
top    = 0.5075

width = 640
height = 480
maxlimit = 4.0
maxiter = 200

file_path = os.path.dirname(os.path.abspath(__file__))
image_folder = os.path.join(file_path, "images")

@nb.njit(locals = dict(c = nb.complex128, z = nb.complex128))
def mandelbrot(width, height, maxiter, maxlimit):
    m = [[(0, 0, 0) for j in range(width)] for i in range(height)]
    for y in range(width):
        cr = left + y*(right - left)/width
        for x in range(height):
            ci = bottom + x*(top - bottom)/height
            c = complex(cr, ci)
            z = complex(0.0, 0.0)
            for i in range(1, maxiter):
                if abs(z) > maxlimit:
                    break
                z = (z**2) + c
                if i == (maxiter - 1):
                    m[x][y] = (245, 245, 0)  # Gelb
                else:
                    m[x][y] = ((i*64)%255, (i*32%255), (i*16)%255)
    return(m)

pixels = mandelbrot(width, height, maxiter, maxlimit)

fig = Figure(figsize = (8, 6), facecolor = "white")
axis = fig.add_subplot(111)

axis.imshow(pixels)
axis.tick_params(labelbottom = False, labelleft = False, bottom = False, left = False)

fig.savefig(os.path.join(image_folder, "mandelbrot_voss2_2.png"), bbox_inches = "tight", pad_inches = 0.0)

root = tk.Tk()
root.title("Mandelbrot Set nach Herbert Voß")

canvas = FigureCanvasTkAgg(fig, master = root)
canvas._tkcanvas.pack(side = tk.TOP, fill = tk.BOTH, expand = 1)

root.mainloop()