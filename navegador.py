#!/usr/bin/env python3

from PyQt5.QtWidgets import  QApplication, QMainWindow, QToolButton, QLineEdit,QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl,QSize
from PyQt5.QtGui import QIcon, QPixmap


application = QApplication([])

home_url = "https://www.google.com"

mainwindows = QMainWindow()
mainwindows.setGeometry(0,0,1250,950)
mainwindows.setWindowTitle("Navegador")
mainwindows.setStyleSheet("background-color: rgb(0,0,0);")


web = QWebEngineView(mainwindows)
web.setGeometry(0,30,1250,950)
web.setStyleSheet("background-color: rgb(255,255,255);")
web.load(QUrl(home_url))


go_line =QLineEdit(mainwindows)
go_line.setGeometry(280,1,900,25)
go_line.setStyleSheet("background-color: rgb(70,130,180);")




home_buton = QToolButton(mainwindows)
home_buton.setGeometry(2,1,70,25)
home_buton.setStyleSheet("background-color: rgb(70,130,180);")
home_buton.setText("Home")



reload_buton = QToolButton(mainwindows)
reload_buton.setGeometry(70,1,70,25)
reload_buton.setStyleSheet("background-color: rgb(70,130,180);")
reload_buton.setText("Reload")

tras_buton = QToolButton(mainwindows)
tras_buton.setGeometry(140,1,70,25)
tras_buton.setStyleSheet("background-color: rgb(70,130,180);")
tras_buton.setText("<")

frent_buton = QToolButton(mainwindows)
frent_buton.setGeometry(210,1,70,25)
frent_buton.setStyleSheet("background-color: rgb(70,130,180);")
frent_buton.setText(">")

go_buton = QToolButton(mainwindows)
go_buton.setGeometry(1185,1,70,25)
go_buton.setStyleSheet("background-color: rgb(70,130,180);")
go_buton.setText("Go")


def home(mainwindows):
    web.load(QUrl(home_url))



def reload(mainwindows):
    web.reload()


def tras(mainwindows):
    web.back()


def frente (mainwindows):
    web.forward()


def go (mainwindows):
    go_url = go_line.text()
    web.load(QUrl(go_url))



home_buton.clicked.connect(home)
reload_buton.clicked.connect(reload)
tras_buton.clicked.connect(tras)
frent_buton.clicked.connect(frente)
go_buton.clicked.connect(go)



mainwindows.show()
application.exec_()     