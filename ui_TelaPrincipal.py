# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Python\pjt_agenda\TelaPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(500, 300)
        mainWindow.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnCadUser = QtWidgets.QPushButton(self.centralwidget)
        self.btnCadUser.setGeometry(QtCore.QRect(80, 30, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.btnCadUser.setFont(font)
        self.btnCadUser.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.btnCadUser.setObjectName("btnCadUser")
        self.btnCadPessoa = QtWidgets.QPushButton(self.centralwidget)
        self.btnCadPessoa.setGeometry(QtCore.QRect(80, 120, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.btnCadPessoa.setFont(font)
        self.btnCadPessoa.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 127);")
        self.btnCadPessoa.setObjectName("btnCadPessoa")
        self.btnVoltar = QtWidgets.QPushButton(self.centralwidget)
        self.btnVoltar.setGeometry(QtCore.QRect(260, 210, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.btnVoltar.setFont(font)
        self.btnVoltar.setObjectName("btnVoltar")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Tela Principal"))
        self.btnCadUser.setText(_translate("mainWindow", "Cadastro de Usu??rio"))
        self.btnCadPessoa.setText(_translate("mainWindow", "Cadastro de Pessoas"))
        self.btnVoltar.setText(_translate("mainWindow", "VOLTAR"))
