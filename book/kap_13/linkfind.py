# ----------------------------------------------------
# Dateiname: linkfind.py
# Suche nach Hyperlinks in einem Text
#
# Python 3, 6. Auflage mitp 2016
# Kap. 13
# Michael Weigend 20.8.2016
# ----------------------------------------------------
from re import *


def linkfind(datei):
    re = compile('http://.+html?', I)  # 1
    f = open(datei, 'r')
    text = f.read()
    f.close()
    return re.findall(text)  # 2


linkliste = linkfind('/python35/README.txt')
print('Links in der Python-README-Datei:')
for link in linkliste: print(link)

input('Beenden mit <ENTER>')
