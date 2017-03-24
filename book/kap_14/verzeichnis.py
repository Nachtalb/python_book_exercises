# ----------------------------------------------------
# Dateiname: verzeichnis.py
# Gibt Namen der Dateien im Arbeitsverzeichnis aus
#
# Objektorientierte Programmierung mit Python
# Kap. 14 
# Michael Weigend 8. 10. 09
# ----------------------------------------------------
import os

for datei in os.listdir(os.getcwd()):
    zeile = '{datei:>30}{bytes:>10} byte'.format(
        datei=datei,
        bytes=os.path.getsize(datei))
    print(zeile)
