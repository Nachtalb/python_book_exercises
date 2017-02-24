#----------------------------------------------------
# Dateiname: vokabelsprecher.py
# Buchstabiertrainer, der englische Worte vorliest
#
# Python 3, 6. Auflage, mitp 2016
# Kap. 13
# Michael Weigend 22.08.2016
#----------------------------------------------------
# vokabelsprecher.py

import win32com.client
import random

class Vokabelgenerator(object):
    """ Aus einer Textdatei wird eine Vokabelliste generiert."""
    def __init__(self, datei):
        f = open(datei,'r')                           
        text = f.read()
        liste = text.split()                          #1
        self.__vokabeln = []                          #2
        for wort in liste:                            #3                   
            if wort.isalpha()and  len(wort) > 3:
             self.__vokabeln.append(wort.lower())
    
    def getVokabel(self):
          """ Liefert zufällige Vokabel"""
          return self.__vokabeln[random.randint(1,
                              len(self.__vokabeln))]

# Hauptprogramm
speaker = win32com.client.Dispatch("SAPI.SpVoice")    
speaker.Voice = speaker.GetVoices().Item(1)            #4
vokabeln = Vokabelgenerator('/python35/README.txt')
punkte = 0
fehler = 0
print ('Listen to the words and spell them.')
speaker.Speak('Listen to the words and spell them.')   #5  
for i in range(5):
     wort = vokabeln.getVokabel()
     speaker.Speak(wort)
     eingabe = input('Spell the word: ')
     if eingabe.lower() == wort:
           speaker.Speak('Correct.')
           punkte += 1
     else:
           speaker.Speak('Sorry, not correct')
           print ('The correct word is:', wort)
           fehler += 1
text = "You've got {} points".format(punkte)      #6
text += " and you've made {} mistakes. ".format(fehler)
text += "Good bye."
print(text)
speaker.Speak(text)

input("Press <ENTER>")
