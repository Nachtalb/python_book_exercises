# ----------------------------------------------------
# Dateiname: geld.py
# Modul mit Definition der Klasse Geld und Testanweisungen
#
# Objektorientierte Programmierung mit Python
# Kap. 11 
# Michael Weigend 10.1.2010
# ----------------------------------------------------
# geld.py
class Geld(object):
    wechselkurs = {'USD': 0.84998,
                   'GBP': 1.39480,
                   'EUR': 1.0,
                   'JPY': 0.007168}

    def __init__(self, waehrung, betrag):
        self.waehrung = waehrung
        self.betrag = float(betrag)

    def getEuro(self):
        return self.betrag * self.wechselkurs[self.waehrung]

    def __add__(self, geld):
        a = self.getEuro()
        b = geld.getEuro()
        faktor = 1.0 / self.wechselkurs[self.waehrung]
        summe = Geld(self.waehrung, (a + b) * faktor)
        return summe

    def __lt__(self, other):
        a = self.getEuro()
        b = other.getEuro()
        return a < b

    def __le__(self, other):
        a = self.getEuro()
        b = other.getEuro()
        return a <= b

    def __eq__(self, other):
        a = self.getEuro()
        b = other.getEuro()
        return a == b

    def __str__(self):
        return self.waehrung + ' ' + format(self.betrag, '.2f')

        # Hauptprogramm – Testumgebung


if __name__ == '__main__':  # 1
    eur100 = Geld('EUR', 100)
    usd100 = Geld('USD', 100)
    print('100 Euro: ', eur100)
    print('100 EUR + 100 USD: ', eur100 + usd100)
    print('100 EUR > 100 USD : ', eur100 > usd100)
    print('100 EUR == 100 EUR : ', eur100 == Geld('EUR', 100))
    print('100 USD in Euro: ', usd100.getEuro())
