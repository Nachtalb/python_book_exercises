# ---------------------------------------------------
# Dateiname: charts.py
# 
# Objektorientierte Programmierung mit Python 3
# Zerlegung eines Geldbetrages in Scheine und Münzen
# Michael Weigend 1. 10. 09
#----------------------------------------------------

geld = input("Geldbetrag in Euro: ")
geld = int(geld)
zwanziger = geld // 20
geld = geld % 20
zehner  =geld // 10
geld = geld % 10
fuenfer = geld // 5
geld = geld % 5
zweier = geld // 2
einer = geld % 2
print("Der Betrag setzt sich wie folgt zusammen:")
print(zwanziger, "mal 20 Euro")
print(zehner, "mal 10 Euro")
print(fuenfer, "mal 5 Euro")
print(zweier, "mal 2 Euro")
print(einer, "mal 1 Euro")

