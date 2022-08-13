# mandelbrot09.py

import numpy as np
import matplotlib.pyplot as plt

# teichenfläche/Ausgabefenster
fig, ax = plt.subplots(figsize = (8, 8))
cc = "Blues" # hot, Blues, plasma. gray, twilight, magma

# Iterationstiefe
N = 50

# Reelle (x) und imaginäre (y) Achse
x1, x2 = -2, 1
y1, y2 = -1.5, 1.5

x, y = np.ogrid[x1:x2:800j, y1:y2:800j]
c = x + 1j*y
z = c
with np.warnings.catch_warnings():
    np.warnings.simplefilter("ignore")
    for _ in range(N):
        z = z**2 + c
    mandelbrot = (np.abs(z) < 2).T
    
# Bildausgabe
plt.imshow(mandelbrot, cmap = cc, extent = [x1, x2, y1, y2])
plt.xlabel("Re(z)")
plt.ylabel("Im(z)", rotation = 90)
plt.tight_layout()
ax.set_aspect("equal")

plt.show()