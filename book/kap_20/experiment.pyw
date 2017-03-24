# ----------------------------------------------------
# Dateiname:  experiment.pyw
# Experiment zu Prozessen
# Objektorientierte Programmierung mit Python
# Kap. 20
# Michael Weigend 15.10.2009
# ----------------------------------------------------

from time import *
from tkinter import *


class Zaehler(object):
    def __init__(self):
        self.f = Tk()
        self.zahl = StringVar()
        Label(self.f, textvariable=self.zahl).pack()  # 1
        Button(self.f, command=self.zaehlen,
               text=' Los! ').pack()
        self.f.mainloop()

    def zaehlen(self):
        for i in range(11):
            self.zahl.set(str(i))  # 2
            sleep(1)  # 3


z = Zaehler()
