# ----------------------------------------------------
# Dateiname: labelgroesse.pyw
#
# Objektorientierte Programmierung mit Python
# Kap. 15  
# Michael Weigend 8. 10. 09
# ----------------------------------------------------
from tkinter import *

fenster = Tk()
label1 = Label(fenster, text='gro\xdf', font=('Arial', 40),
               relief='groove', bg='yellow')
label2 = Label(fenster, text='klein', font=('Arial', 10),
               relief='groove', bg='yellow')
label1.pack()
label2.pack()
fenster.mainloop()
