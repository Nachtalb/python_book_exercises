#----------------------------------------------------
# Dateiname: zugriffszeit.py
# Ermittelt, wie lange die README-Datei
# nicht mehr gelesen worden ist.
#
# Python 3, 6. Auflage, mitp 2016
# Kap. 14
# Michael Weigend 20.08.2016
#----------------------------------------------------
import time
import os
zugriffszeit = os.path.getatime('/python33/README.txt')
aktuelleZeit = time.time()    # Sekunden seit dem 1.1.1970
ausgabe = """Die readme-Datei ist seit {} Stunden
nicht mehr gelesen worden.
""".format(int((aktuelleZeit-zugriffszeit)/3600))
print(ausgabe)



input('Beenden mit <ENTER>')
