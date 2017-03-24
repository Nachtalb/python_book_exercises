#! /Python34/pythonw.exe

# ----------------------------------------------------
# Dateiname:  browser_verlauf.pyw
# Browser, der den Verlauf einer Sitzung anzeigemn kann.
#
# Python 3, 6. Auflage, mitp 2016
# Kap. 28
# Michael Weigend 22.09.2016
# ----------------------------------------------------
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebKit import *
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtWidgets import *

HISTORY_PATTERN = """
<html><body bgcolor="#C0C0FF">
   <h1>Verlauf</h1>
   %s
</body></html>"""


class Browser(QWidget):
    def __init__(self):
        super().__init__()
        self.createWidgets()
        self.createLayout()
        self.createConnections()
        self.show()

    def search(self):
        # Zeige Webseite
        address = str(self.addressBar.text())
        history = self.webView.history().items()
        if address:
            if "://" not in address:
                address = "http://" + address
            url = QUrl(address)
            self.webView.load(url)

    def showHistory(self):
        history = self.webView.history().items()
        htmlHistory = ""
        for i in history:
            htmlHistory += '<a href="%s"> %s </a><br/>' % \
                           (i.url().toString(), i.title())
        self.webView.setHtml(HISTORY_PATTERN % htmlHistory)

    def createWidgets(self):
        self.setWindowTitle("Welt-Browser")
        self.setWindowIcon(QIcon("welt.png"))
        self.webView = QWebView(self)
        self.addressBar = QLineEdit(self)
        self.searchButton = QPushButton("Suchen", self)
        self.historyButton = QPushButton("Verlauf", self)

    def createLayout(self):
        hbl = QHBoxLayout()
        hbl.addWidget(self.addressBar)
        hbl.addWidget(self.searchButton)
        hbl.addWidget(self.historyButton)
        vbl = QVBoxLayout()
        vbl.addLayout(hbl)
        vbl.addWidget(self.webView)
        self.setLayout(vbl)

    def createConnections(self):
        self.addressBar.returnPressed.connect(self.search)
        self.searchButton.clicked.connect(self.search)
        self.historyButton.clicked.connect(self.showHistory)


app = QApplication(sys.argv)
browser = Browser()
sys.exit(app.exec_())
