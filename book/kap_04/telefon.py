# ---------------------------------------------------
# Dateiname: telefon.py
# 
# Objektorientierte Programmierung mit Python 3
# Kap. 4 Lösung 7
# Michael Weigend 18. Januar 2013
# ----------------------------------------------------

print("Bitte geben Sie Name und Telefonnummer ein.")
liste = []
name = input("Name: ")
tel = input("Telefonnummer: ")
liste = liste + [(name, tel)]

name = input("Name: ")
tel = input("Telefonnummer: ")
liste = liste + [(name, tel)]

name = input("Name: ")
tel = input("Telefonnummer: ")
liste = liste + [(name, tel)]

print()
print("Telefonliste:")
print(liste[0][0], liste[0][1])
print(liste[1][0], liste[1][1])
print(liste[2][0], liste[2][1])

input("Beenden mit <ENTER>")
