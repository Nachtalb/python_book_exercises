# ----------------------------------------------------
# Dateiname:  zaehler.pyw
# Zaehler mit Methode, die in eigenem Thread laeft
# Objektorientierte Programmierung mit Python
# Kap. 20
# Michael Weigend 15.10.09
# ----------------------------------------------------

import _thread
from time import *
from tkinter import *


class Zaehler(object):
    def __init__(self):
        self.f = Tk()
        self.zahl = StringVar()
        Label(self.f, textvariable=self.zahl).pack()
        Button(self.f, command=self.zaehlenThread,
               text=' Los! ').pack()  # 1
        self.f.mainloop()

    def zaehlenThread(self):
        _thread.start_new_thread(self.zaehlen, ())  # 2

    def zaehlen(self):
        for i in range(11):
            self.zahl.set(str(i))
            sleep(1)


z = Zaehler()
