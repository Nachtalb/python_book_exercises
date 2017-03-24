#! /Python31/python.exe                               

# ----------------------------------------------------
# Dateiname:  chat1.py 
# CGI-Skript fuer einen Chat-Room mit erweiterten Moeglichkeiten.
# Teilnehmer koennen fluestern, schreien oder normal reden.
# 
# Objektorientierte Programmierung mit Python
# Kap. 22 Loesung 1
# Michael Weigend 21. 10. 09
# ----------------------------------------------------

import cgi
import cgitb

cgitb.enable()

http_SCHABLONE = '''Content-Type: text/html

<html>
<head><title>Python-Chat</title></head>
<body><h1>Python-Chat</h1>
{} <hr>
<form action="http://localhost:8000/cgi-bin/chat1.py" method="POST">
<input type="hidden" name="name" value="{}">
Ich sage:&nbsp;
<input type="Text" name="beitrag" size="40" maxlength="40">
<input type="Submit"  value="OK"><br><br>
<input type="Radio" name="typ" value="normal" 
checked="checked"> normal &nbsp
<input type="Radio" name="typ" value="schreien"> 
schreiend &nbsp
<input type="Radio" name="typ" value="fluestern"> fl&uuml;sternd
</form></body></html>'''

PATH = 'chat/dialog.txt'


class Dialog(object):
    def __init__(self, datei):
        self.datei = datei
        try:
            f = open(datei, 'r')
            self.textzeilen = f.readlines()
            f.close()
        except:
            self.textzeilen = []
            f = open(datei, 'w')
            f.close()

    def aktualisiere(self, name, beitrag):
        # Neuen Beitrag in Dialog einfuegen
        if len(self.textzeilen) > 10:
            self.textzeilen = self.textzeilen[-10:]
        neueZeile = name + ': ' + beitrag + '<br>\n'
        self.textzeilen.append(neueZeile)
        f = open(self.datei, 'w')
        for z in self.textzeilen:
            f.write(z)
        f.close()

    def __str__(self):
        # liefert Darstellung des Dialogs als HTML-Text
        dialog = ''
        for z in self.textzeilen:
            dialog += z
        return dialog


class Chatraum:
    def __init__(self):
        self.form = cgi.FieldStorage()
        self.dialog = Dialog(PATH)
        self.beitrag = self.form.getvalue('beitrag')
        self.name = self.form.getvalue('name')
        self.typ = self.form.getvalue('typ', 'normal')  # 1
        if str(self.beitrag):
            if self.typ == 'fluestern':  # 2
                text = ' <font size="-1" color=#9F9F9F>{} </font>'
            elif self.typ == 'schreien':
                text = ' <font size="+2" color=#FF0000>{} </font>'
            else:
                text = ' {}'
            text = text.format(self.beitrag)  # 3
            self.dialog.aktualisiere(self.name, text)

    def __str__(self):
        return http_SCHABLONE.format(self.dialog,
                                     self.name)  # 4


print(Chatraum())
