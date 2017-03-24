# ----------------------------------------------------
# Dateiname: lesetest.pyw
#
# Objektorientierte Programmierung mit Python
# Kap. 15  
# Michael Weigend 2.10.09
# ----------------------------------------------------
from random import *
from tkinter import *


class Lesetest(object):
    def __init__(self):
        self.fenster = Tk()
        self.text = StringVar()  # 1
        self.button = Button(self.fenster, text='neu!',
                             command=self.neu)
        self.label = [
            Label(self.fenster, font=('Comic Sans MS', 20),
                  width=22, textvariable=self.text),
            Label(self.fenster, font=('Script', 20),
                  width=22, textvariable=self.text),
            Label(self.fenster, font=('Palatino', 20),
                  width=22, textvariable=self.text)]  # 2
        self.neu()
        for l in self.label: l.pack()
        self.button.pack(pady=10)
        self.fenster.mainloop()

    def neu(self):
        liste = ['Wahrnehmen mit den Augen',
                 'Was ist besser lesbar?',
                 'Gut erkennbare Worte']
        self.text.set(choice(liste))  # 3


lesetest = Lesetest()
