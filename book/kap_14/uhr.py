# ----------------------------------------------------
# Dateiname: uhr.py
# Simple Uhr
#
# Objektorientierte Programmierung mit Python
# Kap. 14 
# Michael Weigend 2.6.06
# ----------------------------------------------------
from time import ctime, sleep

for i in range(5):
    print(ctime().split()[3])  # 1
    sleep(1)  # eine Sekunde schlafen
