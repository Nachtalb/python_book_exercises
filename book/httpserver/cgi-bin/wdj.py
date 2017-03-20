#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
#----------------------------------------------------
# Dateiname:  wdj.py 
# Modul mit Klasse Responder zur Wahl des "Wortes des Jahres"
# 
# Python 3, 6. Auflage, mitp 2016
# Kap. 22
# Michael Weigend 22.08.2016
#----------------------------------------------------

import cgi, cgitb
cgitb.enable()                                        #1
from ranking import *
                                                      #2
RESPONSE = """Content-Type: text/html

<html>
<meta http-equiv="Content-Type" content="charset=utf-8" />
<head><title>Wort des Jahres</title></head>
<body >
<font face="VERDANA,ARIAL,HELVETICA">
<h2> Danke f&uuml;r Ihr Votum!</h2>
Hier sind die bisherigen Top Ten: <br>
{} 
Ihr Vorschlag {} steht auf Platz {}.<br>
</font>
</body>
</html>"""                                       

PATH = "wort_des_jahres/words.txt"

class Responder(object):
  def __init__ (self, datafile):
    form = cgi.FieldStorage()
    self.word = form.getvalue("word")            
    self.ranking = Ranking(datafile)                  #3
    self.ranking.add(self.word)                       #4
    self.ranking.save()                           

  def respond(self):                                  #5
      topFive = self.ranking.getTop(5)                #6
      rank = self.ranking.getRank(self.word)          #7
      print(RESPONSE.format(topFive, self.word, rank))#8

r = Responder(PATH)
r.respond()

