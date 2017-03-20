#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

#----------------------------------------------------
# Dateiname:  abstimmung.py 
# Service-Skript, das XML-Dokument verarbeitet
#
# Python 3, 6. Auflage, mitp 2016
# Kap. 
# Michael Weigend 22.08.2016
#----------------------------------------------------
import cgi, os, pickle, http.cookies, cgitb

# Globale Konstanten:
SEITE = """{}
Content-Type: text/html; 

<html>
  <head><title>Online-Abstimmung</title></head>
  <body><h1>Online-Abstimmung</h1>
    <h3> {} </h3>
    Hier ist das aktuelle Abstimmungsergebnis:<br>
    Frage: {} <br><br> {}
  </body>
</html>"""                                           #1

PFAD = "abstimmung/zaehler.txt"
ITEMS = ["Ja", "Nein"]
FRAGE = "Sind Studiengeb&uuml;hren an Unis sinnvoll?"

cgitb.enable()
class Zaehler (object):
  def __init__(self, datei,items):
    self.datei = datei
    try:        # vorhandene Datei laden
       f = open(datei,"rb")
       self.stimmen = pickle.load(f)
       f.close()
    except:     # neue Datei anlegen
       self.stimmen = {}
       for i in items:
           self.stimmen[i] = 0
       f = open(datei,"wb")
       pickle.dump(self.stimmen, f)
       f.close() 

  def votiere(self, item):
    # item erhält eine Stimme
    self.stimmen[item] += 1
    f = open(self.datei, "wb")
    pickle.dump(self.stimmen, f)
    f.close()

  def __str__(self):
    # liefert HTML-Text mit Abstimmungsergebnis
    ergebnis = ""
    for i in self.stimmen.keys():
      ergebnis += "<b>{}: </b>{} Stimmen<br>\n".format(
                                      i,self.stimmen[i])
    return ergebnis

class Abstimmung (object):
  def __init__(self):
    self.form = cgi.FieldStorage()
    self.zaehler = Zaehler(PFAD, ITEMS)
    self.meldung ="--"
    if not self.__schon_mal_abgestimmt():
       if "item" in self.form.keys():
          item = self.form.getvalue('item')
          self.zaehler.votiere(item)
          self.meldung = "Vielen Dank f&uuml;r Ihr Voting!"
    else:
        self.meldung = "Sorry, Sie haben bereits abgestimmt ..."

  def __schon_mal_abgestimmt(self):
    # liefert True, falls schon mal ab-
    # gestimmt wurde und sonst False 
    self.cookie = http.cookies.SimpleCookie()
    try:
          self.cookie.load(os.environ['HTTP_COOKIE'])
          return bool(self.cookie['abstimmung'])            
    except:
          self.cookie['abstimmung'] = True
          return False

  def __str__(self):
      return SEITE.format(self.cookie, self.meldung,
                           FRAGE, self.zaehler) 
      
print(Abstimmung())

















                    
