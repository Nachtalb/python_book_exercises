# ----------------------------------------------------
# Dateiname: behaelter.py
# Demonstration eines tyoischen Fehlers
#
# Objektorientierte Programmierung mit Python
# Kap. 10 
# Michael Weigend 1. 10. 09
# ----------------------------------------------------

class Behaelter(object):
    def __init__(self, volumen):
        self.volumen = volumen  # Volumen in Milliliter

    def setVolumen(self, neuesVolumen):
        self.__volumen = float(neuesVolumen)

    def getVolumen(self):
        return self.__volumen


# Hauptprogramm
tasse = Behaelter(250)
print('In der Tasse sind', tasse.volumen, 'ml.')
ex = input('Wie viel wollen Sie ausschütten?')
tasse.volumen = tasse.volumen - float(ex)  # 1 Volumen groß geschrieben
print('Neuer Inhalt:', tasse.volumen, 'ml')
