# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res/qt/Graphic_editor.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import cv2
import numpy as np
from PIL import ImageFilter
from PIL.ImageFilter import BoxBlur
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QDialog, QFileDialog, QGraphicsScene
from save_as_dialog import *
from linear_filter__dialog import *
from imager import histogramm as hist_util, noisey
import copy


class Ui_MainWindow(object):
    def __init__(self, main_window):
        self.img_pixmap = None
        self.img_pixmap_orig = None
        self.linearFilterValue = 5
        self.main_window = main_window

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 668)
        self.mainWidget = QtWidgets.QWidget(MainWindow)
        self.mainWidget.setObjectName("mainWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.mainWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.workSpaceWidget = QtWidgets.QWidget(self.mainWidget)
        self.workSpaceWidget.setObjectName("workSpaceWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.workSpaceWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftWidget = QtWidgets.QWidget(self.workSpaceWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftWidget.sizePolicy().hasHeightForWidth())
        self.leftWidget.setSizePolicy(sizePolicy)
        self.leftWidget.setMinimumSize(QtCore.QSize(50, 0))
        self.leftWidget.setMaximumSize(QtCore.QSize(50, 16777215))
        self.leftWidget.setObjectName("leftWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.leftWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(6, 6, -1, 6)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        """
        self.actionGroup = QtWidgets.QButtonGroup(self.main_window)
        self.actionGroup.setExclusive(True)
        self.ArrowTool = QtWidgets.QToolButton(self.leftWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/arrow.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ArrowTool.setIcon(icon)
        self.ArrowTool.setObjectName("ArrowTool")
        self.ArrowTool.setCheckable(True)
        self.ArrowTool.setChecked(True)
        self.actionGroup.addButton(self.ArrowTool)
        self.verticalLayout.addWidget(self.ArrowTool)
        self.HandTool = QtWidgets.QToolButton(self.leftWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/hand.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.HandTool.setIcon(icon1)
        self.HandTool.setObjectName("HandTool")
        self.HandTool.setCheckable(True)
        self.actionGroup.addButton(self.HandTool)
        self.verticalLayout.addWidget(self.HandTool)
        self.blurTool = QtWidgets.QToolButton(self.leftWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/blur.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.blurTool.setIcon(icon2)
        self.blurTool.setObjectName("blurTool")
        self.blurTool.setCheckable(True)
        self.actionGroup.addButton(self.blurTool)
    
    """
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.leftWidget)
        self.centralWidget = QtWidgets.QWidget(self.workSpaceWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setMinimumSize(QtCore.QSize(200, 200))
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.mainView = QtWidgets.QGraphicsView(self.centralWidget)
        self.mainView.setObjectName("mainView")
        self.mainView.setMouseTracking(True)
        self.mainView.wheelEvent = self.wheelEvent
        self.gridLayout.addWidget(self.mainView, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.centralWidget)
        self.rightWidget = QtWidgets.QWidget(self.workSpaceWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightWidget.sizePolicy().hasHeightForWidth())
        self.rightWidget.setSizePolicy(sizePolicy)
        self.rightWidget.setMinimumSize(QtCore.QSize(50, 0))
        self.rightWidget.setMaximumSize(QtCore.QSize(150, 16777215))
        self.rightWidget.setObjectName("rightWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.rightWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.rightWidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(5)
        self.line.setMidLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)

        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.noiseSlider = QtWidgets.QLineEdit(self.groupBox)
        self.noiseSlider.setObjectName("noiseSlider")
        self.noiseSlider.editingFinished.connect(self.onNoiseSliderValueChange)
        self.verticalLayout_4.addWidget(self.noiseSlider)

        self.label1 = QtWidgets.QLabel(self.groupBox)
        self.label1.setObjectName("label1")
        self.verticalLayout_4.addWidget(self.label1)
        self.blurRadius = QtWidgets.QLineEdit(self.groupBox)
        self.blurRadius.setObjectName("blurRadius")
        self.blurRadius.editingFinished.connect(self.blurImage)
        self.verticalLayout_4.addWidget(self.blurRadius)

        self.label2 = QtWidgets.QLabel(self.groupBox)
        self.label2.setObjectName("label2")
        self.verticalLayout_4.addWidget(self.label2)
        self.rotateDegree = QtWidgets.QLineEdit(self.groupBox)
        self.rotateDegree.setObjectName("rotateDegree")
        self.rotateDegree.editingFinished.connect(self.rotateImage)
        self.verticalLayout_4.addWidget(self.rotateDegree)

        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.horizontalLayout.addWidget(self.rightWidget)
        self.verticalLayout_2.addWidget(self.workSpaceWidget)
        self.monitorWidget = QtWidgets.QWidget(self.mainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.monitorWidget.sizePolicy().hasHeightForWidth())
        self.monitorWidget.setSizePolicy(sizePolicy)
        self.monitorWidget.setMinimumSize(QtCore.QSize(0, 100))
        self.monitorWidget.setMaximumSize(QtCore.QSize(16777215, 200))
        self.monitorWidget.setObjectName("monitorWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.monitorWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.monitorWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.histogramTab = QtWidgets.QWidget()
        self.histogramTab.setObjectName("histogramTab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.histogramTab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.histogram = QtWidgets.QLabel(self.histogramTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.histogram.sizePolicy().hasHeightForWidth())
        self.histogram.setSizePolicy(sizePolicy)
        self.histogram.setMinimumSize(QtCore.QSize(100, 100))
        self.histogram.setMaximumSize(QtCore.QSize(200, 200))
        self.histogram.setSizeIncrement(QtCore.QSize(0, 0))
        self.histogram.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.histogram.setFrameShadow(QtWidgets.QFrame.Raised)
        self.histogram.setObjectName("histogram")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.histogram)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3.addWidget(self.histogram)
        self.groupBox_2 = QtWidgets.QGroupBox(self.histogramTab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.pixelCount = QtWidgets.QLabel(self.groupBox_2)
        self.pixelCount.setText("")
        self.pixelCount.setObjectName("pixelCount")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pixelCount)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.tabWidget.addTab(self.histogramTab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout_2.addWidget(self.monitorWidget)
        MainWindow.setCentralWidget(self.mainWidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 29))
        self.menubar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.menubar.setAutoFillBackground(False)
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menu_Filters = QtWidgets.QMenu(self.menuTools)
        self.menu_Filters.setObjectName("menu_Filters")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_image = QtWidgets.QAction(MainWindow, triggered=self.openOpenImageDialog)
        self.actionOpen_image.setObjectName("actionOpen_image")
        self.actionSave = QtWidgets.QAction(MainWindow, triggered=self.save)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.setEnabled(False)
        self.actionSave_as = QtWidgets.QAction(MainWindow, triggered=self.openSaveAsDialog)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionSave_as.setEnabled(False)
        self.actionLinear = QtWidgets.QAction(MainWindow, triggered=self.openLinearFilterDialog)
        self.actionLinear.setObjectName("actionLinear")
        self.menuFile.addAction(self.actionOpen_image)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menu_Filters.addAction(self.actionLinear)
        self.menuTools.addAction(self.menu_Filters.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        """self.ArrowTool.setText(_translate("MainWindow", "..."))
        self.HandTool.setText(_translate("MainWindow", "..."))
        self.blurTool.setText(_translate("MainWindow", "..."))"""
        self.groupBox.setTitle(_translate("MainWindow", "Graphic tools"))
        self.label.setText(_translate("MainWindow", "Noise factor:"))
        self.label1.setText(_translate("MainWindow", "Blur radius:"))
        self.label2.setText(_translate("MainWindow", "Rotate degree:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Parameters"))
        self.label_2.setText(_translate("MainWindow", "Pixel count:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.histogramTab), _translate("MainWindow", "Histogram"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menuTools.setTitle(_translate("MainWindow", "&Tools"))
        self.menu_Filters.setTitle(_translate("MainWindow", "&Filters"))
        self.actionOpen_image.setText(_translate("MainWindow", "&Open image"))
        self.actionSave.setText(_translate("MainWindow", "&Save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save &as.."))
        self.actionLinear.setText(_translate("MainWindow", "&Linear"))

    def openSaveAsDialog(self):
        dialog = QDialog()
        dialog.ui = Ui_saveAsDialog(self.filePath, self.img_pixmap)
        dialog.ui.setupUi(dialog)
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dialog.exec_()

    def save(self, path=None):
        if path:
            self.img_pixmap.save(path)
        else:
            self.img_pixmap.save(self.filePath)

    def openOpenImageDialog(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter("(*.png *.xpm *.jpeg *.jpg)")

        if dialog.exec():
            self.filePath = dialog.selectedFiles()[0]
            self.img_pixmap = QtGui.QPixmap(self.filePath)
            self.img_pixmap_orig = QtGui.QPixmap(self.filePath)
            self.notifyImageChange()
            if self.img_pixmap and self.img_pixmap_orig:
                self.actionSave_as.setEnabled(True)
                self.actionSave.setEnabled(True)

    def wheelEvent(self, event):
        zoom = 1 + event.angleDelta().y() / 2880
        self.mainView.scale(zoom, zoom)

    def rotateImage(self):
        text = self.rotateDegree.text()
        if text and text.isnumeric() and self.img_pixmap:
            tmp = Image.fromqpixmap(self.img_pixmap).rotate(int(self.rotateDegree.text()))
            self.img_pixmap = tmp.toqpixmap()
            self.notifyImageChange()

    def openLinearFilterDialog(self):
        dialog = FilterDialog(self.linearFilterValue)
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        if dialog.exec_():
            self.linearFilterValue = dialog.getValue()
            strength = self.linearFilterValue

            kernel_motion_blur = cv2.getGaussianKernel(11, 1.5)
            kernel_motion_blur *= strength/5
            window = np.outer(kernel_motion_blur, kernel_motion_blur.transpose())

            path = "tmp.png"
            self.save(path)

            out = cv2.filter2D(cv2.imread(path), -1, window)
            self.img_pixmap = Image.fromarray(out).toqpixmap()
            self.notifyImageChange()

    def drawHistogram(self):
        hist, pixel_count = hist_util.getRGBhist(Image.fromqpixmap(self.img_pixmap))
        hist_pixmap = hist.toqpixmap()
        hist_pixmap = hist_pixmap.scaledToHeight(self.histogram.frameGeometry().height())
        self.pixelCount.setText(str(pixel_count))
        self.histogram.setPixmap(hist_pixmap)

    def blurImage(self):
        text = self.blurRadius.text()
        if text and text.isnumeric() and self.img_pixmap:
            radius = int(text)
            if radius == 0:
                self.img_pixmap = self.img_pixmap_orig
            else:
                img = Image.fromqpixmap(self.img_pixmap)
                img = img.filter(ImageFilter.BoxBlur(radius))
                self.img_pixmap = img.toqpixmap()
            self.notifyImageChange()

    def onNoiseSliderValueChange(self):
        self.addNoiseToImg()

    def addNoiseToImg(self):
        text = self.noiseSlider.text()
        if text and text.isnumeric() and self.img_pixmap:
            if int(text) > 0:
                self.img_pixmap = noisey.addNoise(int(self.noiseSlider.text()),
                                                  Image.fromqpixmap(self.img_pixmap)).toqpixmap()
            else:
                self.img_pixmap = self.img_pixmap_orig.copy()
            self.notifyImageChange()

    def notifyImageChange(self):
        scene = QGraphicsScene()
        scene.addPixmap(self.img_pixmap)
        self.mainView.setScene(scene)
        self.drawHistogram()


import resources
