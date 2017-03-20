#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

#----------------------------------------------------
# Dateiname:  login.py 
# CGI-Skript, das Formular mit Login-Name und Passwort
# bearbeitet
#
# Python 3, 6. Auflage, mitp 2016
# Kap. 22
# Michael Weigend 22.08.2016
#----------------------------------------------------
                           
import cgi, cgitb
cgitb.enable()

HTML = {ord("ä"): "&auml;", ord("ö"): "&ouml;",
        ord("ü"): "&uuml;", ord("Ä"): "&Auml;",
        ord("Ö"): "&Ouml;", ord("Ü"): "&Uuml;",
        ord("ß"): "&szlig;"}                            #1

form = cgi.FieldStorage()                               
vorname = form.getvalue('vorname', "")                  
name = form.getvalue('name', "")

print('Content-type: text/html; charset=utf-8') 
print()                                                 
print('<html>')
print('<head><title> Login-Seite </title></head>')     
print('<body>')
print('<h3>Herzlich willkommen,',
      vorname.translate(HTML),
      name.translate(HTML),'!</h3>')                   #2
print('</body>')
print('</html>')













                    
