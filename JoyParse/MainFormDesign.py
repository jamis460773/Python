# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\JoyParse\MainFormDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        MainWindow.setMaximumSize(QtCore.QSize(400, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\JoyParse\\Tux.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 381, 31))
        self.label.setTextFormat(QtCore.Qt.MarkdownText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.lineEdit_PagesQty = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_PagesQty.setGeometry(QtCore.QRect(220, 50, 171, 21))
        self.lineEdit_PagesQty.setObjectName("lineEdit_PagesQty")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 211, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 111, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit_StartUrl = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_StartUrl.setGeometry(QtCore.QRect(120, 80, 271, 21))
        self.lineEdit_StartUrl.setObjectName("lineEdit_StartUrl")
        self.pushButton_Run = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Run.setGeometry(QtCore.QRect(170, 230, 75, 23))
        self.pushButton_Run.setAutoDefault(False)
        self.pushButton_Run.setDefault(False)
        self.pushButton_Run.setObjectName("pushButton_Run")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(40, 190, 351, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_About = QtWidgets.QAction(MainWindow)
        self.action_About.setObjectName("action_About")
        self.menu.addAction(self.action_About)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Парсер Joyreactor"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Привет! В разработке...</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Укажите кол-во страниц для обработки</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>Стартовая страница</p></body></html>"))
        self.pushButton_Run.setText(_translate("MainWindow", "Запуск"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.action_About.setText(_translate("MainWindow", "О программе"))
