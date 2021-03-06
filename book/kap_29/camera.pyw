#! /Python34/pythonw.exe

# ----------------------------------------------------
# Dateiname:  camera.pyw
# Fotos aufnehmen und speichern
#
# Python 3, 6. Auflage, mitp 2016
# Kap. 29
# Michael Weigend 22.09.2016
# ----------------------------------------------------

# camera.pyw
import sys
import time

from PyQt5.QtMultimedia import (QCamera,
                                QCameraImageCapture)
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.createWidgets()
        self.createCamera()
        self.createLayout()
        self.show()

    def takePhoto(self):
        if self.imageCapture.isReadyForCapture():
            path = 'c:\\media\\foto%s.jpg' % str(time.time())
            self.imageCapture.capture(path)

    def createWidgets(self):
        self.videoWidget = QVideoWidget()
        self.button = QPushButton("Foto")
        self.button.clicked.connect(self.takePhoto)

    def createLayout(self):
        self.box = QVBoxLayout()
        self.box.addWidget(self.videoWidget)
        self.box.addWidget(self.button)
        self.setLayout(self.box)

    def createCamera(self):
        self.device = QCamera.availableDevices()[0]
        self.camera = QCamera(self.device)
        self.camera.setViewfinder(self.videoWidget)
        self.camera.setCaptureMode(
            QCamera.CaptureStillImage)
        self.imageCapture = QCameraImageCapture(
            self.camera)
        self.camera.start()  # Startet Sucherbild


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
