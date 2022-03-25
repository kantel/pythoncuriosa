import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint

# Parameter
sigma = 10.0
beta = 8 / 3.0
rho = 28.0

# Die Lorenzgleichung
def lorenz(u, t, sigma, beta, rho):
    x, y, z = u
    dxdt = sigma * (y - x)
    dydt = rho * x - y - x * z
    dzdt = x * y - beta * z
    return (dxdt, dydt, dzdt)


# Startwerte und Initialisierung
y0 = 5.0, 5.0, 5.0
t = np.linspace(0, 20, 2000)

solution = odeint(lorenz, y0, t, args=(sigma, beta, rho))

X, Y, Z = solution[:, 0], solution[:, 1], solution[:, 2]

fig1 = plt.figure()
ax1 = fig1.add_subplot(111, projection="3d", title="Lorenz-Attraktor")
ax1.plot(X, Y, Z, "r")

fig2 = plt.figure()
ax2 = fig2.add_subplot(221)
ax2.plot(t, X, "b")
ax3 = fig2.add_subplot(222)
ax3.plot(t, Y, "c")
ax4 = fig2.add_subplot(223)
ax4.plot(t, Z, "m")
ax5 = fig2.add_subplot(224)
ax5.plot(Y, Z, "r")
plt.show()
