#! /Python34/pythonw.exe

#----------------------------------------------------
# Dateiname:  browser_message.pyw
# Browser mit Icon auf einer Schaltfläche und Messagebox
#
# Python 3, 6. Auflage, mitp 2016
# Kap. 28
# Michael Weigend 22.09.2016
#----------------------------------------------------
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKit import *
from PyQt5.QtWebKitWidgets import *

class Browser(QWidget):
    def __init__(self, parent=None):
        super(Browser, self).__init__(parent)
        self.createWidgets()                          #1
        self.createLayout()
        self.createConnections()
        self.show()

    def closeEvent(self, event):   
        reply = QMessageBox.question(self, "Achtung",
            "Möchten Sie wirklich die Anwendung schießen?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()        

    def search(self):
        # Zeige Webseite
        address = str(self.addressBar.text())         #2
        if address:                                   #3
            if "://" not in address:
                address = "http://" + address         #4
            url = QUrl(address)                       #5
            self.webView.load(url)                    #6
            

    def createWidgets(self):
        self.setWindowTitle("Welt-Browser")           #7
        self.setWindowIcon(QIcon("welt.png"))         #8
        self.addressBar = QLineEdit(self)                 #9
        self.addressBar.setToolTip("<b>URL</b> eingeben")
        self.searchButton = QPushButton("Suchen", self)     #10
        self.searchButton.setIcon(QIcon("fernrohr_1.png"))
        self.searchButton.setIconSize(QSize(40,15))      
        self.webView = QWebView(self)                     #11

    def createLayout(self):
        hbl = QHBoxLayout()                           #11
        hbl.addWidget(self.addressBar)                #12
        hbl.addWidget(self.searchButton)
        vbl = QVBoxLayout()
        vbl.addLayout(hbl)
        vbl.addWidget(self.webView)
        self.setLayout(vbl)

    def createConnections(self):
        self.addressBar.returnPressed.connect(self.search)
        self.addressBar.returnPressed.connect(
                                  self.addressBar.selectAll)
        self.searchButton.clicked.connect(self.search)
        self.searchButton.clicked.connect(
                                  self.addressBar.selectAll)

app = QApplication(sys.argv)

browser = Browser()
sys.exit(app.exec_())
