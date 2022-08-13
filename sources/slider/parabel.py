# parabel.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def f(a, b, c):
    return(a*(x - b)**2 + c)

# Plot und Plotausrichtung
fig, ax = plt.subplots(figsize = (5, 5))
plt.title("Parabel")
plt.subplots_adjust(left = 0.15, bottom = 0.25)
plt.xlim(-5.5, 5.5)
plt.ylim(-10, 10)
plt.xlabel("x")
plt.ylabel("y", rotation = 0)

# Berechnung
x = np.arange(-5.5, 5.5, 0.001)
y, = plt.plot(x, f(1, 0, -10), lw = 2)

# Slider Pos
xyA = plt.axes([0.1, 0.12, 0.8, 0.03])
xyB = plt.axes([0.1, 0.07, 0.8, 0.03])
xyC = plt.axes([0.1, 0.02, 0.8, 0.03])
# Slider Objeekte erzeugen
sldA = Slider(xyA, "a", -2.0, 2.0, valinit = 1, valstep = 0.01)
sldB = Slider(xyB, "b", -5.0, 5.0, valinit = 0, valstep = 0.01)
sldC = Slider(xyC, "a", -10.0, 10.0, valinit = -10, valstep = 0.01)

def update(val):
    a = sldA.val
    b = sldB.val
    c = sldC.val
    y.set_data(x, f(a, b, c))
    fig.canvas.draw_idle()
    
# Änderungen abfragen
sldA.on_changed(update)
sldB.on_changed(update)
sldC.on_changed(update)

ax.grid(True)
plt.show()
print("I did it, Babe!")