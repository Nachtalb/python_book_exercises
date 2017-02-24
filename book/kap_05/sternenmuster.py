# ---------------------------------------------------
# Dateiname: sternenmuster.py
# Ausgabe von Sternenmustern
# Objektorientierte Programmierung mit Python 3
# Kap. 5 Loesung 8
# Michael Weigend 1. 10. 09
#----------------------------------------------------


# drei Zeilen mit je 4 Sternen
for i in range(3):
    print("* * * *")

# Sternendreieck 1
for i in range(5):
    print ((i+1)*"* ")

# Sternendreieck 2
for i in range(4):
    print ((3-i)*"  ",(2*i + 1)*"* ")


input("Beenden mit <ENTER>")
                    
       
                
