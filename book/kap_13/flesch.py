# ----------------------------------------------------
# Dateiname: flesch.py
# Flesch-Analyse eines Textes
#
# Python 3, 6. Auflage mitp 2016
# Kap. 13
# Michael Weigend 20.8.2016
# ----------------------------------------------------

from re import *


class Flesch(object):
    def __init__(self, datei):
        f = open(datei, 'r')
        self.text = f.read()
        f.close()

    def anzahlWorte(self):
        return len(self.text.split())  # 1

    def anzahlSaetze(self):
        re = compile('[!?.;:]+\s')  # 2
        return len(re.split(self.text))

    def anzahlSilben(self):
        re = compile('[aeiou]+', I)  # 3
        return len(re.split(self.text))

    def readability(self):
        asl = float(self.anzahlWorte()) / self.anzahlSaetze()
        asw = float(self.anzahlSilben()) / self.anzahlWorte()
        return int(206.835 - 1.015 * asl - 84.6 * asw)

    def __str__(self):
        return 'Lesbarkeitsindex nach Flesch: ' + \
               str(self.readability())


print(Flesch('/python35/README.txt'))

input('Beenden mit <ENTER>')
