# ---------------------------------------------------
# Dateiname: geld.py
# Modul mit Definition der Klasse Geld
# Objektorientierte Programmierung mit Python
# Kap. 10
# Michael Weigend 17.9.2009
# ----------------------------------------------------
class Geld(object):  # 1
    wechselkurs = {'USD': 0.84998,
                   'GBP': 1.39480,
                   'EUR': 1.0,
                   'JPY': 0.007168}  # 2

    def __init__(self, waehrung, betrag):  # 3
        self.waehrung = waehrung
        self.betrag = float(betrag)

    def getEuro(self):  # 4
        return self.betrag * self.wechselkurs[self.waehrung]

    def add(self, geld):  # 5
        summe_in_Euro = self.getEuro() + geld.getEuro()
        summe = Geld(self.waehrung,
                     summe_in_Euro / self.wechselkurs[self.waehrung])
        return summe
