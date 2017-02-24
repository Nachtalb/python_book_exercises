# ---------------------------------------------------
# Dateiname: statisch.py
# Beispiel fuer die Definition statischer Methoden
# Objektorientierte Programmierung mit Python
# Kap. 10
# Michael Weigend 20.4.2006
#----------------------------------------------------
class Statistik(object):
    def mittelwert(s):
        if s:
            return float(sum(s)) / len(s)

    def spannweite(s):
        # groesste minus kleinste Zahl der Zahlenliste s
        if s:
            return max(s) - min(s)

    def median(s):
        if s:
            s1 = sorted(s)
            if len(s)%2==0: # Laenge ist gerade
                return (s1[len(s)/2-1] + s1[len(s)/2])/2.0
            else:
                return s1[(len(s)-1)/2]

    
    mittelwert = staticmethod(mittelwert)
    spannweite = staticmethod(spannweite)
    median = staticmethod(median)
    

        

