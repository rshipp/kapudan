#!/usr/bin/env python2
# coding=UTF-8
#
# Generated by pykdeuic4 from ui/ui_scrAvatar.ui on Thu May 24 19:14:09 2012
#
# WARNING! All changes to this file will be lost.
from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(858, 633)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setMargin(20)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(64, 64))
        self.label_2.setMaximumSize(QtCore.QSize(64, 64))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/raw/pixmap/preferences-desktop-personal.png")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.description = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.description.sizePolicy().hasHeightForWidth())
        self.description.setSizePolicy(sizePolicy)
        self.description.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        self.description.setFont(font)
        self.description.setStyleSheet(_fromUtf8(""))
        self.description.setWordWrap(True)
        self.description.setIndent(10)
        self.description.setObjectName(_fromUtf8("description"))
        self.gridLayout.addWidget(self.description, 0, 1, 1, 1)
        self.scrollArea = QtGui.QScrollArea(Form)
        self.scrollArea.setStyleSheet(_fromUtf8("#scrollAreaWidgetContents {\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"\n"
"#scrollArea{\n"
"    border: 0px;\n"
"    background-color: rgba(0,0,0,0);\n"
"}"))
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 818, 525))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox_3 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QtCore.QSize(450, 0))
        self.groupBox_3.setMaximumSize(QtCore.QSize(450, 16777215))
        self.groupBox_3.setStyleSheet(_fromUtf8("#groupBox_3{\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(132, 132, 132, 255), stop:0.501481 rgba(70, 70, 70, 255), stop:0.503057 rgba(62, 62, 62, 255), stop:1 rgba(16, 16, 16, 255));\n"
"/*\n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(26, 38, 45, 255), stop:0.398093 rgba(51, 72, 91, 255), stop:0.521739 rgba(45, 76, 94, 255), stop:0.531585 rgba(49, 84, 106, 255), stop:0.983696 rgba(99, 141, 164, 255), stop:1 rgba(120, 146, 172, 255));*/\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    padding: 3px 10px 3px 10px;\n"
"    color: white;\n"
"    border:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(132, 132, 132, 255), stop:0.501481 rgba(70, 70, 70, 255), stop:0.503057 rgba(62, 62, 62, 255), stop:1 rgba(16, 16, 16, 255));\n"
"    /*background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(120, 146, 172, 255), stop:0.0155729 rgba(99, 141, 164, 255), stop:0.538376 rgba(49, 84, 106, 255), stop:1 rgba(51, 72, 91, 255))*/\n"
"}\n"
"\n"
"QPushButton::flat:hover{\n"
"    border:1px solid  rgba(34, 49, 60, 100);\n"
"    border-radius:2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(129, 3, 3, 255), stop:0.0192308 rgba(160, 35, 25, 255), stop:0.521739 rgba(166, 35, 29, 255), stop:0.531585 rgba(184, 46, 40, 255), stop:0.983696 rgba(168, 78, 74, 255), stop:1 rgba(210, 110, 110, 255))\n"
"}\n"
"\n"
"QPushButton::flat{\n"
"    border:1px solid  rgba(34, 49, 60, 100);\n"
"    border-radius:2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(132, 132, 132, 255), stop:0.501481 rgba(70, 70, 70, 255), stop:0.503057 rgba(62, 62, 62, 255), stop:1 rgba(16, 16, 16, 255));\n"
"    /*\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(26, 38, 45, 150), stop:0.398093 rgba(44, 62, 79, 255), stop:0.521739 rgba(36, 61, 76, 255), stop:0.531585 rgba(40, 68, 86, 255), stop:0.983696 rgba(73, 109, 129, 255), stop:1 rgba(89, 108, 127, 255))\n"
"    */\n"
"}\n"
"\n"
"QPushButton::flat:pressed{\n"
"    border:1px solid  rgba(34, 49, 60, 100);\n"
"    border-radius:2px;\n"
"    padding: 3px 10px 3px 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(129, 3, 3, 255), stop:0.0192308 rgba(160, 35, 25, 255), stop:0.521739 rgba(166, 35, 29, 255), stop:0.531585 rgba(184, 46, 40, 255), stop:0.983696 rgba(168, 78, 74, 255), stop:1 rgba(210, 110, 110, 255))\n"
"}\n"
"/* ====================================== */\n"
"\n"
" QComboBox {\n"
"     border:1px solid  rgba(34, 49, 60, 100);\n"
"     border-radius:2px;\n"
"     padding: 1px 18px 1px 3px;\n"
"     min-width: 6em;\n"
"     color: white;\n"
" }\n"
"\n"
" QComboBox:editable {\n"
"     background: white;\n"
" }\n"
"\n"
" QComboBox:!editable, QComboBox::drop-down:editable {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(132, 132, 132, 255), stop:0.501481 rgba(70, 70, 70, 255), stop:0.503057 rgba(62, 62, 62, 255), stop:1 rgba(16, 16, 16, 255));\n"
" }\n"
"\n"
" /* QComboBox gets the \"on\" state when the popup is open */\n"
" QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(129, 3, 3, 255), stop:0.0192308 rgba(160, 35, 25, 255), stop:0.521739 rgba(166, 35, 29, 255), stop:0.531585 rgba(184, 46, 40, 255), stop:0.983696 rgba(168, 78, 74, 255), stop:1 rgba(210, 110, 110, 255));\n"
" }\n"
"\n"
" QComboBox:on { /* shift the text when the popup opens */\n"
"     padding-top: 3px;\n"
"     padding-left: 4px;\n"
" }\n"
"\n"
" QComboBox::drop-down {\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 20px;\n"
"     border:0px solid  rgba(34, 49, 60, 100);\n"
" }\n"
"\n"
" QComboBox::down-arrow {\n"
"    image: url(:/raw/pixmap/white-arrow-down.gif);\n"
"     /*image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);*/\n"
" }\n"
"\n"
" QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"     top: 1px;\n"
"     left: 1px;\n"
" }"))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setMargin(4)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.comboBox = QtGui.QComboBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(113, 24))
        self.comboBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.comboBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox.setToolTip(_fromUtf8(""))
        self.comboBox.setEditable(False)
        self.comboBox.setMaxVisibleItems(10)
        self.comboBox.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox.setFrame(True)
        self.comboBox.setModelColumn(0)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.comboBox, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        self.takeButton = QtGui.QPushButton(self.groupBox_3)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/raw/pixmap/webcamreceive.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.takeButton.setIcon(icon)
        self.takeButton.setDefault(True)
        self.takeButton.setFlat(True)
        self.takeButton.setObjectName(_fromUtf8("takeButton"))
        self.gridLayout_3.addWidget(self.takeButton, 0, 2, 1, 1)
        self.takeAgainButton = QtGui.QPushButton(self.groupBox_3)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/raw/pixmap/view-refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.takeAgainButton.setIcon(icon1)
        self.takeAgainButton.setFlat(True)
        self.takeAgainButton.setObjectName(_fromUtf8("takeAgainButton"))
        self.gridLayout_3.addWidget(self.takeAgainButton, 0, 3, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(450, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(450, 16777215))
        self.groupBox.setStyleSheet(_fromUtf8("/*QGroupBox{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 81), stop:0.00537634 rgba(95, 34, 52, 80), stop:1 rgba(255, 213, 230, 80));\n"
"\n"
"border: 1px solid rgb(236, 236, 236, 80);\n"
"\n"
"color: rgb(234, 225, 228);\n"
"}*/\n"
"#groupBox{\n"
"margin:0px;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(219, 219, 219, 100), stop:1 rgba(255, 255, 255, 100));\n"
"border: 1px solid rgba(255,255,255,50);\n"
"border-bottom-left-radius: 4px;\n"
"border-bottom-right-radius: 4px;\n"
"}"))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setMargin(10)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.camGoruntu = QtGui.QLabel(self.groupBox)
        self.camGoruntu.setMinimumSize(QtCore.QSize(320, 240))
        self.camGoruntu.setMaximumSize(QtCore.QSize(320, 240))
        self.camGoruntu.setStyleSheet(_fromUtf8("background-color: #222222;\n"
"border: 4px solid gray;"))
        self.camGoruntu.setText(_fromUtf8(""))
        self.camGoruntu.setObjectName(_fromUtf8("camGoruntu"))
        self.horizontalLayout_2.addWidget(self.camGoruntu)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 2)

        self.retranslateUi(Form)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(kdecore.i18n(_fromUtf8("Form")))
        self.description.setText(kdecore.i18n(_fromUtf8("This screen helps you set your <b>user picture</b>. You can either choose an image from a file or you can capture an image from your camera. Select an option from the <b>options</b> menu.")))
        self.comboBox.setItemText(0, kdecore.i18n(_fromUtf8("Options")))
        self.comboBox.setItemText(1, kdecore.i18n(_fromUtf8("Choose an image")))
        self.takeButton.setText(kdecore.i18n(_fromUtf8("Capture")))
        self.takeAgainButton.setText(kdecore.i18n(_fromUtf8("Recapture")))

import kaptan.kaptan_rc
