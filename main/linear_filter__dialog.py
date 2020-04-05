# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res/qt/linear_filter_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog


class FilterDialog(QDialog):
    def __init__(self, value):
        super().__init__()
        self.value = value
        self.ui = Ui_linearFilterDialog(self.value)
        self.ui.setupUi(self)

    def getValue(self):
        return self.ui.strength


class Ui_linearFilterDialog(object):
    def __init__(self, value):
        self.strength = value

    def setupUi(self, linearFilterDialog):
        linearFilterDialog.setObjectName("linearFilterDialog")
        linearFilterDialog.resize(366, 86)
        self.verticalLayout = QtWidgets.QVBoxLayout(linearFilterDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(linearFilterDialog)
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QVBoxLayout(self.widget)
        self.formLayout.setObjectName("formLayout")

        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.formLayout.addWidget(self.label)

        self.strengthSlider = QtWidgets.QSlider(self.widget)
        self.strengthSlider.setMaximum(10)
        self.strengthSlider.setPageStep(1)
        self.strengthSlider.setOrientation(QtCore.Qt.Horizontal)
        self.strengthSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.strengthSlider.setTickInterval(1)
        self.strengthSlider.setObjectName("sigmaSlider")
        self.strengthSlider.setValue(self.strength)
        self.strengthSlider.valueChanged.connect(self.onStrengthChange)
        self.formLayout.addWidget(self.strengthSlider)

        self.verticalLayout.addWidget(self.widget)
        self.buttonBox = QtWidgets.QDialogButtonBox(linearFilterDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(linearFilterDialog)
        self.buttonBox.accepted.connect(linearFilterDialog.accept)
        self.buttonBox.rejected.connect(linearFilterDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(linearFilterDialog)

    def onStrengthChange(self):
        self.strength = self.strengthSlider.value()

    def retranslateUi(self, linearFilterDialog):
        _translate = QtCore.QCoreApplication.translate
        linearFilterDialog.setWindowTitle(_translate("linearFilterDialog", "Add linear filter"))
        self.label.setText(_translate("linearFilterDialog", "Strength:"))
