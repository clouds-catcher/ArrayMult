# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIFiles/MainForm.ui',
# licensing of 'UIFiles/MainForm.ui' applies.
#
# Created: Tue Feb  5 18:48:47 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(400, 175)
        self.input1_line = QtWidgets.QLineEdit(MainForm)
        self.input1_line.setGeometry(QtCore.QRect(8, 20, 381, 27))
        self.input1_line.setObjectName("input1_line")
        self.input2_line = QtWidgets.QLineEdit(MainForm)
        self.input2_line.setGeometry(QtCore.QRect(8, 68, 381, 27))
        self.input2_line.setObjectName("input2_line")
        self.result_line = QtWidgets.QLineEdit(MainForm)
        self.result_line.setGeometry(QtCore.QRect(8, 130, 381, 27))
        self.result_line.setObjectName("result_line")
        self.label = QtWidgets.QLabel(MainForm)
        self.label.setGeometry(QtCore.QRect(171, 48, 54, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.solve_button = QtWidgets.QPushButton(MainForm)
        self.solve_button.setGeometry(QtCore.QRect(155, 99, 85, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.solve_button.setFont(font)
        self.solve_button.setObjectName("solve_button")

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(QtWidgets.QApplication.translate("MainForm", "Vectors multiplication", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainForm", "x", None, -1))
        self.solve_button.setText(QtWidgets.QApplication.translate("MainForm", "=", None, -1))

