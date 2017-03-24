# ----------------------------------------------------
# Dateiname:  primfak.py
# Modul mit Funktion primfak(), die eine
# natuerliche Zahl in Primfaktoren zerlegt.
# Pruefung von Vor- und Nachbedingung.
#
# Objektorientierte Programmierung mit Python
# Kap. 21
# Michael Weigend 16. 10. 09
# ----------------------------------------------------

def primfak(zahl):
    # Prüfe Vorbedingung
    assert type(zahl) == int and zahl > 0
    x = zahl
    fak = [1]
    faktor = 2
    while x > 1:
        while x % faktor == 0:
            fak.append(faktor)
            x /= faktor
        faktor += 1
    # Prüfe Nachbedingung
    produkt = 1
    for i in fak: produkt *= i
    assert produkt == zahl
    return fak


if __name__ == "__main__":
    print(primfak(6))
    print(primfak(-2))
