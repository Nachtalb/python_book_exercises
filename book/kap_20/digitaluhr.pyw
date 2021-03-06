# ----------------------------------------------------
# Dateiname:  digitaluhr.pyw
# Objektorientierte Programmierung mit Python
# Kap. 20
# Michael Weigend 10. 10. 09
# ----------------------------------------------------

import _thread
from time import *
from tkinter import *


class Uhr(object):
    def __init__(self):
        self.fenster = Tk()
        self.zeit = StringVar()  # 1
        self.anzeige = Label(self.fenster,
                             textvariable=self.zeit,
                             font=("Arial", "20"))  # 2
        self.anzeige.pack()
        _thread.start_new_thread(self.aktualisieren, ())  # 3
        self.fenster.mainloop()

    def aktualisieren(self):
        while True:
            self.zeit.set(strftime("%X"))  # 4
            sleep(1)  # 5


uhr = Uhr()
