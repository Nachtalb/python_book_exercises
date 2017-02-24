#----------------------------------------------------
# Dateiname: ozon.pyw
# Recherchiert auf der Website des Landesumweltamtes
# nach der aktuellen Ozon-Konzentration am angegebenen Ort.
#
# Python 3, 6. Auflage, mitp 2016
# Kap. 23 Lösung 1
# Michael Weigend 24.08.2016
#----------------------------------------------------

from http.client import HTTPConnection
from re import compile, findall
from tkinter import *
SCHABLONE = '''Die Ozonkonzentration der Luft
am Standort {} beträgt 
{} Mikrogramm pro Kubikmeter
(gemessen in Bodennähe).'''                           #1

SERVER = "www.lanuv.nrw.de"
PFAD = "/fileadmin/lanuv/luft/immissionen/aktluftqual/eu_o3_akt"

class Ozoncheck:                                      #2
  def __init__ (self, ort):
    try:
      self.ort = ort
      verbindung = HTTPConnection(SERVER)             #3
      verbindung.request('GET', PFAD)   
      antwort = verbindung.getresponse()
      self.htmltext = str(antwort.read())
      verbindung.close()
      self.ergebnis = self.auswerten()
    except:
      self.ergebnis = ''

  def auswerten(self):
     re1 = compile(self.ort + '.*?</tr>')             #5
     re2 = compile('<td .+?</td></tr>')
     re3 = compile('\d+')
     zeile = re1.findall(self.htmltext)[0]
     letztesStueck = re2.findall(zeile)[0]
     return re3.findall(letztesStueck)[0]

  def __str__(self):
      return self.ergebnis

class Benutzungsoberflaeche:
  def __init__(self):
    meinfont = ('Arial', 10)
    self.fenster = Tk()
    self.ort = StringVar()
    self.ergebnis = StringVar()
    self.fenster.title('Ozon-Check')
    self.frame = Frame(self.fenster)
    Label(self.frame, font=meinfont,
          text='Ort: ').pack(side=LEFT)
    Entry(self.frame, font=meinfont,
          textvariable=self.ort).pack(side=LEFT)
    Button(self.frame, font=meinfont, text=' Ozon ',
           command=self.ozoncheck).pack(side=LEFT, padx=5)
    self.frame.pack(padx=5, pady=5)
    Label(self.fenster, font=meinfont,height=4,
          textvariable=self.ergebnis).pack()
    self.fenster.mainloop()

  def ozoncheck(self):                                #6
    zahl = str(Ozoncheck(self.ort.get()))
    if zahl:
      self.ergebnis.set(SCHABLONE.format(self.ort.get(), zahl))
    else:
      self.ergebnis.set(
      'Ihre Anfrage konnte nicht \n bearbeitet werden.')
                       
Benutzungsoberflaeche()
