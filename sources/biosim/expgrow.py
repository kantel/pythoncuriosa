# Exponentielles Wachstum

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

r = 0.5   # Wachstumsrate

tmax = 24
y0 = [1]
ti = [0, tmax]

# Differentialgleichung für exponentielles Wachstum
def expgrow(t, y0, r):
    N = y0
    dn_dt = r*N
    return(dn_dt)

t = np.linspace(0, tmax, 500)
z = solve_ivp(expgrow, ti, y0, args = (r,), dense_output = True)
N_t = z.sol(t)

# Plot
plt.figure(figsize = (8, 6))
plt.title("Exponentielles Wachstum")
plt.plot(t, N_t.flatten(), "g", lw = 2)
plt.xlabel("Zeit")
plt.ylabel("Anzahl")
plt.grid(True)
plt.show()