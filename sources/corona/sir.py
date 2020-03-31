import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Startwerte
S0, I0, R0 = 0.99,0.01, 0.0

# Annahmen zur Infektionsrate und zur Heilungsrate
transm, recov = 3.2, 0.23
max_t = 20                #Zeit[Tage]

# Flatten the Curve
# transm, recov = 0.5, 0.14
# max_t = 50

def deriv(u, t, transm, recov):
    S, I, R = u
    dSdt = -transm * S * I
    dIdt = transm * S * I - recov * I
    dRdt = recov * I
    return(dSdt, dIdt, dRdt)

y0 = S0, I0, R0
T = np.linspace(0, max_t, 10*max_t)

ret = odeint(deriv, y0, T, args = (transm, recov))
S, I, R = ret.T

plots = plt.plot(T, S, "b", lw = 2, label = "Susceptible") \
    + plt.plot(T, I, "r", lw = 2, label = "Infected") \
    + plt.plot(T, R, "g", lw = 2, label = "Recovered/Removed")
plt.title("Coronavirus-Kurve")
# plt.title("Flatten the Curve")
plt.xlabel("Zeit [Tage]")
plt.ylabel("Anzahl")
plt.legend(loc = "upper right")
plt.show()