import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Startwerte

B0 = 100        # Startwert Beutepopulation
R0 = 45         # Startwert Räuberpopulation
max_t = 50

# Parameter

eps1 = 0.5      # Reproduktionsrate der Beute
gamma1 = 0.0333 # Freßrate der Räuber = Sterberate der Beute
eps2 = 1.0      # Sterberate der Räuber
gamma2 = 0.01   # Reproduktionsrate der Räuber

def deriv(u, t, eps1, eps2, gamma1, gamma2):
    x, y = u
    dBdt = eps1*x - gamma1*x*y
    dRdt = -eps2*y + gamma2*x*y
    return(dBdt, dRdt)

y0 = B0, R0
T = np.linspace(0, max_t, 100*max_t)
ret = odeint(deriv, y0, T, args = (eps1, eps2, gamma1, gamma2))

b, r = ret.T

plots = plt.plot(T, b, "g", lw = 2, label = "Beute") \
        + plt.plot(T, r, "r", lw = 2, label = "Räuber")
plt.title("Lotka-Volterra-Gleichung")
plt.xlabel("Zeit [Tage]")
plt.ylabel("Anzahl")
plt.grid(True, linestyle = "--")
plt.legend(loc = "upper right")

plt.show()