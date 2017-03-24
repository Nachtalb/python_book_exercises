#! /Python34/python.exe

# ----------------------------------------------------
# Dateiname:  hello_qt.pyw 
# Erszeugt ein Fenster mit Titel "Hallo Qt"
#
# Python 3, 6. Auflage, mitp 2016
# Kap. 28
# Michael Weigend 22.09.2016
# ----------------------------------------------------

import sys

from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
w = QWidget()
w.resize(250, 100)
w.setWindowTitle("Hallo Qt")
w.show()
sys.exit(app.exec_())
