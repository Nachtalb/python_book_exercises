#! /Python34/python.exe

#----------------------------------------------------
# Dateiname:  aufgabe2_wuerfeln.py
# Simulation 100 Würfe eines Würfels.
#
# Python 3, 6. Auflage, mitp 2016
# Kap. 30, Aufgabe 2
# Michael Weigend 22.09.2016
#----------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

bins=np.arange(1,13)

d1, d2, d3 = np.random.randint(1, 7, (3, 100))
plt.figure()
plt.hist(d1 + d2 , bins + 0.5,  facecolor="b")
plt.title("100 Würfe mit zwei Würfeln")
plt.grid(True)
plt.show()

