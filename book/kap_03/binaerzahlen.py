#-----------------------------------------------------
# Dateiname: binaerzahlen.py
# Version: 1.0
# Funktion: Vierstellige Binärzahlen werden ausgegeben
# Autor: Michael Weigend 
# Datum der letzten Änderung: 26.09.09
#-----------------------------------------------------

for i3 in [0, 1]:
    for i2 in [0, 1]:
        for i1 in [0, 1]:
            for i0 in [0, 1]:
                print(i3,i2, i1, i0, end="   ")
                # ende for i0 ...
            # ende for i1 ...
        print()
        # ende for i2 ...
    # ende for i3 ...


