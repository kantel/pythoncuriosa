#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 18:10:28 2020

@author: Jörg Kantel
"""

import numpy as np
import matplotlib.pyplot as plt

def mag(v):
    vx, vy = v
    return(np.sqrt(vx**2 + vy**2))

def normalize(v):
    vx, vy = v
    m = mag(v)
    return(vx/m, vy/m)

def angle_between(v1, v2, degrees = False):
    v1x, v1y = v1
    v2x, v2y = v2
    m_v1 = mag(v1)
    m_v2 = mag(v2)
    
    angle = np.arccos((v1x*v2x + v1y*v2y)/(m_v1*m_v2))
    if degrees:
        angle = angle/np.pi*180
    
    return(angle)

def projection(v1, v2):
    vx, vy = v1
    ux, uy = normalize(v2)
    return(vx*ux + vy*uy)

fig, axes = plt.subplots()
axes.set_aspect(1)

plt.xlim(-3.0, 3.0)
plt.ylim(-3.0, 3.0)

a = ax, ay = np.random.randn(2)
# b = bx, by = 0.0, 2.0
b = bx, by = np.random.randn(2)

print(a, b)

plt.quiver(0, 0, ax, ay, scale = 1, units = "xy", color = "blue")
plt.quiver(0, 0, bx, by, scale = 1, units = "xy", color = "red")

ux, uy = normalize(b)
proj = projection(a, b)
plt.quiver(0, 0, proj*ux, proj*uy, scale = 1, units = "xy", color = "green")

print("Die Länge des Vektors a ist %5.2f" %mag(a))
print("Die Länge des Vektors b ist %5.2f" %mag(b))
print("Der Winkel zwischen a und b in Radians ist %5.2f" %angle_between(a, b))
print("Der Winkel zwischen a und b in Grad ist %0.0f" %angle_between(a, b, degrees = True))