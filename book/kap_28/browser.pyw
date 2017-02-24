#! /Python34/pythonw.exe

#----------------------------------------------------
# Dateiname:  browser.pyw 
# Ein einfacher Webbrowser.
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
    def __init__(self):
        super().__init__()
        self.createWidgets()                           #1
        self.createLayout()
        self.createConnections()
        self.show()                                   

    def search(self):
        # Zeige Webseite
        address = str(self.addressBar.text())          #2
        if address:                                    #3
            if "://" not in address:
                address = "http://" + address          #4
            url = QUrl(address)                        #5
            self.webView.load(url)                     #6

    def createWidgets(self):
        self.setWindowTitle("Welt-Browser")            #7
        self.setWindowIcon(QIcon("welt.png"))          #8
        self.webView = QWebView(self)                  #9
        self.addressBar = QLineEdit(self)              #10
        self.searchButton = QPushButton("Suchen", self)#11


    def createLayout(self):
        hbl = QHBoxLayout()                            #12
        hbl.addWidget(self.addressBar)                
        hbl.addWidget(self.searchButton)
        vbl = QVBoxLayout()                            #13
        vbl.addLayout(hbl)
        vbl.addWidget(self.webView)
        self.setLayout(vbl)                            #14

    def createConnections(self):                       #15
        self.addressBar.returnPressed.connect(self.search)
        self.searchButton.clicked.connect(self.search)
        

app = QApplication(sys.argv)
browser = Browser()
sys.exit(app.exec_())
