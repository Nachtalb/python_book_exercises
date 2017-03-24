# ----------------------------------------------------
# Dateiname:  admin.py
# Administration eines Redaktionssystems.
# Die Datenbank-Tabellen für User und Beiträge werden initialisiert
# (falls sie nich nicht existieren).  
# Ausserdem wird die Einrichtung neuer Benutzer ermöglicht.
#
# Dieses Skript muss so gespeichert werden, dass nur
# der Administrator Zugriffsrechte hat 
#
# Python 3, 6. Auflage, mitp 2016
# Kap. 24
# Michael Weigend 22.08.2016
# ----------------------------------------------------

import hashlib
import sqlite3


class Admin(object):
    def __init__(self, db_pfad):
        verbindung = sqlite3.connect(db_pfad)
        c = verbindung.cursor()
        try:
            c.execute("SELECT * FROM person")
            c.execute("SELECT * FROM beitrag")
        except:
            # Tabellen existieren noch nicht
            c.execute("""CREATE TABLE
                       person(name VARCHAR(50),
                              fingerprint BINARY(16))
                  """)
            c.execute("""CREATE TABLE
                       beitrag(titel VARCHAR(100),
                               text VARCHAR(1000),
                               verfallsdatum FLOAT,
                               autor VARCHAR(50))
                  """)
            verbindung.commit()

        print('Liste der User-Namen:')
        c.execute("SELECT * FROM person")
        for zeile in c: print(zeile[0])
        neu = input('Neuer User (Ende mit ENTER): ')
        while neu:
            if list(c.execute("""SELECT *
                           FROM person
                           WHERE name = ?;""", (neu,))):
                print('Name existiert bereits.')
            else:
                m = hashlib.md5(neu.encode("utf-8"))
                c.execute("""INSERT INTO person
                    VALUES(?, ?);""",
                          (neu, m.digest()))
                verbindung.commit()
            neu = input('Neuer User (ENDE mit ENTER): ')
        print("Datenbank wurde aktualisiert.")
        c.close()
        verbindung.close()


Admin('redaktion.db')
