# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIFiles/MainForm.ui',
# licensing of 'UIFiles/MainForm.ui' applies.
#
# Created: Wed Feb  6 16:48:14 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(400, 220)
        self.input1_line = QtWidgets.QLineEdit(MainForm)
        self.input1_line.setGeometry(QtCore.QRect(8, 78, 381, 27))
        self.input1_line.setObjectName("input1_line")
        self.input2_line = QtWidgets.QLineEdit(MainForm)
        self.input2_line.setGeometry(QtCore.QRect(8, 126, 381, 27))
        self.input2_line.setObjectName("input2_line")
        self.result_line = QtWidgets.QLineEdit(MainForm)
        self.result_line.setGeometry(QtCore.QRect(8, 188, 381, 27))
        self.result_line.setReadOnly(True)
        self.result_line.setObjectName("result_line")
        self.label = QtWidgets.QLabel(MainForm)
        self.label.setGeometry(QtCore.QRect(171, 106, 54, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.solve_button = QtWidgets.QPushButton(MainForm)
        self.solve_button.setGeometry(QtCore.QRect(8, 157, 381, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.solve_button.setFont(font)
        self.solve_button.setObjectName("solve_button")
        self.groupBox = QtWidgets.QGroupBox(MainForm)
        self.groupBox.setGeometry(QtCore.QRect(10, 2, 381, 71))
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.radio_elementwise = QtWidgets.QRadioButton(self.groupBox)
        self.radio_elementwise.setGeometry(QtCore.QRect(10, 23, 131, 22))
        self.radio_elementwise.setChecked(True)
        self.radio_elementwise.setObjectName("radio_elementwise")
        self.radio_vector = QtWidgets.QRadioButton(self.groupBox)
        self.radio_vector.setGeometry(QtCore.QRect(10, 43, 131, 22))
        self.radio_vector.setChecked(False)
        self.radio_vector.setObjectName("radio_vector")

        self.retranslateUi(MainForm)
        QtCore.QObject.connect(self.input1_line, QtCore.SIGNAL("returnPressed()"), self.solve_button.click)
        QtCore.QObject.connect(self.input2_line, QtCore.SIGNAL("returnPressed()"), self.solve_button.click)
        QtCore.QMetaObject.connectSlotsByName(MainForm)
        MainForm.setTabOrder(self.radio_elementwise, self.radio_vector)
        MainForm.setTabOrder(self.radio_vector, self.input1_line)
        MainForm.setTabOrder(self.input1_line, self.input2_line)
        MainForm.setTabOrder(self.input2_line, self.solve_button)
        MainForm.setTabOrder(self.solve_button, self.result_line)

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(QtWidgets.QApplication.translate("MainForm", "Vectors multiplication", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainForm", "x", None, -1))
        self.solve_button.setText(QtWidgets.QApplication.translate("MainForm", "=", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainForm", "Тип умножения", None, -1))
        self.radio_elementwise.setText(QtWidgets.QApplication.translate("MainForm", "Поэлементное", None, -1))
        self.radio_vector.setText(QtWidgets.QApplication.translate("MainForm", "Векторное", None, -1))

