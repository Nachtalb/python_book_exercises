#! /Python34/pythonw.exe

# ----------------------------------------------------
# Dateiname:  worldmap.pyw
# Auf einer Weltkarte wird ein gesuchter Ort angezeigt
#
# Python 3, 6. Auflage, mitp 2016
# Kap. 29
# Michael Weigend 22.09.2016
# ----------------------------------------------------

import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from geopy.geocoders import Nominatim

MAPFILE = "world_map.png"


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.createWidgets()
        self.show()

    def createWidgets(self):
        self.setWindowTitle("Weltkarte")
        self.label = QLabel(self)
        self.pixmap = QPixmap(MAPFILE)
        self.label.setPixmap(self.pixmap)
        self.label.adjustSize()
        self.adjustSize()
        self.target = QLabel(self)
        self.target.setPixmap(QPixmap("target.gif"))
        self.button = QPushButton("Ort suchen", self)
        self.button.clicked.connect(self.search)
        self.button.move(20, 200)
        self.target.hide()

    def search(self):
        town, ok = QInputDialog.getText(self, "Suche Ort",
                                        "Bitte geben Sie eine Stadt ein")
        self.target.hide()
        if ok:
            geolocator = Nominatim()
            location = geolocator.geocode(town, timeout=10)
            k = self.pixmap.width() / 360
            x = (location.longitude + 180) * k
            y = (-location.latitude + 90) * k
            self.target.move(x, y)
            self.target.show()


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
