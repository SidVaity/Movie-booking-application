# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seatboxfinal.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QTableWidgetItem
from seatlink import Ui_fifthwindow
import sqlite3

class Ui_fourthwindow(object):

    def newwindow5(self):
        self.window = QtWidgets.QMainWindow()
        self.ui= Ui_fifthwindow()
        self.ui.setupUi(self.window)
        self.window.showFullScreen()
        
      
        self.ui.lineEdit.setText(self.lineEdit_6.text()+""+self.lineEdit_7.text()+""+self.lineEdit_10.text()+""+self.lineEdit_16.text()+""+self.lineEdit_21.text()+""+self.lineEdit_2.text()+""+self.lineEdit_3.text()+""+self.lineEdit.text()+""+self.lineEdit_17.text()+""+self.lineEdit_22.text()+""+self.lineEdit_8.text()+""+self.lineEdit_9.text()+" "+self.lineEdit_4.text()
        +""+self.lineEdit_18.text()+""+self.lineEdit_23.text()+""+self.lineEdit_11.text()+""+self.lineEdit_12.text()+""+self.lineEdit_5.text()+""+self.lineEdit_19.text()+""+self.lineEdit_24.text()+""+self.lineEdit_13.text()+self.lineEdit_14.text()+""+self.lineEdit_15.text()+""+self.lineEdit_20.text()+""+self.lineEdit_25.text())        

  
        
    
    def setupUi(self, fourthwindow):
        fourthwindow.setObjectName("fourthwindow")
        fourthwindow.resize(1368, 768)
        fourthwindow.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0.338983 rgba(218, 189, 79, 255), stop:1 rgba(255, 255, 255, 255))")
        self.centralwidget = QtWidgets.QWidget(fourthwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(250, 20, 771, 361))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_19 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_19.setObjectName("checkBox_19")
        self.gridLayout.addWidget(self.checkBox_19, 3, 3, 1, 1)
        self.checkBox_19.clicked.connect(self.oncheck)
        self.checkBox_19.setIcon(QtGui.QIcon("seat1.webp"))
        self.checkBox_19.setIconSize(QtCore.QSize(30,30))
        
        self.checkBox_6 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout.addWidget(self.checkBox_6, 0, 0, 1, 1)
        self.checkBox_6.clicked.connect(self.oncheck)
        self.checkBox_6.setIcon(QtGui.QIcon("seat1.webp"))
        self.checkBox_6.setIconSize(QtCore.QSize(30,30))
        
        self.checkBox_9 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout.addWidget(self.checkBox_9, 2, 1, 1, 1)
        self.checkBox_9.clicked.connect(self.oncheck)
        self.checkBox_9.setIcon(QtGui.QIcon("seat1.webp"))
        self.checkBox_9.setIconSize(QtCore.QSize(30,30))
        
        self.checkBox_22 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_22.setObjectName("checkBox_22")
        self.gridLayout.addWidget(self.checkBox_22, 1, 4, 1, 1)
        self.checkBox_22.clicked.connect(self.oncheck)
        self.checkBox_22.setIcon(QtGui.QIcon("seat1.webp"))
        self.checkBox_22.setIconSize(QtCore.QSize(30,30))
        
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 1, 2, 1, 1)
        self.checkBox.clicked.connect(self.oncheck)
        self.checkBox.setIcon(QtGui.QIcon("seat1.webp"))
        self.checkBox.setIconSize(QtCore.QSize(30,30))
        
        self.checkBox_16 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_16.setObjectName("checkBox_16")
        self.gridLayout.addWidget(self.checkBox_16, 0, 3, 1, 1)
        self.checkBox_16.clicked.connect(self.oncheck)
        self.checkBox_16.setIcon(QtGui.QIcon("seat1.webp"))
        self.checkBox_16.setIconSize(QtCore.QSize(30,30))
        
        self.checkBox_10 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_10.setObjectName("checkBox_10")
        self.gridLayout.addWidget(self.checkBox_10, 0, 2, 1, 1)
        self.checkBox_10.clicked.connect(self.oncheck)
        self.checkBox_10.setIcon(QtGui.QIcon("seat1.webp"))
        self.checkBox_10.setIconSize(QtCore.QSize(30,30))
        
        self.checkBox_2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 1, 0, 1, 1)
        self.checkBox_2.clicked.connect(self.oncheck)
        self.checkBox_2.setIcon(QtGui.QIcon("seat1.webp"))
        self.checkBox_2.setIconSize(QtCore.QSize(30,30))
        
        self.checkBox_20 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_20.setObjectName("checkBox_20")
        self.gridLayout.addWidget(self.checkBox_20, 4, 3, 1, 1)
        self.checkBox_20.clicked.connect(self.oncheck)
        self.checkBox_20.setIcon(QtGui.QIcon("seat1.webp"))
        self.checkBox_20.setIconSize(QtCore.QSize(30,30))
        
        self.checkBox_18 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_18.setObjectName("checkBox_18")
        self.gridLayout.addWidget(self.checkBox_18, 2, 3, 1, 1)
        self.checkBox_18.clicked.connect(self.oncheck)
        self.checkBox_18.setIcon(QtGui.QIcon("seat1.webp"))
        self.checkBox_18.setIconSize(QtCore.QSize(30,30))
        
        self.checkBox_24 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_24.setObjectName("checkBox_24")
        self.gridLayout.addWidget(self.checkBox_24, 3, 4, 1, 1)
        self.checkBox_24.clicked.connect(self.oncheck)
        self.checkBox_24.setIcon(QtGui.QIcon("seat1.webp"))
        self.checkBox_24.setIconSize(QtCore.QSize(30,30))
        
        self.checkBox_15 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_15.setObjectName("checkBox_15")
        self.gridLayout.addWidget(self.checkBox_15, 4, 2, 1, 1)
        self.checkBox_15.clicked.connect(self.oncheck)
        self.checkBox_15.setIcon(QtGui.QIcon("seat1.webp"))
        self.checkBox_15.setIconSize(QtCore.QSize(30,30))
        
        self.checkBox_23 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_23.setObjectName("checkBox_23")
        self.gridLayout.addWidget(self.checkBox_23, 2, 4, 1, 1)
        self.checkBox_23.clicked.connect(self.oncheck)
        self.checkBox_23.setIcon(QtGui.QIcon("seat1.webp"))
        self.checkBox_23.setIconSize(QtCore.QSize(30,30))
        
        self.checkBox_14 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_14.setObjectName("checkBox_14")
        self.gridLayout.addWidget(self.checkBox_14, 4, 1, 1, 1)
        self.checkBox_14.clicked.connect(self.oncheck)
        self.checkBox_14.setIcon(QtGui.QIcon("seat1.webp"))
        self.checkBox_14.setIconSize(QtCore.QSize(30,30))
        
        self.checkBox_3 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 1, 1, 1, 1)
        self.checkBox_3.clicked.connect(self.oncheck)
        self.checkBox_3.setIcon(QtGui.QIcon("seat1.webp"))
        self.checkBox_3.setIconSize(QtCore.QSize(30,30))
        
        self.checkBox_8 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout.addWidget(self.checkBox_8, 2, 0, 1, 1)
        self.checkBox_8.clicked.connect(self.oncheck)
        self.checkBox_8.setIcon(QtGui.QIcon("seat1.webp"))
        self.checkBox_8.setIconSize(QtCore.QSize(30,30))
        
        self.checkBox_12 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_12.setObjectName("checkBox_12")
        self.gridLayout.addWidget(self.checkBox_12, 3, 1, 1, 1)
        self.checkBox_12.clicked.connect(self.oncheck)
        self.checkBox_12.setIcon(QtGui.QIcon("seat1.webp"))
        self.checkBox_12.setIconSize(QtCore.QSize(30,30))
        
        self.checkBox_5 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 3, 2, 1, 1)
        self.checkBox_5.clicked.connect(self.oncheck)
        self.checkBox_5.setIcon(QtGui.QIcon("seat1.webp"))
        self.checkBox_5.setIconSize(QtCore.QSize(30,30))
        
        self.checkBox_25 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_25.setObjectName("checkBox_25")
        self.gridLayout.addWidget(self.checkBox_25, 4, 4, 1, 1)
        self.checkBox_25.clicked.connect(self.oncheck)
        self.checkBox_25.setIcon(QtGui.QIcon("seat1.webp"))
        self.checkBox_25.setIconSize(QtCore.QSize(30,30))
        
        self.checkBox_17 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_17.setObjectName("checkBox_17")
        self.gridLayout.addWidget(self.checkBox_17, 1, 3, 1, 1)
        self.checkBox_17.clicked.connect(self.oncheck)
        self.checkBox_17.setIcon(QtGui.QIcon("seat1.webp"))
        self.checkBox_17.setIconSize(QtCore.QSize(30,30))
        
        self.checkBox_21 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_21.setObjectName("checkBox_21")
        self.gridLayout.addWidget(self.checkBox_21, 0, 4, 1, 1)
        self.checkBox_21.clicked.connect(self.oncheck)
        self.checkBox_21.setIcon(QtGui.QIcon("seat1.webp"))
        self.checkBox_21.setIconSize(QtCore.QSize(30,30))
        
        self.checkBox_11 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_11.setObjectName("checkBox_11")
        self.gridLayout.addWidget(self.checkBox_11, 3, 0, 1, 1)
        self.checkBox_11.clicked.connect(self.oncheck)
        self.checkBox_11.setIcon(QtGui.QIcon("seat1.webp"))
        self.checkBox_11.setIconSize(QtCore.QSize(30,30))
        
        self.checkBox_7 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout.addWidget(self.checkBox_7, 0, 1, 1, 1)
        self.checkBox_7.clicked.connect(self.oncheck)
        self.checkBox_7.setIcon(QtGui.QIcon("seat1.webp"))
        self.checkBox_7.setIconSize(QtCore.QSize(30,30))
        
        self.checkBox_13 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_13.setObjectName("checkBox_13")
        self.gridLayout.addWidget(self.checkBox_13, 4, 0, 1, 1)
        self.checkBox_13.clicked.connect(self.oncheck)
        self.checkBox_13.setIcon(QtGui.QIcon("seat1.webp"))
        self.checkBox_13.setIconSize(QtCore.QSize(30,30))
        
        self.checkBox_4 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 2, 2, 1, 1)
        self.checkBox_4.clicked.connect(self.oncheck)
        self.checkBox_4.setIcon(QtGui.QIcon("seat1.webp"))
        self.checkBox_4.setIconSize(QtCore.QSize(30,30))
        
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(230, 570, 121, 151))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        
       
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(480, 450, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 530, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(50, 570, 21, 21))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(70, 570, 21, 21))
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(90, 570, 21, 21))
        self.lineEdit_10.setText("")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 590, 21, 21))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 610, 21, 21))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_18.setGeometry(QtCore.QRect(110, 610, 21, 21))
        self.lineEdit_18.setText("")
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 590, 21, 21))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 590, 21, 21))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_19.setGeometry(QtCore.QRect(110, 630, 21, 21))
        self.lineEdit_19.setText("")
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_16.setGeometry(QtCore.QRect(110, 570, 21, 21))
        self.lineEdit_16.setText("")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_17.setGeometry(QtCore.QRect(110, 590, 21, 21))
        self.lineEdit_17.setText("")
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(70, 610, 21, 21))
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(50, 610, 21, 21))
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(70, 630, 21, 21))
        self.lineEdit_12.setText("")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_21.setGeometry(QtCore.QRect(130, 570, 21, 21))
        self.lineEdit_21.setText("")
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_22.setGeometry(QtCore.QRect(130, 590, 21, 21))
        self.lineEdit_22.setText("")
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_23.setGeometry(QtCore.QRect(130, 610, 21, 21))
        self.lineEdit_23.setText("")
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(50, 630, 21, 21))
        self.lineEdit_11.setText("")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_24.setGeometry(QtCore.QRect(130, 630, 21, 21))
        self.lineEdit_24.setText("")
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(90, 630, 21, 21))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_20.setGeometry(QtCore.QRect(110, 650, 21, 21))
        self.lineEdit_20.setText("")
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_14.setGeometry(QtCore.QRect(70, 650, 21, 21))
        self.lineEdit_14.setText("")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_13.setGeometry(QtCore.QRect(50, 650, 21, 21))
        self.lineEdit_13.setText("")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_25.setGeometry(QtCore.QRect(130, 650, 21, 21))
        self.lineEdit_25.setText("")
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_15.setGeometry(QtCore.QRect(90, 650, 21, 21))
        self.lineEdit_15.setText("")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1020, 610, 101, 31))
        self.pushButton.setStyleSheet("background-color:rgb(232, 232, 232)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.newwindow5)
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(830, 610, 101, 31))
        self.pushButton_2.setStyleSheet("background-color:rgb(232, 232, 232)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.checkseats)
        
        
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 530, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        fourthwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(fourthwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 869, 21))
        self.menubar.setObjectName("menubar")
        fourthwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(fourthwindow)
        self.statusbar.setObjectName("statusbar")
        fourthwindow.setStatusBar(self.statusbar)

        self.retranslateUi(fourthwindow)
        QtCore.QMetaObject.connectSlotsByName(fourthwindow)
        
        
        
    def oncheck(self):
    
        if self.checkBox_6.isChecked():
            self.lineEdit_6.setText(""+self.checkBox_6.text())
            

        if self.checkBox_7.isChecked():
            self.lineEdit_7.setText(""+self.checkBox_7.text())
            
         
        if self.checkBox_10.isChecked():
            self.lineEdit_10.setText(""+self.checkBox_10.text())
           
                
        if self.checkBox_16.isChecked():
            self.lineEdit_16.setText(""+self.checkBox_16.text())

        if self.checkBox_21.isChecked():
            self.lineEdit_21.setText(""+self.checkBox_21.text())

        if self.checkBox_2.isChecked():
            self.lineEdit_2.setText(""+self.checkBox_2.text())
           
            

        if self.checkBox_3.isChecked():
            self.lineEdit_3.setText(""+self.checkBox_3.text())
          

        if self.checkBox.isChecked():
            self.lineEdit.setText(""+self.checkBox.text())
         

        if self.checkBox_17.isChecked():
            self.lineEdit_17.setText(""+self.checkBox_17.text())
              

        if self.checkBox_22.isChecked():
            self.lineEdit_22.setText(""+self.checkBox_22.text())
       

        if self.checkBox_8.isChecked():
            self.lineEdit_8.setText(""+self.checkBox_8.text())
       
            
        if self.checkBox_9.isChecked():
            self.lineEdit_9.setText(""+self.checkBox_9.text())
           
            
        if self.checkBox_4.isChecked():
            self.lineEdit_4.setText(""+self.checkBox_4.text())
          
            
        if self.checkBox_18.isChecked():
            self.lineEdit_18.setText(""+self.checkBox_18.text())
         
            
        if self.checkBox_23.isChecked():
            self.lineEdit_23.setText(""+self.checkBox_23.text())
            
             
        if self.checkBox_11.isChecked():
            self.lineEdit_11.setText(""+self.checkBox_11.text())
         
            
        if self.checkBox_12.isChecked():
            self.lineEdit_12.setText(""+self.checkBox_12.text())
        
            
        if self.checkBox_5.isChecked():
            self.lineEdit_5.setText(""+self.checkBox_5.text())
         
            
        if self.checkBox_19.isChecked():
            self.lineEdit_19.setText(""+self.checkBox_19.text())
           

        if self.checkBox_24.isChecked():
            self.lineEdit_24.setText(""+self.checkBox_24.text())
            

        if self.checkBox_13.isChecked():
            self.lineEdit_13.setText(""+self.checkBox_13.text())
            
      
        if self.checkBox_14.isChecked():
            self.lineEdit_14.setText(""+self.checkBox_14.text())
           
             
        if self.checkBox_15.isChecked():
            self.lineEdit_15.setText(""+self.checkBox_15.text())
            
            
        if self.checkBox_20.isChecked():
            self.lineEdit_20.setText(""+self.checkBox_20.text())
           
            
        if self.checkBox_25.isChecked():
            self.lineEdit_25.setText(""+self.checkBox_25.text())
           
             

    def checkseats(self):
        conn = sqlite3.connect('testdb3.db')
        c = conn.cursor()
        content = 'SELECT * FROM student'
        res = conn.execute(content)
        self.tableWidget.setRowCount(0)
        for row_index ,row_data in enumerate(res):
            self.tableWidget.insertRow(row_index)
            for column_index ,column_data in enumerate(row_data):
                self.tableWidget.setItem(row_index,column_index,QTableWidgetItem(str(column_data)))
           
        conn.close()
            
        
            
            
            

    def retranslateUi(self, fourthwindow):
        _translate = QtCore.QCoreApplication.translate
        fourthwindow.setWindowTitle(_translate("fourthwindow", "MainWindow"))
        self.checkBox_19.setText(_translate("fourthwindow", "D4"))
        self.checkBox_6.setText(_translate("fourthwindow", "A1"))
        self.checkBox_9.setText(_translate("fourthwindow", "C2"))
        self.checkBox_22.setText(_translate("fourthwindow", "B5"))
        self.checkBox.setText(_translate("fourthwindow", "B3"))
        self.checkBox_16.setText(_translate("fourthwindow", "A4"))
        self.checkBox_10.setText(_translate("fourthwindow", "A3"))
        self.checkBox_2.setText(_translate("fourthwindow", "B1"))
        self.checkBox_20.setText(_translate("fourthwindow", "E4"))
        self.checkBox_18.setText(_translate("fourthwindow", "C4"))
        self.checkBox_24.setText(_translate("fourthwindow", "D5"))
        self.checkBox_15.setText(_translate("fourthwindow", "E3"))
        self.checkBox_23.setText(_translate("fourthwindow", "C5"))
        self.checkBox_14.setText(_translate("fourthwindow", "E2"))
        self.checkBox_3.setText(_translate("fourthwindow", "B2"))
        self.checkBox_8.setText(_translate("fourthwindow", "C1"))
        self.checkBox_12.setText(_translate("fourthwindow", "D2"))
        self.checkBox_5.setText(_translate("fourthwindow", "D3"))
        self.checkBox_25.setText(_translate("fourthwindow", "E5"))
        self.checkBox_17.setText(_translate("fourthwindow", "B4"))
        self.checkBox_21.setText(_translate("fourthwindow", "A5"))
        self.checkBox_11.setText(_translate("fourthwindow", "D1"))
        self.checkBox_7.setText(_translate("fourthwindow", "A2"))
        self.checkBox_13.setText(_translate("fourthwindow", "E1"))
        self.checkBox_4.setText(_translate("fourthwindow", "C3"))
        self.label.setText(_translate("fourthwindow", "Screen is here"))
        self.label_2.setText(_translate("fourthwindow", "Preview of your seats:"))
        self.pushButton.setText(_translate("fourthwindow", "Book them"))
        self.pushButton_2.setText(_translate("fourthwindow", "Check seats"))
        self.label_3.setText(_translate("fourthwindow", "Already selected seats :"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("fourthwindow", "Prebooked seats"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("fourthwindow", "us"))
                 
        
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fourthwindow = QtWidgets.QMainWindow()
    ui = Ui_fourthwindow()
    ui.setupUi(fourthwindow)
   # fourthwindow = MyWindow()
    fourthwindow.showFullScreen()
    sys.exit(app.exec_())
