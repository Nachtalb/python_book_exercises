# ---------------------------------------------------
# Dateiname: geldproperties.py
# Klasse Geld mit privaten Attributen und Properties
# Objektorientierte Programmierung mit Python
# Kap. 10
# Michael Weigend 20.9.2009
#----------------------------------------------------
class Geld(object):
    __wechselkurs={'USD':0.84998,
                   'GBP':1.39480,
                   'EUR':1.0,
                   'JPY':0.007168} 
    def __init__(self, waehrung, betrag):
        self.__waehrung = waehrung
        self.__betrag = float(betrag)

    def getBetrag(self):
        return self.__betrag

    def getWaehrung(self):
        return self.__waehrung

    def getEuro(self):                                 
        return self.__betrag *   \
              self.__wechselkurs[self.__waehrung]

    def setBetrag(self, neuerBetrag):
        self.__betrag = float (neuerBetrag)
        
    def setWaehrung(self, neueWaehrung):
        if neueWaehrung in self.__wechselkurs.keys():
            alt = self.__wechselkurs[self.__waehrung]
            neu = self.__wechselkurs[neueWaehrung]
            self.__betrag = alt/neu * self.__betrag
            self.__waehrung = neueWaehrung
   
    def add (self, geld):                              
        summe_in_Euro = self.getEuro()+geld.getEuro()
        summe = Geld1(self.__waehrung,
             summe_in_Euro/self.__wechselkurs[self.__waehrung])
        return summe

    betrag = property(getBetrag, setBetrag)
    waehrung = property(getWaehrung, setWaehrung)
