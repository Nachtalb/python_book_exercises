# ----------------------------------------------------
# Dateiname:  test_finally.py
# Auch wenn das Speichern einer Datei nicht gelingt, wird sie
# in jedem Fall im Verzeichis temp gespeichert
# Kap. 9
# Michael Weigend 22.01.2013
# ----------------------------------------------------

daten = input('Daten: ')
pfad = input('Pfad: ')
try:
    f = open(pfad, 'w')  # 1
    f.write(daten)
    f.close()
    print('Daten im Verzeichnis "c:\\daten" gespeichert')
finally:
    f = open('/temp/daten.bak', 'w')
    f.write(daten)
    f.close()
    print('Sicherheitskopie im Verzeichnis " c:\\temp"')

print("Programm beendet")
