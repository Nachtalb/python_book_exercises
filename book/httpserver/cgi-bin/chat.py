#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3                              #1

#----------------------------------------------------
# Dateiname:  chat.py 
# CGI-Skript fuer einen einfachen Chat-Room.
# 
# Python 3, 6. Auflage, mitp 2016
# Kap. 22
# Michael Weigend 22.08.2016
#----------------------------------------------------
                           
HTTP_SCHABLONE = '''Content-Type: text/html

<html><head><title>Python-Chat</title></head>
  <body>
    <h1>Python-Chat</h1>
     {} <hr>
     <form action="http://localhost:8080/cgi-bin/chat.py" 
     method="POST">
       <input type="hidden" name="name" value="{}">
       Ich sage:&nbsp;
       <input type="Text" name="beitrag" size="40"
       maxlength="40">
       <input type="Submit"  value="OK">
     </form>
  </body>
</html>'''

PFAD = "chat/dialog.txt"

import cgi, cgitb
cgitb.enable()                                          #1

class Dialog:
  def __init__(self, datei):
    self.datei = datei
    try:                                                #2
      f = open(datei,'r')
      self.textzeilen = f.readlines()
      f.close()
    except:                                             #3
      self.textzeilen=[]
      f = open(datei, 'w')
      f.close()

  def aktualisiere(self, name, beitrag):  
    # Neuen Beitrag in Dialog einfügen
    if len(self.textzeilen)>10:                       #4                 
        self.textzeilen = self.textzeilen[-10:]
    neueZeile = name+': '+ beitrag+ '<br>\n'
    self.textzeilen.append (neueZeile)                #5
    f = open(self.datei,'w') 
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
    self.dialog = Dialog(PFAD)
    self.beitrag=self.form.getvalue('beitrag')        #6    
    self.name = self.form.getvalue('name')
    if self.beitrag:                                  #7
       self.dialog.aktualisiere(self.name, self.beitrag)

  def __str__(self):
     return HTTP_SCHABLONE.format(self.dialog,
                                 self.name)           #8
    
print(Chatraum())














                    
