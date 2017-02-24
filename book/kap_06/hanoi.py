# ---------------------------------------------------
# Dateiname: hanoi.py
# Rekursive Berechnung einer Loesung des Problems
# "Die Tuerme von Hanoi"
# Objektorientierte Programmierung mit Python 3
# Kap. 6 Loesung 4
# Michael Weigend 1. 10. 03
#----------------------------------------------------

def bewege(n, von, ueber, nach):
        if n==1:
            print ('Lege eine Scheibe von', von, 'nach', nach,'.')
        else:
            bewege(n-1, von, nach, ueber)
            bewege(1, von, ueber, nach)
            bewege (n-1, ueber, von, nach)
        
    
bewege (3,1,2,3)
input("Beenden mit <ENTER>")
