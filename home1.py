# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from testbench import Ui_secondwindow
from testbench2 import Ui_secondwindow2
from testbench5 import Ui_secondwindow5
from testbench4 import Ui_secondwindow4
from testbench3 import Ui_secondwindow3


class Ui_MainWindow(object):
    def newwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_secondwindow()
        self.ui.setupUi(self.window)
        self.window.showFullScreen()
        MainWindow.hide()
        
       
    def newwindow1(self):
        self.window = QtWidgets.QMainWindow()
        self.ti = Ui_secondwindow2()
        self.ti.setupUi(self.window)
        self.window.showFullScreen()
        MainWindow.hide()
        
    def newwindow2(self):
        self.window = QtWidgets.QMainWindow()
        self.ti = Ui_secondwindow4()
        self.ti.setupUi(self.window)
        self.window.showFullScreen()
        MainWindow.hide()
        
    def newwindow3(self):
        self.window = QtWidgets.QMainWindow()
        self.ti = Ui_secondwindow3()
        self.ti.setupUi(self.window)
        self.window.showFullScreen()
        MainWindow.hide()   
        
    def newwindow4(self):
        self.window = QtWidgets.QMainWindow()
        self.ti = Ui_secondwindow5()
        self.ti.setupUi(self.window)
        self.window.showFullScreen()
        MainWindow.hide()        
    
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setStyleSheet("background-color:qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255))")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.upLeft = QtWidgets.QPushButton(self.centralwidget)
        self.upLeft.setGeometry(QtCore.QRect(40, 120, 161, 211))
        self.upLeft.clicked.connect(self.newwindow)
        self.upLeft.setStyleSheet("#upLeft {\n"
"background-color: transparent;\n"
"border-image: url(:/Blade-Runner-2049-Final-Style-Poster-buy-original-movie-posters-at-starstills__83407.1519904794.jpg);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"")
        self.upLeft.setText("")
        self.upLeft.setObjectName("upLeft")
        self.down = QtWidgets.QPushButton(self.centralwidget)
        self.down.setGeometry(QtCore.QRect(240, 120, 161, 211))
        self.down.setStyleSheet("#down {\n"
"background-color: transparent;\n"
"border-image:url(:/inception_ver12.jpg);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"")
        self.down.setText("")
        self.down.setObjectName("down")
        self.third = QtWidgets.QPushButton(self.centralwidget)
        self.third.setGeometry(QtCore.QRect(440, 120, 161, 211))
        self.third.setStyleSheet("#third {\n"
"background-color: transparent;\n"
"border-image: url(:/logan.jpg);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"")
        self.third.setText("")
        self.third.setObjectName("third")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 350, 131, 31))
        self.label.setStyleSheet("background-color:none;\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 350, 61, 21))
        self.label_2.setStyleSheet("background-color:none;\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(500, 350, 41, 21))
        self.label_3.setStyleSheet("background-color:none;\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.third_2 = QtWidgets.QPushButton(self.centralwidget)
        self.third_2.setGeometry(QtCore.QRect(640, 120, 161, 211))
        self.third_2.setStyleSheet(" #third_2{\n"
"background-color: transparent;\n"
"border-image: url(:/captain america.jpg);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"\n"
"}")
        self.third_2.setText("")
        self.third_2.setObjectName("third_2")
        self.third_3 = QtWidgets.QPushButton(self.centralwidget)
        self.third_3.setGeometry(QtCore.QRect(840, 120, 161, 211))
        self.third_3.setStyleSheet("#third_3 {\n"
"background-color: transparent;\n"
"border-image:url(:/insidious.jpg);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"")
        self.third_3.setText("")
        self.third_3.setObjectName("third_3")
        self.third_3.clicked.connect(self.newwindow3)
        
        self.third_4 = QtWidgets.QPushButton(self.centralwidget)
        self.third_4.setGeometry(QtCore.QRect(40, 400, 161, 211))
        self.third_4.setStyleSheet("#third_4 {\n"
"background-color: transparent;\n"
"border-image:url(:/oblivion.jpg);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"")
        self.third_4.setText("")
        self.third_4.setObjectName("third_4")
        self.third_4.clicked.connect(self.newwindow2)
        
        self.third_5 = QtWidgets.QPushButton(self.centralwidget)
        self.third_5.setGeometry(QtCore.QRect(240, 400, 161, 211))
        self.third_5.setStyleSheet("#third_5 {\n"
"background-color: transparent;\n"
"border-image: url(:/once upon a time.jpg);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"")
        self.third_5.setText("")
        self.third_5.setObjectName("third_5")
        self.third_5.clicked.connect(self.newwindow4)
        
        self.third_6 = QtWidgets.QPushButton(self.centralwidget)
        self.third_6.setGeometry(QtCore.QRect(440, 400, 161, 211))
        self.third_6.setStyleSheet("#third_6 {\n"
"background-color: transparent;\n"
"border-image: url(:/the godfather.jpg);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"")
        self.third_6.setText("")
        self.third_6.setObjectName("third_6")
        self.third_7 = QtWidgets.QPushButton(self.centralwidget)
        self.third_7.setGeometry(QtCore.QRect(630, 400, 161, 211))
        self.third_7.setStyleSheet("#third_7 {\n"
"background-color: transparent;\n"
"border-image:url(:/thor-the-dark-world-movie-poster-international.jpg);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"")
        self.third_7.setText("")
        self.third_7.setObjectName("third_7")
        self.third_8 = QtWidgets.QPushButton(self.centralwidget)
        self.third_8.setGeometry(QtCore.QRect(830, 400, 161, 211))
        self.third_8.setStyleSheet("#third_8 {\n"
"background-color: transparent;\n"
"border-image: url(:/Thor-Ragnarok-HD-printable-official-posters-692x1024.jpg);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"")
        self.third_8.setText("")
        self.third_8.setObjectName("third_8")
        self.third_8.clicked.connect(self.newwindow1)
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(680, 350, 71, 21))
        self.label_4.setStyleSheet("background-color:none;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.third_9 = QtWidgets.QPushButton(self.centralwidget)
        self.third_9.setGeometry(QtCore.QRect(1040, 400, 161, 211))
        self.third_9.setStyleSheet("#third_9 {\n"
"background-color: transparent;\n"
"border-image: url(:/braveheart.jpg);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"")
        self.third_9.setText("")
        self.third_9.setObjectName("third_9")
        self.third_10 = QtWidgets.QPushButton(self.centralwidget)
        self.third_10.setGeometry(QtCore.QRect(1040, 120, 161, 211))
        self.third_10.setStyleSheet("#third_10 {\n"
"background-color: transparent;\n"
"border-image: url(:/legion movie scenes.jpg);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"")
        self.third_10.setText("")
        self.third_10.setObjectName("third_10")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 10, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(52)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color:none;\n"
"\n"
"font: 52pt \"Gabriola\";\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(90, 630, 61, 21))
        self.label_6.setStyleSheet("background-color:none;\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(220, 630, 211, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color:none;\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(470, 630, 101, 21))
        self.label_8.setStyleSheet("background-color:none;\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(690, 630, 41, 21))
        self.label_9.setStyleSheet("background-color:none;\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(670, 350, 111, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color:none;\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(900, 350, 61, 21))
        self.label_11.setStyleSheet("background-color:none;\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(870, 630, 101, 21))
        self.label_12.setStyleSheet("background-color:none;\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(1080, 630, 81, 21))
        self.label_13.setStyleSheet("background-color:none;\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(1100, 350, 51, 21))
        self.label_14.setStyleSheet("background-color:none;\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.label_14.setObjectName("label_14")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Blade Runner:2049"))
        self.label_2.setText(_translate("MainWindow", "Inception"))
        self.label_3.setText(_translate("MainWindow", "logan"))
        self.label_5.setText(_translate("MainWindow", "Cineplex"))
        self.label_6.setText(_translate("MainWindow", "Oblivion"))
        self.label_7.setText(_translate("MainWindow", "Once upon a time in holloywood"))
        self.label_8.setText(_translate("MainWindow", "The Godfather"))
        self.label_9.setText(_translate("MainWindow", "Thor"))
        self.label_10.setText(_translate("MainWindow", "Captain America"))
        self.label_11.setText(_translate("MainWindow", "Insidious"))
        self.label_12.setText(_translate("MainWindow", "Thor Ragnarok"))
        self.label_13.setText(_translate("MainWindow", "Braveheart"))
        self.label_14.setText(_translate("MainWindow", "Legion"))
import img


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showFullScreen()
    sys.exit(app.exec_())
