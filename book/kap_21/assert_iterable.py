#----------------------------------------------------
# Dateiname:  assert_iterable.py 
# Beispiel für assert-Anweisung zum Testen von Vorbedingungen
#
# Objektorientierte Programmierung mit Python 3
# Kap. 21
# Michael Weigend 25.01.2013
#----------------------------------------------------


def diversität(s):
   # liefert die Anzahl unterschiedlicher Elemente einer Kollektion
   assert hasattr(s, "__iter__")
   assert len(s) > 0
   menge = set(s)
   return len(menge)
      
   
   

         










                    
