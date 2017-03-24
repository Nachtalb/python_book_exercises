#! /Python34/python.exe

# ----------------------------------------------------
# Dateiname:  diffusion.py
# Simulation einer eindimensionalen Diffusion.
#
# Python 3, 6. Auflage, mitp 2016
# Kap. 30
# Michael Weigend 22.09.2016
# ----------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

n_particles = 200  # Anzahl der Partikel
t_max = 100  # Gesamter Beobachtungszeitraum
t = np.arange(t_max)
steps = 2 * np.random.randint(0, 2, (n_particles, t_max)) - 1
positions = np.cumsum(steps, axis=1)
sq_d = positions ** 2
mean_sq_d = np.mean(sq_d, axis=0)
plt.figure()
plt.plot(t, np.sqrt(mean_sq_d), 'b.',
         np.sqrt(t), '-')
plt.xlabel("Zeit")
plt.ylabel("Mittlere Verschiebung")
plt.legend(("Simulation", "Theorie"), loc=(0.6, 0.1))
plt.show()
