# Extend Ticket selling manager

## Description 
Extend the ticket selling manager, so it can print the tickets. The printer should be made with a
private method. <br>
It should be able to print out the following: Title of the musical, date and time of the event 
row and number of the booked seat, name of the buyer and the entry fee.

## Code / Answer
```python

allePlaetze = []

#...

allePlaetze.append((int(reihe) - 1, int(platz) - 1))

#...

if allePlaetze:
    self.__drucken(vorstellung, zuschauer, allePlaetze)

#...

def __drucken(self, vorstellung, zuschauer, plaetze):
    print()
    print("------------")
    print("|  TICKET  |")
    print("------------")
    print("Musical: " + self.__musical.titel, "Vorstellung am: " + vorstellung.datum +
          " um " + vorstellung.beginn, "Zugunsten von: " + zuschauer.name, "Telefonummer: " + zuschauer.tel,
          sep="\n")
    print("Plätze: ")
    for p in plaetze:
        print("Reihe: " + str(p[0]) + "\tPlatz: " + str(p[1]))
```

## Example use
```
              W I L L K O M M E N
beim Buchungssystem für das Musical Hairspray

    Musical-Ticketservice
    ---------------------
    (B)uchung
    (U)eberblick Vorstellungen
    (E)nde
    
Auswahl: B
Datum der Vorstellung: 1. 10. 2010
Saalbelegung
   Platz: 1  2  3  4  5  6  7  8  9  10 11 12 13 14
Reihe  1: -- -- Mü Sc Sc -- -- -- -- -- 
Reihe  2: Ka Ka -- Me Me -- -- -- -- -- -- -- 
Reihe  3: -- Ni Ni -- -- -- -- -- -- -- -- -- 
Reihe  4: -- Ni Ni -- -- -- -- -- -- -- 

Name: Herrmann Schulz
Telefonnummer: 012 345 67 89
Reihe: 1
Platz: 1
Platz gebucht
Reihe: 1
Platz: 2
Platz gebucht
Reihe: 

------------
|  TICKET  |
------------
Musical: Hairspray
Vorstellung am: 1. 10. 2010 um 20.00 Uhr
Zugunsten von: Herrmann Schulzt
Telefonummer: 012 345 67 89
Plätze: 
Reihe: 0	Platz: 0
Reihe: 0	Platz: 1

    Musical-Ticketservice
    ---------------------
    (B)uchung
    (U)eberblick Vorstellungen
    (E)nde
    
Auswahl: 
```