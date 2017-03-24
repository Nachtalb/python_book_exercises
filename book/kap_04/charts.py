# ---------------------------------------------------
# Dateiname: charts.py
# 
# Objektorientierte Programmierung mit Python 3
# Kap. 4 Lösung 6
# Michael Weigend Januar 2013
# ----------------------------------------------------

# charts.py
print("Bitte geben Sie die ersten Titel der Charts ein!")
charts = []
titel = input("Titel: ")
charts += [titel]
titel = input("Titel: ")
charts += [titel]
titel = input("Titel: ")
charts += [titel]
print
print("Hier sind die ersten drei Titel der Charts:")
print("Platz 1:", charts[0])
print("Platz 2:", charts[1])
print("Platz 3:", charts[2])
print()  # leere Zeile
input("Beenden mit <ENTER>")
