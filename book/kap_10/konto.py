# ---------------------------------------------------
# Dateiname: konto.py
# Modul mit Implementierung der Klasse Konto. Sie wird von
# der Klasse Geld abgeleitet und modelliert ein Bankkonto
#
# Objektorientierte Programmierung mit Python
# Kap. 10 
# Michael Weigend 20.9.2009
#----------------------------------------------------
import time
from geld2 import Geld
class Konto(Geld):
    """ Spezialisierung der Klasse Geld zur Verwaltung eines Kontos
    
        Öffentliche Attribute:
           geerbt: waehrung, betrag, wechselkurs

        Öffentliche Methoden und Überladungen:
           geerbt: __add__(), __cmp__(), getEuro()
           ueberschrieben: __str__()
           Erweiterungen:
             einzahlen(), auszahlen(), druckeKontoauszug() 
    """
    def __init__(self, waehrung, inhaber):
        Geld.__init__(self,waehrung, 0)               #1
        self.__inhaber = inhaber                      #2
        self.__kontoauszug = [str(self)]              #3

    def einzahlen(self,waehrung, betrag):             #4          
        einzahlung = Geld(waehrung,betrag)
        self.betrag =(self+einzahlung).betrag         #5
        eintrag = time.asctime()+ ' ' + str(einzahlung)+ \
                ' neuer Kontostand: ' + self.waehrung + \
                format (self.betrag, '.2f')
        self.__kontoauszug += [eintrag]               #6

    def auszahlen(self, waehrung, betrag): 
        self.einzahlen(waehrung,-betrag)

    def druckeKontoauszug(self):                      #7
        for i in self.__kontoauszug:
            print(i)
        self.__kontoauszug = [str(self)]

    def __str__(self):                                #8
        return 'Konto von ' + self.__inhaber + \
                ':\nKontostand am ' + \
                time.asctime()+ ': '+ self.waehrung + ' ' +\
                format (self.betrag, '.2f')

