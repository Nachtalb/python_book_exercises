#----------------------------------------------------
# Dateiname: verzeichnisanlegen.py
#
# Objektorientierte Programmierung mit Python
# Kap. 14 Loesung 1
# Michael Weigend 8. 10. 09
#----------------------------------------------------
# verzeichnisanlegen.py
from os import makedirs
vorname = input('Vorname: ')
nachname = input('Nachname: ')
verzeichnisname = (vorname[:6]+nachname[:2]).lower()  #1
try:
    makedirs('/python/projekt/user/'+verzeichnisname) #2
    print('Verzeichnis angelegt')   
except:
    print('Verzeichnis existiert bereits')



input('Beenden mit <ENTER>')
