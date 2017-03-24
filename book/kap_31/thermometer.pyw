#! /Python34/python.exe

# ----------------------------------------------------
# Dateiname:  thermometer.py
# Von einem digitalen Messgerät, dass den Widerstand
# eines Pt-100-Thermometers misst, wird die Display-Anzeige
# (natürliche Zahl) übernommen und daraus die Temperatur berechnet
# und angezeigt.
#
# Python 3, 6. Auflage, mitp 2016
# Kap. 31.2
# Michael Weigend 22.09.2016
# ----------------------------------------------------

from _thread import start_new_thread
from tkinter import Tk, Label

from dmm import get_digits


def show():
    global label
    n = get_digits()
    t = (n / 10 - 100) / 0.39
    label.config(text='%.1f°C' % temp)
    label.after(1000, show)


window = Tk()
label = Label(master=window, width=8,
              font=('Courier', 150))
label.pack()
start_new_thread(show, ())
window.mainloop()
