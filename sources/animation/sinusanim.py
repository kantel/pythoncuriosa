import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

TWOPI = 2*np.pi

fig, ax = plt.subplots()

t = np.arange(0.0, TWOPI, 0.001)
s = np.sin(t)

l = plt.plot(t, s)
ax = plt.axis([0, TWOPI, -1, 1])

redDot, = plt.plot([0], [np.sin(0)], "ro")

def animate(i):
    redDot.set_data(i, np.sin(i))
    return redDot,
    
anim = FuncAnimation(fig, animate, frames = np.arange(0.0, TWOPI, 0.05),
                interval = 10, blit = True, repeat = True)

anim.save("sin.gif", writer = PillowWriter(fps = 30))

plt.show()