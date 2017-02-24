# ---------------------------------------------------
# Dateiname: geld2.py
# Klasse Geld mit Überladung der Operatoren +, <, >, ==
# Objektorientierte Programmierung mit Python
# Kap. 10
# Michael Weigend 20.9.2009
#----------------------------------------------------
class Geld(object):  
    wechselkurs={'USD':0.84998,
                 'GBP':1.39480,
                 'EUR':1.0,
                 'JPY':0.007168}         

    def _berechneEuro(self):                         #1
        return self.betrag*self.wechselkurs[self.waehrung]

    def __init__(self, waehrung, betrag): 
        self.waehrung=waehrung
        self.betrag=float(betrag)

    def __add__ (self, geld):                        #2
        a = self._berechneEuro()
        b = geld._berechneEuro()
        faktor=1.0/self.wechselkurs[self.waehrung]
        summe = Geld (self.waehrung, (a+b)*faktor )
        return summe

    def __lt__(self, other):
        a = self.getEuro () 
        b = other.getEuro ()
        return a < b
        
    def __le__(self, other):
        a = self.getEuro () 
        b = other.getEuro ()
        return a <= b

    def __eq__(self, other):
        a = self.getEuro () 
        b = other.getEuro ()
        return a == b
        
    def __str__(self):
        return self.waehrung + ' ' + format(self.betrag, '.2f')


