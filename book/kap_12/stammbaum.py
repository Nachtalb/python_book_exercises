#----------------------------------------------------
# Dateiname: stammbaum.py
# Modellierung eines Stammbaums als rekursive Klasse
#
# Objektorientierte Programmierung mit Python
# Kap. 12 
# Michael Weigend 2. 10. 09
#----------------------------------------------------

class Stammbaum(object):
    def __init__(self, name, vater, mutter):
        self.name = name                        # String
        self.vater = vater                      #1  
        self.mutter = mutter

    def __str__(self):                          #2               
        s=""      # String-Repraesentation
        if self.name:
            s += self.name + '\n'
            if self.mutter:                     #3
                s += 'Mutter von ' + self.name + \
		     ': ' + str(self.mutter)        
            if self.vater:
                s += 'Vater von '+ self.name + \
		     ': ' + str(self.vater)
        return s

# Hauptprogramm

sarah = Stammbaum('Sarah', None, None)          #4
willy = Stammbaum('Willy', None, None)
marianne = Stammbaum('Marianne', None, None)
anton = Stammbaum('Anton', None, None)
marlene = Stammbaum('Marlene', willy, sarah)
werner = Stammbaum('Werner', anton, marianne)
jenny = Stammbaum('Jenny', werner, marlene)
print(jenny)                                     #5

input('Beenden mit <ENTER>')



