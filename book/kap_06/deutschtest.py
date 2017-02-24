# ---------------------------------------------------
# Dateiname: deutschtest.py
# Analyse der Vorkommenshaeufigkeit von Buchstaben
# in einem Text
# Objektorientierte Programmierung mit Python 3
# Kap. 6 
# Michael Weigend 1. 10. 09
#----------------------------------------------------
def deutsch (s):
    def h(text, buchstabe):
        text.upper()                            #1
        anzahl = text.count(buchstabe)          #2
        relativeHaeufigkeit = float(anzahl)*100/len(text)
        return relativeHaeufigkeit   
        # Ende def h 

    if (4<h(s,"a")<8) and (13<h(s,"e")<20) and (h(s,"y")<1):                                   #3
        return True
    else:
        return False
    # Ende def deutsch

text = input("Text: ")

if deutsch(text):
    print ("vermutlich deutsch")
else:
    print ("vermutlich nicht deutsch") 

