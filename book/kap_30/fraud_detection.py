#! /Python34/python.exe

#----------------------------------------------------
# Dateiname:  fraud_detection.py
# Die Daten in der Datei groesse.dat(Größenangaben)
# werden mit einer Normalverteilung verglichen.
#
# Python 3, 6. Auflage, mitp 2016
# Kap. 30.15
# Michael Weigend 23.10.2016
#----------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

mean = 165.4
sd = 4.5
bins=np.arange(140, 200, 2)

data = np.loadtxt("groesse.dat").ravel()
normal = mean + sd * np.random.randn(1000000)

plt.figure(1)
plt.subplot(2,1,1)
plt.hist(normal, bins, normed=1, facecolor="b", alpha=0.75)               
plt.title("Körpergröße - Normalverteilung")
plt.grid(True)

plt.subplot(2,1,2)
plt.hist(data, bins, normed=1, facecolor="r", alpha=0.50)               
plt.title("Körpergröße - Stichprobe")
plt.grid(True)
plt.show()

