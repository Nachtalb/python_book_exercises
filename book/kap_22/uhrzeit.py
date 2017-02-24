#!/Python31/python.exe

#----------------------------------------------------
# Dateiname:  uhrzeit.py 
# CGI-Skript, das html-Seite mit aktueller Uhrzeit ausgibt
#
# Objektorientierte Programmierung mit Python
# Kap. 22
# Michael Weigend 17. 10. 09
#----------------------------------------------------
SCHABLONE = """Content-type: text/html; char-set=utf-8

<html>
  <body>
    <h2>Die aktuelle Uhrzeit </h2>
      Es ist {} Uhr und {} {}.
  </body>
</html>""" #1
    
import cgitb
cgitb.enable()
from time import localtime
zeit = localtime()
h = zeit[3]
m = zeit[4]
if m == 1:
    m_text = "Minute"
else:
    m_text = "Minuten"

print(SCHABLONE.format(h, m, m_text))
