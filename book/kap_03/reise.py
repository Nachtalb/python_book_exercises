# ------------------------------------------------------
# Dateiname: reise.py
# Aufgabe: Berechnung des Kostenplans für eine Reise
# Autor: Michael Weigend
# Datum der letzten Änderung: 28.09.2009
#-------------------------------------------------------
print("Kostenplan für eine Reise")       
print("-------------------------")

# Eingabe
bus = float(input("Kosten für den Reisebus: "))
hotel = float(input("Hotelkosten pro Person: "))
events = float(input("Gesamtkosten für touristische Events: "))
personen = int(input("Anzahl der Teilnehmer: "))

# Verarbeitung
gesamtkosten = bus + events + personen*hotel
kostenProPerson = gesamtkosten/personen

# Ausgabe
print()
print("Die Gesamtkosten betragen", gesamtkosten, "EUR.")
print("Die Kosten pro Person sind", kostenProPerson, "EUR.")

