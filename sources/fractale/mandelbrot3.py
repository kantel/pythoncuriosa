import numpy as np
import numba as nb
import matplotlib.pyplot as plt
import math

left  = -2.25
right = 0.75
bottom = -1.5
top    = 1.5

size = 600
maxlimit = 4.0
maxiter = 100

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

plt.imshow(pixels)
plt.savefig("mandel.png", bbox_inches = "tight")
plt.show()