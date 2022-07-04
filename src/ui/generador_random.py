# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'generador_random.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NumeroRandom(object):
    def setupUi(self, NumeroRandom):
        NumeroRandom.setObjectName("NumeroRandom")
        NumeroRandom.resize(300, 200)
        NumeroRandom.setMinimumSize(QtCore.QSize(300, 200))
        self.centralwidget = QtWidgets.QWidget(NumeroRandom)
        self.centralwidget.setObjectName("centralwidget")
        self.label_inferior = QtWidgets.QLabel(self.centralwidget)
        self.label_inferior.setGeometry(QtCore.QRect(10, 30, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_inferior.setFont(font)
        self.label_inferior.setObjectName("label_inferior")
        self.spinBox_inferior = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_inferior.setGeometry(QtCore.QRect(110, 20, 171, 31))
        self.spinBox_inferior.setMinimum(-99999)
        self.spinBox_inferior.setMaximum(99999)
        self.spinBox_inferior.setObjectName("spinBox_inferior")
        self.label_superior = QtWidgets.QLabel(self.centralwidget)
        self.label_superior.setGeometry(QtCore.QRect(10, 80, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_superior.setFont(font)
        self.label_superior.setObjectName("label_superior")
        self.spinBox_superior = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_superior.setGeometry(QtCore.QRect(110, 75, 171, 31))
        self.spinBox_superior.setMinimum(-99999)
        self.spinBox_superior.setMaximum(99999)
        self.spinBox_superior.setProperty("value", 10)
        self.spinBox_superior.setObjectName("spinBox_superior")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 120, 291, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.genera_button = QtWidgets.QPushButton(self.centralwidget)
        self.genera_button.setGeometry(QtCore.QRect(10, 150, 89, 25))
        self.genera_button.setAutoDefault(False)
        self.genera_button.setDefault(False)
        self.genera_button.setFlat(False)
        self.genera_button.setObjectName("genera_button")
        self.label_respuesta = QtWidgets.QLabel(self.centralwidget)
        self.label_respuesta.setGeometry(QtCore.QRect(120, 150, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_respuesta.setFont(font)
        self.label_respuesta.setText("")
        self.label_respuesta.setObjectName("label_respuesta")
        NumeroRandom.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(NumeroRandom)
        self.statusbar.setObjectName("statusbar")
        NumeroRandom.setStatusBar(self.statusbar)

        self.retranslateUi(NumeroRandom)
        QtCore.QMetaObject.connectSlotsByName(NumeroRandom)

    def retranslateUi(self, NumeroRandom):
        _translate = QtCore.QCoreApplication.translate
        NumeroRandom.setWindowTitle(_translate("NumeroRandom", "Generador Random"))
        self.label_inferior.setText(_translate("NumeroRandom", "Lím. Inferior"))
        self.label_superior.setText(_translate("NumeroRandom", "Lím. Superior"))
        self.genera_button.setText(_translate("NumeroRandom", "Genera"))
        self.genera_button.setShortcut(_translate("NumeroRandom", "Return"))
