# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testbench.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from testdialog import *
from seatboxfinal import *


class Ui_secondwindow(object):
    
    def newwindow4(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_fourthwindow()
        self.ui.setupUi(self.window)
        self.window.showFullScreen()
        
        

        
    def setupUi(self, secondwindow):
        secondwindow.setObjectName("secondwindow")
        secondwindow.resize(1367, 777)
        font = QtGui.QFont()
        font.setPointSize(12)
        secondwindow.setFont(font)
        secondwindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        secondwindow.setStyleSheet("background-color:qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255))")
        self.centralwidget = QtWidgets.QWidget(secondwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(510, 50, 421, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:none;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 370, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border:none;\n"
"background-color:none;")
        self.label_3.setObjectName("label_3")
        self.timing1 = QtWidgets.QPushButton(self.centralwidget)
        self.timing1.setGeometry(QtCore.QRect(260, 70, 221, 271))
        self.timing1.setStyleSheet("#timing1 {\n"
"background-color: transparent;\n"
"border-image: url(:/Blade-Runner-2049-Final-Style-Poster-buy-original-movie-posters-at-starstills__83407.1519904794.jpg);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"")
        self.timing1.setText("")
        self.timing1.setObjectName("timing1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(570, 280, 239, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border:none;\n"
"background-color:none;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lower2 = QtWidgets.QPushButton(self.centralwidget)
        self.lower2.setGeometry(QtCore.QRect(570, 210, 239, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lower2.setFont(font)
        self.lower2.setStyleSheet("border:none;\n"
"background-color:none;")
        self.lower2.setObjectName("lower2")
        self.lower2_2 = QtWidgets.QPushButton(self.centralwidget)
        self.lower2_2.setGeometry(QtCore.QRect(570, 150, 239, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lower2_2.setFont(font)
        self.lower2_2.setStyleSheet("border:none;\n"
"background-color:none;")
        self.lower2_2.setObjectName("lower2_2")
        self.lower2_2.clicked.connect(self.newwindow4)
        
        secondwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(secondwindow)
        self.statusbar.setObjectName("statusbar")
        secondwindow.setStatusBar(self.statusbar)

        self.retranslateUi(secondwindow)
        QtCore.QMetaObject.connectSlotsByName(secondwindow)

        
    def retranslateUi(self, secondwindow):
        _translate = QtCore.QCoreApplication.translate
        secondwindow.setWindowTitle(_translate("secondwindow", "MainWindow"))
        self.label_2.setText(_translate("secondwindow", "Available show timings are"))
        self.label_3.setText(_translate("secondwindow", "Blade runner : 2049"))
        self.pushButton_2.setText(_translate("secondwindow", "6:00 PM"))
        self.lower2.setText(_translate("secondwindow", "3:00 PM"))
        self.lower2_2.setText(_translate("secondwindow", "12:00 PM"))
import img


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    secondwindow = QtWidgets.QMainWindow()
    ui = Ui_secondwindow()
    ui.setupUi(secondwindow)
    secondwindow.showFullScreen()
    sys.exit(app.exec_())
