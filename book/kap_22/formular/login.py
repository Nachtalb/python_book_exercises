#! c:/Python31/python.exe                               #1

#----------------------------------------------------
# Dateiname:  login.py 
# CGI-Skript, das Formular mit Login-Name und Passwort
# bearbeitet
#
# Objektorientierte Programmierung mit Python
# Kap. 22
# Michael Weigend 19. 10. 09
#----------------------------------------------------
                           
import cgi, cgitb
cgitb.enable()

form = cgi.FieldStorage()                               #2
vorname = form.getvalue('vorname')                      #3
name = form.getvalue('name')
print('Content-type: text/html; charset=utf-8')         #4
print()                                                 #5
print('<html>')                                         #6
print('<head><title> Login-Seite </title></head>')     
print('<body>')
print('<h3>Herzlich willkommen,',
      vorname, name,'!</h3>')
print('</body>')
print('</html>')













                    
