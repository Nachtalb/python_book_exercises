#----------------------------------------------------
# Dateiname: buchstabenregler.pyw
#
# Objektorientierte Programmierung mit Python
# Kap. 15  
# Michael Weigend 8. 10. 09
#----------------------------------------------------
 
from tkinter import *
class Buchstabenregler(object):
    def __init__ (self):
        self.fenster = Tk()
        self.label = Label(self.fenster, text='A',
                           font=('Arial', 4))
        self.scale = Scale(self.fenster, length='3c',
                           from_=4, to=60,
                           command=self.setzeGroesse)
        self.label.pack(side=LEFT)
        self.scale.pack(side=RIGHT)
        self.fenster.mainloop()

    def setzeGroesse(self, event):
        x=int(self.scale.get())
        self.label.config(font=('Arial', x))

b = Buchstabenregler()



 



