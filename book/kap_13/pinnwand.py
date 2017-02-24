#----------------------------------------------------
# Dateiname: pinnwand.py
# Modellierung einer intelligenten Pinnwand
#
# Objektorientierte Programmierung mit Python
# Kap. 13 Loesung 2
# Michael Weigend 2.10.09
#----------------------------------------------------
 
class Pinnwand(object):
    def __init__(self):
        self.__zettel = []

    def __ermittlePrioritaet(self, notiz):            #1
        return notiz.count('!')+                   \
               notiz.upper().count('WICHTIG') +    \
               notiz.upper().count('DRINGEND') +   \
               notiz.upper().count('EILT')

    def hefteAn(self, notiz):                         #2
        self.__zettel.append(
            (self.__ermittlePrioritaet(notiz), notiz))
        self.__zettel.sort()                          #3
        self.__zettel.reverse()

    def __str__(self):                
        beschreibung = 'Notizen\n'                    #4
        for z in self.__zettel:
            beschreibung += z[1]
            beschreibung += '(Prioritaet: '+str(z[0])+')\n'
        return beschreibung

    def entferne(self):
        notiz = self.__zettel[0][1]
        del self.__zettel[0]
        return notiz

class Benutzungsoberflaeche(object):                           
    __menuetext = """
(N)eue Notiz anheften          (A)lle Notizen auflisten
(W)ichtigste Notiz entfernen   (E)nde
"""

    def __init__ (self, pinnwand):                  
        self.__pw = pinnwand

    def run(self):                                     
        wahl = '-'
        print('Pinnwand')
        while wahl not in 'Ee':
            print (self.__menuetext)
            wahl = input('Ihre Wahl: ')
            if wahl in 'nN': self.__neu()
            elif wahl in 'aA': print(self.__pw)
            elif wahl in 'wW': print (self.__pw.entferne())

        print("Danke für die Verwendung der Pinnwand!")

    def __neu(self):                                  
        notiz = input('Notiz: ')
        while notiz:
            self.__pw.hefteAn(notiz)
            notiz = input('Notiz: ')

# Hauptprogramm                                       #5
pinnwand = Pinnwand()                                    
menue = Benutzungsoberflaeche(pinnwand)
menue.run()


input('Beenden mit <ENTER>')
