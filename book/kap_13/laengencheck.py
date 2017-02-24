#----------------------------------------------------
# Dateiname: laengencheck.py
# Ermittelt die mittlere Satzlänge in einem Text
#
# Python 3, 6. Auflage mitp 2016
# Kap. 13
# Michael Weigend 20.8.2016
#----------------------------------------------------
from re import *
def laengencheck(datei):
    re = compile('[.,;:!?]+\s')                       #1
    f = open(datei,'r')
    text = f.read()
    f.close()
    anzahl = len(re.split(text))                      #2
    laenge = float(len(text.split())) / anzahl        #3
    return laenge

print('Mittlere Satzlänge in der README-Datei:')
print(laengencheck('/python35/README.txt'), 'Wörter')


input('Beenden mit <ENTER>')
