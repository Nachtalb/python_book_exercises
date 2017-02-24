#----------------------------------------------------
# Dateiname: schalter.pyw
#
# Objektorientierte Programmierung mit Python
# Kap. 15  Lösung 1
# Michael Weigend 2.10.09
#----------------------------------------------------
 
from tkinter import *
class Schalter(object):
    def __init__(self):
        self.fenster = Tk()
        self.label = Label(self.fenster,
                      width=20, height=5, bg='black')
        self.button = Button(self.fenster, text='0 / I',
                        command=self.schalten)        #1
        self.label.pack()
        self.button.pack(pady=5)
        self.ein = 0
        self.fenster.mainloop()                     

    def schalten(self):                               #2
      if self.ein: 
        self.label.config(bg='black', fg='white',
                          text='Licht aus') 
        self.ein = 0
      else:
        self.label.config(bg='white',fg='black',
                          text='Licht an') 
        self.ein = 1

schalter = Schalter()                                 



 



