#----------------------------------------------------
# Dateiname: email.py
# Modul mit einer XML-basierten Klasse Addresses
#
# Objektorientierte Programmierung mit Python (3. Aufl.)
# Kap. 26 
# Michael Weigend 19.11.2009
#----------------------------------------------------

# email.py
from xml.dom import minidom

class Addresses(object):

  def __init__(self, path):
    self.doc = minidom.parse(path)                    #1

  def insertAddress (self, name, email):
    # Fügt neue Email-Adresse email für Person name ein
    for p in self.doc.getElementsByTagName("person"): #2
      if p.getAttribute("name") == name:
        textNode = self.doc.createTextNode(email)     #3
        elementNode = self.doc.createElement("email")
        elementNode.appendChild(textNode)             #4
        p.appendChild(elementNode)
        return

  def deleteAddress (self, email):
    # Löscht erstes Vorkommen der E-Mail-Adresse email
    emails = self.doc.getElementsByTagName("email")   #5
    for e in emails:
        if e.firstChild.data == email:
            p = e.parentNode                          #6
            p.removeChild(e)
            e.unlink()                                #7

  def save (self, path):
    f = open(path, 'w')                               #8
    f.write(self.doc.toxml())
    f.close()

  def __str__(self):                                  #9
    return self.doc.toprettyxml()

# Test
if __name__ == "__main__":
    a = Addresses("gruppeattr.xml")                  #10
    a.deleteAddress("sabrina@maier.de")
    a.insertAddress("Tom Kahlenbaum",
                    "tom@media-objects.de")
    a.save("gruppeattr_1.xml")
    print(a)




