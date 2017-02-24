#----------------------------------------------------
# Dateiname: email1.pyw
# Einfacher E-Mail-Client, der ueber SMTP Mails verschickt.
# Passwort, Mail-Server und eigene E-Mail-Adresse muessen
# noch angepasst werden.
#
# Objektorientierte Programmierung mit Python
# Kap. 23
# Michael Weigend 23.10.09
#----------------------------------------------------

import smtplib
from tkinter import *

SCHABLONE = """From: {}
To: {}
Subject: {}
MIME-Version: 1.0
Content-Type: text/html
Content-Transfer-Encoding: quoted-printable

{}
"""                                                       #1

class SMTPClient:  
  def __init__ (self):
    fenster = Tk()
    fenster.title("SMTP-Client Nr. 1")
    Label(fenster, text="Adresse: ").grid(row=0, column=0)  
    self.adresse = Entry(fenster, width=40)
    self.adresse.grid(row=0, column=1, pady=5) 
    Label(fenster, text="Betrifft: ").grid(row=1, column=0)   
    self.betreff = Entry(fenster, width=40)
    self.betreff.grid(row=1, column=1,pady=5) 
    self.text = Text(fenster,width= 40, height =10)   
    self.text.grid(row=3, column=1, pady=5, padx=5)
    self.absenden = Button(fenster, text="Abschicken",
                       command=self.abschicken)
    self.absenden.grid(row=3, column=0,padx=5)
    self.absender = 'ich@meinedomain.de'
    fenster.mainloop()

  def abschicken(self):
    server = smtplib.SMTP('smtp.meinprovider.de')          #2
    server.login("ich@meinedomain.de", "passwort")
    server.set_debuglevel(1)                               #4
    inhalt = self.text.get('1.0', END)
    nachricht = SCHABLONE.format(self.absender,
                 self.adresse.get(),
                 self.betreff.get(),
                 inhalt)                                   #5
    server.sendmail(self.absender,
                         [self.adresse.get()], nachricht)  #6
    server.quit()                                          #7

SMTPClient()





                    
