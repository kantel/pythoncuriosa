#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SIR 1
Created on Mon Apr 17 20:43:17 2023

@author: Jörg Kantel
"""
import numpy as np
import matplotlib.pyplot as plt

# time unit: 1 h
beta = 10./(40*8*24)          # Infektionsrate
gamma = 3.0/(15*24)           # Genesungsrate
dt = 0.1                      # Schrittweite (6 min)
D = 30                        # Simulatsdauer in Tagen (D)
N_t = int(D*24/dt)            # Zeitsschritte (Tage*Stunden/dt)

t = np.linspace(0, N_t*dt, N_t + 1)
S = np.zeros(N_t + 1)
I = np.zeros(N_t + 1)
R = np.zeros(N_t + 1)

# Initialisierung der Variablen
S[0] = 50                     # Anzahl Personen
I[0] = 1                      # davon infiziert
R[0] = 0                      # und genesen

## Schleife über die Zeit
for n in range(N_t):
    S[n+1] = S[n] - dt*beta*S[n]*I[n]
    I[n+1] = I[n] + dt*beta*S[n]*I[n] - dt*gamma*I[n]
    R[n+1] = R[n] + dt*gamma*I[n]


# Ergebnis plotten
fig = plt.figure()
l1, l2, l3 = plt.plot(t, S, t, I, t, R)
plt.title("S-I-R-Modell einer Grippe-Pandemie")
fig.legend((l1, l2, l3), ("S: Gesunde", "I: Infizierte", "R: Genesende"),
           loc = "center right")
plt.xlabel("Zeit = Stunden")
plt.ylabel("Anzahl Personden")
plt.show()

print("I did it, Babe!")