#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sinuskurve
Created on Wed Apr 19 17:59:30 2023

@author: Jörg Kantel
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def f(x, a, b, c):
    return (a*np.sin(b*np.radians(x) - np.radians(c)))

fig, ax = plt.subplots(figsize = (6, 6))
plt.title(r"$y = a\/sin(b\/(x-c))$")
plt.subplots_adjust(left = 0.12, bottom = 0.25)
plt.xlim(0, 360)
plt.ylim(-10, 10)
plt.xlabel(r"$x$")
plt.ylabel(r"$y$", rotation = 0)

x = np.arange(0, 400, 0.001)
y, = plt.plot(x, f(x, 5, 1, 0), lw = 2)

# x- und y-Position, Länge, Höhe
xyA = plt.axes([0.1, 0.12, 0.8, 0.03])
xyB = plt.axes([0.1, 0.07, 0.8, 0.03])
xyC = plt.axes([0.1, 0.02, 0.8, 0.03])

# Slider-Objekte erzeugen
sldA = Slider(xyA, "a",   2.0, 10.0, valinit = 5, valstep = 0.1)
sldB = Slider(xyB, "b",   1.0,  4.0, valinit = 1, valstep = 0.1)
sldC = Slider(xyC, "c", -90.0, 90.0, valinit = 0, valstep = 1.0)

# Slider Update
def update(val):
    a = sldA.val
    b = sldB.val
    c = sldC.val
    y.set_data(x, f(x, a, b, c))
    
# Änderungen abfragen
sldA.on_changed(update)
sldB.on_changed(update)
sldC.on_changed(update)

ax.grid(True)
plt.show()