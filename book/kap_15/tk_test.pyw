# ----------------------------------------------------
# Dateiname: tk_test.pyw
# Einführungsbeispiel für ein Programm mit GUI
#
# Python 3, 6. Auflage, mitp 2016
# Kap. 15
# Michael Weigend 20.08.2016
# ----------------------------------------------------
def gruessen():
    fenster.label.config(text='Hallo!')  # 1


from tkinter import *

fenster = Tk()
fenster.label = Label(fenster, text='Begr\xfc\xdfung')
fenster.label.pack()
fenster.button = Button(master=fenster,
                        text='Sage Hallo',
                        command=gruessen)  # 2
fenster.button.pack()  # 3
fenster.mainloop()
