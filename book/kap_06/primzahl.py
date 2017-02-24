def primzahl (zahl):
    if zahl <= 2:
        prim = True
    else:
       for i in range(2,zahl):
           if zahl%i == 0:
               prim = False
               break
       else:
            prim = True
    return prim
            

z = input("Zahl: ")

print (primzahl (int(z)))
input("Beenden mit <ENTER>")
