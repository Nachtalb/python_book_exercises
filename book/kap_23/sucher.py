#----------------------------------------------------
# Dateiname: sucher.py
# Befragt Suchmaschine, wieviele Web-Dokumente sie zu
# einem Suchbegriff findet.
#
# Objektorientierte Programmierung mit Python 3
# Kap. 23
# Michael Weigend 30.1.2013
#----------------------------------------------------

# sucher.py
from http.client import HTTPConnection
from re import *

class Sucher(object):
  def __init__(self):
    suchwort = input('Suchwort: ')
    while suchwort:
      ergebnis = self.suche(suchwort)
      print(ergebnis)
      suchwort = input('Suchwort: ')
    print('Auf Wiedersehen ...')

  def suche (self, suchwort):
    verbindung = HTTPConnection('www.google.de')        #1
    verbindung.request('GET', '/search?q='+suchwort)    #2
    antwort = verbindung.getresponse()
    if int(antwort.status)==200:                        #3
      inhalt = str(antwort.read())
      textstelle = findall('Ungef.+? Ergeb', inhalt)[0] #4
      zahl = findall(' .+ ', textstelle)[0]             #5
      ergebnis = 'Google findet' + zahl + 'Ergebnisse.' #6
    else: ergebnis = 'Keine Verbindung zu Google.'      #7
    verbindung.close()
    return  ergebnis

Sucher()



                    
