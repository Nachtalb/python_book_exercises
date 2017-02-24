#----------------------------------------------------
# Dateiname:  photoviewer.pyw
# Bearbeitung eines Fotos
# Objektorientierte Programmierung mit Python
# Kap. 17 
# Michael Weigend 7.10.09
#----------------------------------------------------

from tkinter import filedialog, Label, Tk, Button, \
     PhotoImage, LEFT

DEFAULT_PATH = "bilder/strasse.gif"

class FotoViewer(object):  
  def __init__ (self):   
    self.__createWidgets()
    self.__layout()
    self.fenster.mainloop()
        
  def __createWidgets(self):
    self.fenster = Tk()
    self.bild = BitmapImage(file=DEFAULT_PATH)
    self.bildflaeche = Label(master=self.fenster,
                        image=self.bild)
    
    self.buttonLaden = Button(master=self.fenster,
                             text="Laden",
                             command=self.__laden)
    self.buttonNegativ = Button(master=self.fenster,
                             text="Negativ",
                             command=self.__invertieren)
  def __layout(self):
    self.bildflaeche.pack()
    self.buttonLaden.pack(side=LEFT)
    self.buttonNegativ.pack(side=LEFT)
        
  def __laden (self):    
    pfad = filedialog.askopenfilename()
    if pfad:    
        self.bild = PhotoImage(file=pfad)
        self.bildflaeche.config(image=self.bild)

  def __invertieren (self):    
    punkte = ((x,y) for x in range(self.bild.width())
                    for y in range(self.bild.height()))
    for x, y in punkte:
        rgb = self.bild.get(x, y)
        r, g, b = map(int, rgb.split())
        r = 255 - r
        g = 255 - g
        b = 255 - b
        rgb = "#{:02x}{:02x}{:02x}".format(r, g, b)
        self.bild.put((rgb,), (x,y))
               
f = FotoViewer()
