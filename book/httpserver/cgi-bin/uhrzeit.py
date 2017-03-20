#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

#----------------------------------------------------
# Dateiname:  uhrzeit.py 
# CGI-Skript, das html-Seite mit aktueller Uhrzeit ausgibt
#
# Python 3, 6. Auflage, mitp 2016
# Kap. 22
# Michael Weigend 22.08.2016
#----------------------------------------------------
SCHABLONE = """Content-type: text/html; char-set=utf-8

<html>
  <body>
    <h2>Die aktuelle Uhrzeit </h2>
      Es ist {} Uhr und {} {}.
  </body>
</html>"""         #1
    
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
