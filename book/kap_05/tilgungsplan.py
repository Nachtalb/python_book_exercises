# ---------------------------------------------------
# Dateiname: tilgungsplan.py
# 
# Objektorientierte Programmierung mit Python
# Kap. 5 Loesung 6
# Michael Weigend 1. 10. 03
# ----------------------------------------------------
print("Berechnung des Tilgungsplans für einen Kredit")
print()
schulden = float(input("Kreditsumme in Euro: "))
zinssatz = float(input("Zinssatz (Prozent pro Jahr): "))
rueckzahlung = float(input("Jährliche Rückzahlung in Euro: "))
jahr = 2003
while schulden > rueckzahlung:
    zinsen = schulden * zinssatz / 100
    tilgung = rueckzahlung - zinsen
    schulden = schulden - tilgung
    jahr += 1
    print(jahr, " Zinsen:", zinsen, "EUR",
          " Tilgung:", tilgung, "EUR", " Restschulden:",
          schulden, "EUR")
print("Restforderung:", schulden, "Euro")

input("Beenden mit <ENTER>")
