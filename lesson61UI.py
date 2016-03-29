# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Code\Python\lesson61.ui'
#
# Created: Mon Mar 28 11:27:29 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 801, 551))
        self.graphicsView.setObjectName("graphicsView")
        self.calendarWidget = QtGui.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(30, 20, 361, 231))
        self.calendarWidget.setObjectName("calendarWidget")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(410, 40, 111, 31))
        self.label.setObjectName("label")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 280, 111, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 330, 121, 51))
        self.label_4.setObjectName("label_4")
        self.CurrentPlace = QtGui.QLineEdit(self.centralwidget)
        self.CurrentPlace.setGeometry(QtCore.QRect(110, 290, 91, 21))
        self.CurrentPlace.setObjectName("CurrentPlace")
        self.CurrentTime = QtGui.QLCDNumber(self.centralwidget)
        self.CurrentTime.setGeometry(QtCore.QRect(450, 30, 91, 41))
        self.CurrentTime.setObjectName("CurrentTime")
        self.CurrentPlaceButton = QtGui.QPushButton(self.centralwidget)
        self.CurrentPlaceButton.setGeometry(QtCore.QRect(240, 290, 75, 23))
        self.CurrentPlaceButton.setObjectName("CurrentPlaceButton")
        self.CurrentWeather = QtGui.QTextBrowser(self.centralwidget)
        self.CurrentWeather.setGeometry(QtCore.QRect(80, 370, 271, 121))
        self.CurrentWeather.setObjectName("CurrentWeather")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuStart = QtGui.QMenu(self.menubar)
        self.menuStart.setObjectName("menuStart")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuStart.addAction(self.actionOpen)
        self.menuStart.addAction(self.actionExit)
        self.menubar.addAction(self.menuStart.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "时间：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "地点：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "当前天气：", None, QtGui.QApplication.UnicodeUTF8))
        self.CurrentPlaceButton.setText(QtGui.QApplication.translate("MainWindow", "确认", None, QtGui.QApplication.UnicodeUTF8))
        self.menuStart.setTitle(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))

