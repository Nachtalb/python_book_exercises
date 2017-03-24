# ----------------------------------------------------
# Dateiname: intergruss.pyw
#
# Objektorientierte Programmierung mit Python
# Kap. 15  
# Michael Weigend 8. 10. 09
# ----------------------------------------------------

from tkinter import *

fenster = Tk()
gruss = StringVar()  # 1
engl = Radiobutton(fenster, text='englisch    ',
                   value='Hello', variable=gruss)  # 2
franz = Radiobutton(fenster, text='französisch',
                    value='Bonjour', variable=gruss)
deutsch = Radiobutton(fenster, text='deutsch    ',
                      value='Guten Tag', variable=gruss,
                      )
ausgabe = Label(fenster, textvariable=gruss,
                font=('Arial', 20), width=10)
deutsch.select()  # 3
ausgabe.pack()
franz.pack()
engl.pack()
deutsch.pack()
fenster.mainloop()
