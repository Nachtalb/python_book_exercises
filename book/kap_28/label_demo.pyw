#! /Python34/pythonw.exe

# ----------------------------------------------------
# Dateiname:  label_demo.pyw 
# Ein Anwednungsfenster mit Text und Bild.
#
# Python 3, 6. Auflage, mitp 2016
# Kap. 28
# Michael Weigend 22.09.2016
# ----------------------------------------------------

import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *


class PhotoView(QWidget):
    def __init__(self):
        super().__init__()
        picture = QPixmap("skytree.png")
        self.label1 = QLabel()
        self.label1.setPixmap(picture)
        self.label2 = QLabel("Der Skytree in Tokio, Japan")
        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.label2)
        self.setLayout(vbox)
        self.show()


app = QApplication(sys.argv)
pv = PhotoView()
sys.exit(app.exec_())
