#! /Python34/python.exe

# ----------------------------------------------------
# Dateiname:  thermometer.py
# Von einem digitalen Messgerät, dass den Widerstand
# eines Pt-100-Thermometers misst, wird in regelmäßigen 
# Zeitabständen die Display-Anzeige (natürliche Zahl)
# übernommen und daraus die Temperatur berechnet.
# Die Werte werden in einer Datei gespeichert.
#
# Python 3, 6. Auflage, mitp 2016
# Kap. 31.3
# Michael Weigend 22.09.2016
# ----------------------------------------------------
from time import sleep

from dmm import get_number

f = open('daten.csv', mode='w')
t = 0
print('Wie lange soll gemessen werden?')
max_time = int(input('Sekunden: '))
print('In welchen Zeitabständen?')
dt = int(input('Sekunden: '))
f.write('Zeit (s); Temperatur (°C)\n')
while t < max_time:
    n = get_number()
    temp = (n / 10 - 100) / 0.39
    f.write(' %i;%.1f;\n' % (t, temp))
    print(' %4i Sekunden %5.1f °C ' % (t, temp))
    sleep(dt)
    t += dt
f.close()
