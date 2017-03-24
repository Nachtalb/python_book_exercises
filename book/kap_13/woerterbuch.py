# ----------------------------------------------------
# Dateiname: woerterbuch.py
# Woerter und ihre Haeufigkeit in einem Text
#
# Objektorientierte Programmierung mit Python
# Kap. 13 Lösung 3
# Michael Weigend 8. 10. 09
# ----------------------------------------------------

# woerterbuch.py
def woerter(text):
    text = text.lower()
    for p in '.,:-?!;':
        text.replace(p, '')  # 1
    liste = text.split()  # 2
    woerterbuch = []
    while liste:  # 3
        wort = liste[0]
        anzahl = 0
        while wort in liste:  # 4
            liste.remove(wort)
            anzahl += 1
        woerterbuch += [(wort, anzahl)]  # 5
        woerterbuch.sort()  # 6
    return woerterbuch


# Aufruf zum Testen der Funktion
print(woerter('Brautkleid bleibt Brautkleid und Blaukraut bleibt Blaukraut'))

input('Beenden mit <ENTER>')
