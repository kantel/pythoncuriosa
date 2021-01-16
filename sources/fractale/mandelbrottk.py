from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import numpy as np
import numba as nb
import math

left   = -0.25 # -2.25 -0.25
right  = 0.25  # 0.75 0.25
bottom = -1.0  # -1.5 -1.0
top    = -0.5  # 1.5 -0.5

size = 600
maxlimit = 4.0
maxiter = 1000

@nb.njit(locals = dict(c = nb.complex128, z = nb.complex128))
def mandelbrot(size, maxiter, maxlimit):
    m = [[(0, 0, 0) for j in range(size)] for i in range(size)]
    for y in range(size):
        cr = left + y*(right - left)/size
        for x in range(size):
            ci = bottom + x*(top - bottom)/size
            c = complex(cr, ci)
            z = complex(0.0, 0.0)
            for i in range(1, maxiter):
                if abs(z) > maxlimit:
                    break
                z = (z**2) + c
                if i == (maxiter - 1):
                    m[x][y] = (0, 0, 0)
                else:
                    log_iter = math.log(i)
                    m[x][y] = (int(255*(1+math.cos(3.32*log_iter))/2),
                               int(255*(1+math.cos(0.774*log_iter))/2),
                               int(255*(1+math.cos(0.412*log_iter))/2))
    return(m)

pixels = mandelbrot(size, maxiter, maxlimit)

fig = Figure(figsize = (6, 6), facecolor = "white")
axis = fig.add_subplot(111)

axis.imshow(pixels)
axis.tick_params(labelbottom = False)
axis.tick_params(labelleft = False)
axis.tick_params(bottom = False)
axis.tick_params(left = False)

root = tk.Tk()
root.title("Mandelbrot Set")

canvas = FigureCanvasTkAgg(fig, master = root)
canvas._tkcanvas.pack(side = tk.TOP, fill = tk.BOTH, expand = 1)

root.mainloop()