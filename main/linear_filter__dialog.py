# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res/qt/linear_filter_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_linearFilterDialog(object):
    def setupUi(self, linearFilterDialog):
        linearFilterDialog.setObjectName("linearFilterDialog")
        linearFilterDialog.resize(366, 86)
        self.verticalLayout = QtWidgets.QVBoxLayout(linearFilterDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(linearFilterDialog)
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.sigmaSlider = QtWidgets.QSlider(self.widget)
        self.sigmaSlider.setMaximum(10)
        self.sigmaSlider.setPageStep(1)
        self.sigmaSlider.setOrientation(QtCore.Qt.Horizontal)
        self.sigmaSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.sigmaSlider.setTickInterval(1)
        self.sigmaSlider.setObjectName("sigmaSlider")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sigmaSlider)
        self.verticalLayout.addWidget(self.widget)
        self.buttonBox = QtWidgets.QDialogButtonBox(linearFilterDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(linearFilterDialog)
        self.buttonBox.accepted.connect(linearFilterDialog.accept)
        self.buttonBox.rejected.connect(linearFilterDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(linearFilterDialog)

    def retranslateUi(self, linearFilterDialog):
        _translate = QtCore.QCoreApplication.translate
        linearFilterDialog.setWindowTitle(_translate("linearFilterDialog", "Add linear filter"))
        self.label.setText(_translate("linearFilterDialog", "Sigma:"))

