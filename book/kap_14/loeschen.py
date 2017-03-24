# ----------------------------------------------------
# Dateiname: loeschen.py
#
# Objektorientierte Programmierung mit Python
# Kap. 14 Lösung 2
# Michael Weigend 22.01.2013
# ----------------------------------------------------
from os import *

verzeichnis = input('Verzeichnis: ')
zaehler = 0
chdir(verzeichnis)  # 1
print('Geloeschte Dateien:')
for datei in listdir(verzeichnis):
    if datei.split('.')[-1] == 'old':  # 2
        remove(datei)  # 3
        print(datei)
        zaehler += 1
print('Es wurden %i Dateien gelöscht.' % zaehler)

input('Beenden mit <ENTER>')
