#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, random
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
import PyQt5.QtCore

class Arayuz(QWidget):

    renk = "kirmizi"

    def __init__(self):

        super().__init__()
        self.initUI()

    def zarUret(self):

        rasgele1 = random.randint(1,6)
        rasgele2 = random.randint(1,6)

        return [rasgele1,rasgele2]

    def zarDegistir(self, hangi, sayi):

        resim_adresi = "resim/" + self.renk + "/" + str(sayi) + ".png"
        resim = QPixmap(resim_adresi)
        resim = resim.scaled(100, 100, PyQt5.QtCore.Qt.KeepAspectRatio)
        if hangi == 1:
            self.zar1.setPixmap(resim)
        else:
            self.zar2.setPixmap(resim)


    def zarAtOnClick(self):

        sonuc = self.zarUret()
        self.zarDegistir(1, sonuc[0])
        self.zarDegistir(2, sonuc[1])
        if(self.renk == "siyah"):
            self.renk = "kirmizi"
        else:
            self.renk = "siyah"

    def initUI(self):

        self.resize(280,240)
        self.setFixedSize(280,240)
        self.center()
        self.setWindowTitle("Zar Uygulaması")
        self.setWindowIcon(QIcon("resim/icon.png"))
        self.setStyleSheet("background-color: white")

        self.zar1 = QLabel(self)
        self.zar2 = QLabel(self)

        self.zar1.resize(100,100)
        self.zar2.resize(100,100)

        self.zar1.move(30,30)
        self.zar2.move(150,30)

        self.zar1.setStyleSheet("border-radius: 10px")
        self.zar2.setStyleSheet("border-radius: 10px")

        bekle_resim_adresi = "resim/bekle.png"
        bekle_resim = QPixmap(bekle_resim_adresi)
        bekle_resim = bekle_resim.scaled(100, 100, PyQt5.QtCore.Qt.KeepAspectRatio)
        self.zar1.setPixmap(bekle_resim)
        self.zar2.setPixmap(bekle_resim)

        self.zarAt = QPushButton("ZAR AT", self)
        self.zarAt.resize(220, 50)
        self.zarAt.move(30,160)
        self.zarAt.clicked.connect(self.zarAtOnClick)

        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = Arayuz()
    sys.exit(app.exec_())

