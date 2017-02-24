#----------------------------------------------------
# Dateiname: sehtest.pyw
#
# Objektorientierte Programmierung mit Python
# Kap. 15  
# Michael Weigend 2.6.06
#----------------------------------------------------
from tkinter import *
from random import*

class Sehtest(object):
  def __init__(self):
    self.fenster = Tk()
    self.button = Button(self.fenster,text='neu!',
                         command=self.neu)            #1
    self.label = [
      Label(self.fenster, font=('Arial',40), width=6),
      Label(self.fenster, font=('Arial',20), width=6),
      Label(self.fenster, font=('Arial',10), width=6)]#2
    self.neu()
    for l in self.label: l.pack()                     #3
    self.button.pack(pady=10)       
    self.fenster.mainloop()  

  def neu(self):
    a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for l in self.label:
      zeichen = choice(a)+' '+choice(a)+' '+choice(a) #4
      l.config(text=zeichen)                          #5

sehtest=Sehtest()
 



