#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

#----------------------------------------------------
# Dateiname:  shop.py 
# CGI-Skript, das Teil eines online-Shops ist.
# Folgende Variablen eines HTML-Formulars werden verarbeitet:
# email: E-Mail-Adresse des Kunden
# artikel: Liste der ausgewaehlten Artikel.
# Das Skript sendet eine Antwortseite und zwei E-Mails mit
# einer Auftragsbestaetigung.
# 
# Python 3, 6. Auflage, mitp 2016
# Kap. 23 Lösung 2
# Michael Weigend 22.08.2016
#----------------------------------------------------
 
import cgi, cgitb, smtplib, poplib
cgitb.enable()

MESSAGE = '''From: {}
To: {}
Subject: Bestellung Online-Shop
MIME-Version: 1.0
Content-Type: text/html
Content-Transfer-Encoding: quoted-printable

<html><body>
<h3>Vielen Dank f&uuml;r Ihre Bestellung!</h3>
{}
</body></html>'''                                        #1

ANTWORT1 = '''Content-Type: text/html

<html><body>
<h3>Vielen Dank f&uuml;r Ihre Bestellung!</h3>
Sie erhalten eine Mail mit einer
Auftragsbest&auml;tigung.</body></html>'''               #2

ANTWORT2 = '''Content-Type: text/html

<html><body>
<h3>Fehler</h3>
Ihre Bestellung konnte nicht bearbeitet werden.
</body></html>'''

ABSENDER = 'ich@meinedomain.de'                          #3
PASSWORT = 'meinpasswort'
SERVER = 'smtp.meinprovider.de'

class Shop:                                              #4
  def __init__(self):
    self.artikel = {'buerste':('Schuhb&uuml;rste', '4.50'),
                  'schwarz':('Schuhcreme (schwarz)', '3.00'),
                  'farblos':('Schuhcreme (farblos)', '3.00')}
    self.form = cgi.FieldStorage()
    self.artikelliste = self.form.getvalue('artikel',[]) #5
    if type(self.artikelliste) != type([]):
      self.artikelliste = [self.artikelliste]            #6
    self.kunde = self.form.getvalue('email','')
    self.sachbearbeiter = 'mw@media-objects.de'   
    self.bestellung = self.macheBestellung()
    if self.bestellung:
      self.sende(self.kunde, self.bestellung)
      self.sende(self.sachbearbeiter, self.bestellung)

  def macheBestellung(self):                             #7
    text = 'E-Mail-Adresse des Kunden: ' + self.kunde +'<br><br>'
    text += 'Bestellte Artikel:<br>'
    summe = 0
    for art in self.artikelliste:
        text += self.artikel[art][0]
        text += ' ' + self.artikel[art][1] + ' EUR<br>'
        summe += float(self.artikel[art][1])
    text += 'Transport und Verpackung: 5 EUR<br>'
    text += 'Summe: ' + str(summe+5) + ' EUR'
    if self.kunde and self.artikelliste:
        return text
    else: return ''

  def sende (self, adressat, bestellung):
    #sende E-Mail
    server = smtplib.SMTP(SERVER)
    server.login(ABSENDER, PASSWORT)
    msg = MESSAGE.format(ABSENDER, 
                 adressat, bestellung)
    server.sendmail(ABSENDER, adressat, msg)
    server.quit()

  def __str__(self):
      if self.bestellung: return ANTWORT1
      else: return ANTWORT2

print(Shop())                                         
                                       

















                    
