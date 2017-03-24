# waehrungen.pyw
from tkinter import *


class Waehrungsrechner:
    kurs = {'USD': 1.4699,
            'GBP': 0.9206}  # 1

    def __init__(self):
        self.fenster = Tk()
        self.fenster.title('W\xe4hrungen')
        self.euros = DoubleVar()  # 2
        self.waehrung = StringVar()  # 3
        self.ausgabe = StringVar()

        Label(self.fenster,
              text='Geben Sie einen Betrag in Euro ein\n' + \
                   'und wählen Sie eine Währung',
              width=30, height=3,
              font=('Arial', 12), fg='blue').pack()  # 4
        Entry(self.fenster, textvariable=self.euros).pack()
        self.us = Radiobutton(self.fenster, text='US-Dollar',
                              value='USD',
                              variable=self.waehrung)
        self.us.pack()
        Radiobutton(self.fenster, text='Britisches Pfund',
                    value='GBP',
                    variable=self.waehrung).pack()
        Button(self.fenster, text='Rechnung',
               command=self.rechnung).pack()
        Label(self.fenster, font=('Arial', 12),
              width=30, height=2,
              textvariable=self.ausgabe).pack()
        self.us.select()
        self.fenster.mainloop()

    def rechnung(self):
        euros = self.euros.get()
        waehrung = self.waehrung.get()
        ergebnis = str(euros * self.kurs[waehrung])
        self.ausgabe.set(ergebnis + ' ' + waehrung)  # 5


w = Waehrungsrechner()
