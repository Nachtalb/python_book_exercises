#----------------------------------------------------
# Dateiname: beenden.py
#
# Python 3, 6. Auflage mitp 2016
# Kap. 14
# Michael Weigend 20.08.2016
#----------------------------------------------------
import sys

antwort = input("Programm beenden? (j/n)")
if antwort == 'j':
    sys.exit(0) 
print("Programm läuft weiter")
