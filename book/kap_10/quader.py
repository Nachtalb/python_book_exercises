# ----------------------------------------------------
# Dateiname: quader.py
# Modul mit Definition der Klasse Quader, die von
# Ding abgeleitet wird.
#
# Objektorientierte Programmierung mit Python
# Kap. 10 Loesung 2
# Michael Weigend 8. 10. 09
# ----------------------------------------------------

from ding import Ding


class Quader(Ding):
    def __init__(self, symbol,
                 laenge, breite, hoehe):  # 1
        Ding.__init__(self, symbol, laenge * breite * hoehe)
        self.__laenge = float(laenge)
        self.__breite = float(breite)
        self.__hoehe = float(hoehe)

    def __gt__(self, other):  # 2
        return self.getMasse() > other.getMasse()

    def __ge__(self, other):
        return self.getMasse() >= other.getMasse()

    def __eq__(self, other):
        return self.getMasse() == other.getMasse()

    def __str__(self):
        text = 'Ein Quader aus ' + \
               self._dichte[self._symbol][0] + ', ' + \
               format(self.__laenge, '.2f') + ' cm mal ' + \
               format(self.__breite, '.2f') + ' cm mal ' + \
               format(self.__hoehe, '.2f') + ' cm'
        return text


# Hauptprogramm mit Anweisungen zum Testen der Klasse Quader
silberbarren = Quader('Ag', 2, 3, 4)
print('Masse: ', silberbarren.getMasse())
print('Volumen: ', silberbarren.getVolumen())
print(silberbarren)
input('Beenden mit <ENTER>')
