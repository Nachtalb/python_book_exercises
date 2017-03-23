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
# Objektorientierte Programmierung mit Python 3
# Kap. 24  
# Michael Weigend 29.1.2013
# ----------------------------------------------------

import hashlib
import sqlite3


def show_users(c):
    print("-" * 20)
    print('Liste der User-Namen:')
    c.execute("SELECT * FROM person")
    for zeile in c: print(zeile[0])
    print("-" * 20)


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

        inp = "x"
        show_users(c)
        while inp != "":
            inp = menu()
            if inp in ["A", "a"]:
                add(c, verbindung)
            elif inp in ["D", "d"]:
                delete(c, verbindung)
            elif inp in ["E", "e"]:
                break

        c.close()
        verbindung.close()


def delete(c, verbindung):
    print("Benutzer entfernen")
    dele = input('Zu entfernender User (Ende mit RETURN): ')
    while dele:
        if list(c.execute("""SELECT * FROM person WHERE name=?""", (dele,))):
            c.execute("""DELETE FROM beitrag WHERE autor = ?""", (dele,))
            c.execute("""DELETE FROM person WHERE name = ?""", (dele,))
            verbindung.commit()
            print("Benutzer entfernt.\n")
            show_users(c)
        else:
            print("Dieser Benutzer existiert nicht.")
        dele = input('Zu entfernender User (Ende mit RETURN): ')  # Achtung, Einrückung


def add(c, verbindung):
    print("Neue User anlegen. (Name ist provisorisches Passwort)")
    neu = input('Neuer User (Ende mit RETURN): ')
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
            print("Neuer User hinzugefügt.\n")
            show_users(c)
        neu = input('Neuer User: ')  # Achtung, Einrückung!


def menu():
    print("(D)elete")
    print("(A)dd")
    print(end=": ")
    return input()


Admin('redaktion.db')
