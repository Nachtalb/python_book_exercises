#----------------------------------------------------
# Dateiname:  bilder.pyw
# Bildergalerie mit vor-Schaltflaeche
# Python 3, 6. Auflage, mitp 2016
# Kap. 17 Lösung 1
# Michael Weigend 7.08.2016
#----------------------------------------------------

DATEN = [('Festung von Bodrum','bilder/bodrum.png'),
  ('Im Reallabor des Futuriums (Berlin)', 'bilder/futurium.png')]

from tkinter import *
from PIL import Image, ImageTk

class Galerie:
  def __init__(self, daten):
        self.daten = daten
        self.nr = 0

  def nächstes(self):
         self.nr = (self.nr +1) % len(self.daten) 
         return self.daten[self.nr]
 
class Projektor:
  def __init__(self):
    self.fenster = Tk()
    self.galerie =  Galerie(DATEN)                    #1
    self.LabelBild = Label(self.fenster)       #2
    self.LabelBild.pack()
    self.LabelText = Label(self.fenster, width=25,
                      font=('Arial', 10))        #3
    self.LabelText.pack()
    icon=PhotoImage(file='bilder/weiter.gif')         #4
    Button(self.fenster,image=icon,
        command=self.weiter).pack()
    self.weiter()
    self.fenster.mainloop()

  def weiter(self):
      text, bilddatei = self.galerie.nächstes()           #5
      img = Image.open(bilddatei)
      self.imgTk = ImageTk.PhotoImage(img)
      self.LabelBild.config(image=self.imgTk)
      self.LabelText.config(text=text)

p = Projektor()



                    
