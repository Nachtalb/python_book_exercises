# ---------------------------------------------------
# Dateiname: noch_einmal.py
# 
# Objektorientierte Programmierung mit Python
# Quaderberechnung.py
# Michael Weigend 1. 10. 09
#----------------------------------------------------
# 
print "Berechnung des Volumens eines Quaders"
antwort = 'j'
while antwort == 'j':
    l = input ("Länge in cm: ")
    b = input ("Breite in cm: ")
    h = input("Höhe in cm:")
    volumen = l*b*h
    print ("Das Volumen ist", volumen, "ccm.")
    antwort = input("Noch einmal? (j, n) ")
print ("Vielen Dank für die Benutzung dieses Programms")
