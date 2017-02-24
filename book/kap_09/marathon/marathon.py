# ---------------------------------------------------
# Dateiname: marathon.py
# Abspeichern der Ankunftzeiten von Rennläufern
# Objektorientierte Programmierung mit Python
# Kap. 9 Lösung 1
# Michael Weigend 8. 10. 09
#----------------------------------------------------
# marathon.py
import time
print("Marathon")
print()
nummer = "  "                                         #1
daten = open("/marathon/daten.txt", "w")
while nummer != "":
    nummer = input("Startnummer (Ende mit <Enter>): ")
    daten.write(nummer + ": " + time.asctime() + "\n")#2
    daten.flush()                                     #3
print()
print("Die Daten befinden sich in der Datei /marathon/daten.txt")
daten.close()                                         #4

                
    
