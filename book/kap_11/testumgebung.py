#----------------------------------------------------
# Dateiname: testumgebung.py
# Testumgebung fuer Klasse Geld
#
# Objektorientierte Programmierung mit Python
# Kap. 11 
# Michael Weigend 8. 10. 09
#----------------------------------------------------
import sys
sys.path.append('module')
sys.path.append(r'c:\projekt\module')
from geld import Geld 
print("Test der Klasse Geld")
print()
anweisung = input('Anweisung: ')
while anweisung !=  '':
    try:
        exec(anweisung)  # Anweisung wird ausgeführt
    except:
        print ("Fehler: " + str(sys.exc_info()[0]))
    anweisung = input('Anweisung: ')
print("Ende des Tests")
