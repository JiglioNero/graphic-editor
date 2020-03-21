# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res/qt/save_as_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_saveAsDialog(object):
    def setupUi(self, saveAsDialog):
        saveAsDialog.setObjectName("saveAsDialog")
        saveAsDialog.resize(367, 194)
        self.verticalLayout = QtWidgets.QVBoxLayout(saveAsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(saveAsDialog)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.formLayout = QtWidgets.QFormLayout(self.widget_3)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.widthImg = QtWidgets.QLineEdit(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widthImg.sizePolicy().hasHeightForWidth())
        self.widthImg.setSizePolicy(sizePolicy)
        self.widthImg.setObjectName("widthImg")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.widthImg)
        self.heightLine = QtWidgets.QLineEdit(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.heightLine.sizePolicy().hasHeightForWidth())
        self.heightLine.setSizePolicy(sizePolicy)
        self.heightLine.setObjectName("heightLine")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.heightLine)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.filePath = QtWidgets.QLineEdit(self.widget_2)
        self.filePath.setObjectName("filePath")
        self.horizontalLayout.addWidget(self.filePath)
        self.fileBrowseButton = QtWidgets.QPushButton(self.widget_2)
        self.fileBrowseButton.setObjectName("fileBrowseButton")
        self.horizontalLayout.addWidget(self.fileBrowseButton)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.verticalLayout.addWidget(self.widget)
        self.buttonBox = QtWidgets.QDialogButtonBox(saveAsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(saveAsDialog)
        self.buttonBox.accepted.connect(saveAsDialog.accept)
        self.buttonBox.rejected.connect(saveAsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(saveAsDialog)

    def retranslateUi(self, saveAsDialog):
        _translate = QtCore.QCoreApplication.translate
        saveAsDialog.setWindowTitle(_translate("saveAsDialog", "Save as..."))
        self.label_2.setText(_translate("saveAsDialog", "Width:"))
        self.label_3.setText(_translate("saveAsDialog", "Height:"))
        self.label.setText(_translate("saveAsDialog", "Save to:"))
        self.fileBrowseButton.setText(_translate("saveAsDialog", "Browse"))

