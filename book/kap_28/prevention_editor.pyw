#! /Python34/pythonw.exe

#----------------------------------------------------
# Dateiname:  prevention_editor.pyw
# Editor für P-Sätze (Vorbeugung bei gefährlichen Stoffen)
#
# Python 3, 6. Auflage, mitp 2016
# Kap. 28
# Michael Weigend 22.09.2016
#----------------------------------------------------

# 
import sys
from PyQt5.QtWidgets import *

P = {"P201": "Vor Gebrauch besondere Anweisungen einholen.",
     "P202": "Vor Gebrauch alle Sicherheitshinweise lesen und verstehen.",
     "P210": "Von Hitze, heißen Oberflächen, Funken, offenen Flammen sowie " \
             + "anderen Zündquellenarten fernhalten. Nicht rauchen."}



class Editor(QWidget):
    def __init__(self):
        super().__init__()

        # Widgets
        self.text = QTextEdit()
        self.text.setText("<h1>Prävention</h1>")
        self.combo = QComboBox()
        self.combo.addItem("P201")
        self.combo.addItem("P202")
        self.combo.addItem("P210")
                             
        # Layout
        vBox = QVBoxLayout()
        self.setLayout(vBox)
        vBox.addWidget(self.text)
        vBox.addWidget(self.combo)
        self.show()

        self.combo.activated[str].connect(self.addText)
        
    def addText (self, item):
        self.text.append(P[item])

app = QApplication(sys.argv)
order = Editor()
sys.exit(app.exec_())
