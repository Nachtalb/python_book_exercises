# ---------------------------------------------------
# Dateiname: heron1.py
# Wurzelberechnung nach Heron - schnellere Version
# Objektorientierte Programmierung mit Python 3
# Kap. 6 Lösung 3
# Michael Weigend Januar 2013
# ----------------------------------------------------
def wurzel(x, n=20):
    if n == 1:
        return 1
    else:
        vorigeNaeherung = wurzel(x, n - 1)
        return 0.5 * (vorigeNaeherung + float(x) / vorigeNaeherung)


print(wurzel(2))
input("Beenden mit <ENTER>")
