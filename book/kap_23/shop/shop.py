#! c:\python23\python.exe                               #1

# ----------------------------------------------------
# Dateiname:  shop.py 
# CGI-Skript, das Teil eines online-Shops ist.
# Folgende Variablen eines HTML-Formulars werden verarbeitet:
# email: E-Mail-Adresse des Kunden
# artikel: Liste der ausgewaehlten Artikel.
# Das Skript sendet eine Antwortseite und zwei E-Mails mit
# einer Auftragsbestaetigung.
# 
# Objektorientierte Programmierung mit Python
# Kap. 23 Loesung 2
# Michael Weigend 2.6.06
# ----------------------------------------------------

import cgi
import cgitb
import poplib
import smtplib

cgitb.enable()
message = ''''From: %s
To: %s
Subject: Bestellung Online-Shop
MIME-Version: 1.0
Content-Type: text/html
Content-Transfer-Encoding: quoted-printable

<html><body>
<h3>Vielen Dank f&uuml;r Ihre Bestellung!</h3>
%s
</body></html>'''  # 1

antwort1 = '''Content-Type: text/html

<html><body>
<h3>Vielen Dank f&uuml;r Ihre Bestellung!</h3>
Sie erhalten eine Mail mit einer
Auftragsbest&auml;tigung.</body></html>'''  # 2

antwort2 = '''Content-Type: text/html

<html><body>
<h3>Fehler</h3>
Ihre Bestellung konnte nicht bearbeitet werden.
</body></html>'''


class SMTPClient(object):  # 3
    def __init__(self):
        self.fromaddr = 'ich@shoeshop.de'
        self.server = 'post.webmailer.de'

    def sende(self, toaddr, bestellung):
        self.mailcheck()
        client = smtplib.SMTP(self.server)
        msg = message % (self.fromaddr, toaddr, bestellung)
        client.sendmail(self.fromaddr, toaddr, msg)
        client.quit()

    def mailcheck(self):
        client = poplib.POP3(self.server)
        client.user('ich@shoeshop.de')
        client.pass_('meinpasswort')
        client.quit()


class Shop(object):  # 4
    def __init__(self):
        self.artikel = {'buerste': ('Schuhb&uuml;rste', '4.50'),
                        'schwarz': ('Schuhcreme (schwarz)', '3.00'),
                        'farblos': ('Schuhcreme (farblos)', '3.00')}
        self.form = cgi.FieldStorage()
        self.smtpclient = SMTPClient()
        self.artikelliste = self.form.getlist('artikel')  # vom Kunden gewaehlte Artikel
        self.kunde = self.form.getvalue('email')
        self.sachbearbeiter = 'mw@media-objects.de'
        self.bestellung = self.macheBestellung()
        if self.bestellung:
            self.smtpclient.sende(self.kunde, self.bestellung)
            self.smtpclient.sende(self.sachbearbeiter, self.bestellung)

    def macheBestellung(self):  # 5
        text = 'E-Mail-Adresse des Kunden: ' + self.kunde + '<br><br>'
        text += 'Bestellte Artikel:<br>'
        summe = 0
        for art in self.artikelliste:
            text += self.artikel[art][0]
            text += ' ' + self.artikel[art][1] + ' EUR<br>'
            summe += float(self.artikel[art][1])
        text += 'Transport und Verpackung: 5 EUR<br>'
        text += 'Summe: ' + str(summe + 5) + ' EUR'
        if self.kunde and self.artikelliste:
            return text
        else:
            return ''

    def __str__(self):
        if self.bestellung:
            return antwort1
        else:
            return antwort2


print
Shop()
