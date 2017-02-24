#----------------------------------------------------
# Dateiname:  q_gleichung.py 
# Modul mit Funktion q_gleichung(), die eine
# quadratische Gleichung löst.
#
# Objektorientierte Programmierung mit Python
# Kap. 21
# Michael Weigend 16. 10. 09
#----------------------------------------------------

from math import *
def q_gleichung(p, q):
   # Vorbedingung
   assert ((p/2)**2 - q) >= 0 
   x1 = -p/2.0 + sqrt((p/2.0)**2 - q)
   x2 = -p/2.0 - sqrt((p/2.0)**2 - q)
   # Nachbedingung
   assert (x1**2 + p*x1 + q == 0) and (x2**2 + p*x2 + q == 0)
   return x1, x2











                    
