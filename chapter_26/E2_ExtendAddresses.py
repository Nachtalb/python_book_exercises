# ----------------------------------------------------
# Dateiname: email.py
# Modul mit einer XML-basierten Klasse Addresses
#
# Objektorientierte Programmierung mit Python (3. Aufl.)
# Kap. 26 
# Michael Weigend 19.11.2009
# ----------------------------------------------------

# email.py
from xml.dom import minidom


class Addresses(object):
    def __init__(self, path):
        self.doc = minidom.parse(path)

    def insertAddress(self, name, email):
        for p in self.doc.getElementsByTagName("person"):
            if p.getAttribute("name") == name:
                textNode = self.doc.createTextNode(email)
                elementNode = self.doc.createElement("email")
                elementNode.appendChild(textNode)
                p.appendChild(elementNode)
                return

    def deleteAddress(self, email):
        emails = self.doc.getElementsByTagName("email")
        for e in emails:
            if e.firstChild.data == email:
                p = e.parentNode
                p.removeChild(e)
                e.unlink()

    def save(self, path):
        f = open(path, 'w')
        f.write(self.doc.toxml())
        f.close()

    def __str__(self):
        return self.doc.toprettyxml()


if __name__ == "__main__":
    a = Addresses("gruppeattr.xml")
    a.deleteAddress("sabrina@maier.de")
    a.insertAddress("Tom Kahlenbaum",
                    "tom@media-objects.de")
    a.save("gruppeattr_1.xml")
    print(a)
