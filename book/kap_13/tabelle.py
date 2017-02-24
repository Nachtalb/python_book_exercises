#----------------------------------------------------
# Dateiname: tabelle.py
# Ausgabe eines Analyseergebnisses
#
# Objektorientierte Programmierung mit Python
# Kap. 13
# Michael Weigend 2.10.09
#----------------------------------------------------
tabelle=""
for i in range(1, 6):
    tabelle +="{a:>10}{b:>10}{c:>10}\n".format(
        a=i, b=i**2, c=i**3)
    

print (tabelle)


input('Beenden mit <ENTER>')
