#!/usr/bin/env python2
# coding=UTF-8
#
# Generated by pykdeuic4 from ui/ui_scrGoodbye.ui on Thu May 24 19:14:05 2012
#
# WARNING! All changes to this file will be lost.
from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_goodbyeWidget(object):
    def setupUi(self, goodbyeWidget):
        goodbyeWidget.setObjectName(_fromUtf8("goodbyeWidget"))
        goodbyeWidget.resize(629, 772)
        goodbyeWidget.setStyleSheet(_fromUtf8(""))
        self.gridLayout_5 = QtGui.QGridLayout(goodbyeWidget)
        self.gridLayout_5.setMargin(20)
        self.gridLayout_5.setHorizontalSpacing(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.description = QtGui.QLabel(goodbyeWidget)
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
        self.description.setObjectName(_fromUtf8("description"))
        self.gridLayout_5.addWidget(self.description, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem, 1, 0, 1, 1)
        self.scrollArea = QtGui.QScrollArea(goodbyeWidget)
        self.scrollArea.setStyleSheet(_fromUtf8("#scrollArea {background-color: rgba(0, 0, 0, 0);border: 0px}"))
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 589, 653))
        self.scrollAreaWidgetContents.setStyleSheet(_fromUtf8("#scrollAreaWidgetContents{background-color: rgba(0, 0, 0, 0);}"))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setSpacing(14)
        self.verticalLayout.setMargin(10)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Gothic L"))
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(132, 132, 132, 255), stop:0.501481 rgba(70, 70, 70, 255), stop:0.503057 rgba(62, 62, 62, 255), stop:1 rgba(16, 16, 16, 255));\n"
"/*background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(219, 219, 219, 100), stop:1 rgba(255, 255, 255, 100));*/\n"
"border: 1px solid rgba(255,255,255,50);\n"
"color:white;\n"
"border-top-left-radius: 4px;\n"
"border-top-right-radius: 4px;"))
        self.label.setMargin(5)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.smoltGroupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.smoltGroupBox.setFont(font)
        self.smoltGroupBox.setStyleSheet(_fromUtf8("#smoltGroupBox{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(219, 219, 219, 100), stop:1 rgba(255, 255, 255, 100));\n"
"border: 1px solid rgba(255,255,255,50);\n"
"border-bottom-left-radius: 4px;\n"
"border-bottom-right-radius: 4px;\n"
"}"))
        self.smoltGroupBox.setTitle(_fromUtf8(""))
        self.smoltGroupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.smoltGroupBox.setFlat(True)
        self.smoltGroupBox.setCheckable(False)
        self.smoltGroupBox.setObjectName(_fromUtf8("smoltGroupBox"))
        self.gridLayout = QtGui.QGridLayout(self.smoltGroupBox)
        self.gridLayout.setMargin(10)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem1 = QtGui.QSpacerItem(30, 28, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.buttonSystemSettings_2 = QtGui.QPushButton(self.smoltGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonSystemSettings_2.sizePolicy().hasHeightForWidth())
        self.buttonSystemSettings_2.setSizePolicy(sizePolicy)
        self.buttonSystemSettings_2.setMinimumSize(QtCore.QSize(180, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.buttonSystemSettings_2.setFont(font)
        self.buttonSystemSettings_2.setStyleSheet(_fromUtf8("color: rgb(30, 43, 51)"))
        self.buttonSystemSettings_2.setObjectName(_fromUtf8("buttonSystemSettings_2"))
        self.gridLayout.addWidget(self.buttonSystemSettings_2, 0, 3, 1, 1)
        self.labelSystemSettings_2 = QtGui.QLabel(self.smoltGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSystemSettings_2.sizePolicy().hasHeightForWidth())
        self.labelSystemSettings_2.setSizePolicy(sizePolicy)
        self.labelSystemSettings_2.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        self.labelSystemSettings_2.setFont(font)
        self.labelSystemSettings_2.setStyleSheet(_fromUtf8("color: rgb(30, 43, 51)"))
        self.labelSystemSettings_2.setScaledContents(True)
        self.labelSystemSettings_2.setWordWrap(True)
        self.labelSystemSettings_2.setMargin(0)
        self.labelSystemSettings_2.setIndent(7)
        self.labelSystemSettings_2.setObjectName(_fromUtf8("labelSystemSettings_2"))
        self.gridLayout.addWidget(self.labelSystemSettings_2, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.smoltGroupBox)
        self.label_5.setMinimumSize(QtCore.QSize(64, 64))
        self.label_5.setMaximumSize(QtCore.QSize(64, 64))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8(":/raw/pixmap/view-pim-contacts.png")))
        self.label_5.setScaledContents(False)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.smoltGroupBox)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_3 = QtGui.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Gothic L"))
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(132, 132, 132, 255), stop:0.501481 rgba(70, 70, 70, 255), stop:0.503057 rgba(62, 62, 62, 255), stop:1 rgba(16, 16, 16, 255));\n"
"border: 1px solid rgba(255,255,255,50);\n"
"color:white;\n"
"border-top-left-radius: 4px;\n"
"border-top-right-radius: 4px;"))
        self.label_3.setMargin(5)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_4.addWidget(self.label_3)
        self.groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(_fromUtf8("#groupBox{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(219, 219, 219, 100), stop:1 rgba(255, 255, 255, 100));\n"
"border: 1px solid rgba(255,255,255,50);\n"
"border-bottom-left-radius: 4px;\n"
"border-bottom-right-radius: 4px;\n"
"}"))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setMargin(10)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        spacerItem2 = QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 2, 1, 1)
        self.labelSystemSettings = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSystemSettings.sizePolicy().hasHeightForWidth())
        self.labelSystemSettings.setSizePolicy(sizePolicy)
        self.labelSystemSettings.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        self.labelSystemSettings.setFont(font)
        self.labelSystemSettings.setStyleSheet(_fromUtf8("color: rgb(30, 43, 51)"))
        self.labelSystemSettings.setScaledContents(True)
        self.labelSystemSettings.setWordWrap(True)
        self.labelSystemSettings.setMargin(0)
        self.labelSystemSettings.setIndent(7)
        self.labelSystemSettings.setObjectName(_fromUtf8("labelSystemSettings"))
        self.gridLayout_3.addWidget(self.labelSystemSettings, 0, 1, 1, 1)
        self.buttonSystemSettings = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonSystemSettings.sizePolicy().hasHeightForWidth())
        self.buttonSystemSettings.setSizePolicy(sizePolicy)
        self.buttonSystemSettings.setMinimumSize(QtCore.QSize(180, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.buttonSystemSettings.setFont(font)
        self.buttonSystemSettings.setStyleSheet(_fromUtf8("color: rgb(30, 43, 51)"))
        self.buttonSystemSettings.setObjectName(_fromUtf8("buttonSystemSettings"))
        self.gridLayout_3.addWidget(self.buttonSystemSettings, 0, 3, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setMinimumSize(QtCore.QSize(64, 64))
        self.label_6.setMaximumSize(QtCore.QSize(64, 64))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8(":/raw/pixmap/preferences-system.png")))
        self.label_6.setScaledContents(False)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_4 = QtGui.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Gothic L"))
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(132, 132, 132, 255), stop:0.501481 rgba(70, 70, 70, 255), stop:0.503057 rgba(62, 62, 62, 255), stop:1 rgba(16, 16, 16, 255));\n"
"border: 1px solid rgba(255,255,255,50);\n"
"color:white;\n"
"border-top-left-radius: 4px;\n"
"border-top-right-radius: 4px;"))
        self.label_4.setMargin(5)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_5.addWidget(self.label_4)
        self.groupBox_2 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet(_fromUtf8("#groupBox_2{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(219, 219, 219, 100), stop:1 rgba(255, 255, 255, 100));\n"
"border: 1px solid rgba(255,255,255,50);\n"
"border-bottom-left-radius: 4px;\n"
"border-bottom-right-radius: 4px;\n"
"}"))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setMargin(10)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.labelHelpPages = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelHelpPages.sizePolicy().hasHeightForWidth())
        self.labelHelpPages.setSizePolicy(sizePolicy)
        self.labelHelpPages.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        self.labelHelpPages.setFont(font)
        self.labelHelpPages.setStyleSheet(_fromUtf8("color: rgb(30, 43, 51)"))
        self.labelHelpPages.setScaledContents(True)
        self.labelHelpPages.setWordWrap(True)
        self.labelHelpPages.setMargin(0)
        self.labelHelpPages.setIndent(7)
        self.labelHelpPages.setObjectName(_fromUtf8("labelHelpPages"))
        self.gridLayout_4.addWidget(self.labelHelpPages, 0, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 0, 2, 1, 1)
        self.buttonHelpPages = QtGui.QPushButton(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonHelpPages.sizePolicy().hasHeightForWidth())
        self.buttonHelpPages.setSizePolicy(sizePolicy)
        self.buttonHelpPages.setMinimumSize(QtCore.QSize(180, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.buttonHelpPages.setFont(font)
        self.buttonHelpPages.setStyleSheet(_fromUtf8("color: rgb(30, 43, 51)"))
        self.buttonHelpPages.setObjectName(_fromUtf8("buttonHelpPages"))
        self.gridLayout_4.addWidget(self.buttonHelpPages, 0, 3, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setMinimumSize(QtCore.QSize(64, 64))
        self.label_8.setMaximumSize(QtCore.QSize(64, 64))
        self.label_8.setText(_fromUtf8(""))
        self.label_8.setPixmap(QtGui.QPixmap(_fromUtf8(":/raw/pixmap/system-help.png")))
        self.label_8.setScaledContents(False)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.verticalLayout.addLayout(self.verticalLayout_5)
        spacerItem4 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_5.addWidget(self.scrollArea, 3, 0, 1, 1)

        self.retranslateUi(goodbyeWidget)
        QtCore.QMetaObject.connectSlotsByName(goodbyeWidget)

    def retranslateUi(self, goodbyeWidget):
        goodbyeWidget.setWindowTitle(kdecore.i18n(_fromUtf8("More")))
        self.description.setText(kdecore.i18n(_fromUtf8("<b>Your settings have been applied.</b> Now you can start enjoying Pardus or you can checkout the following links and applications for more settings or for help and support. Don\'t forget to <b>join our community!</b>")))
        self.label.setText(kdecore.i18n(_fromUtf8("My Smolt Page")))
        self.buttonSystemSettings_2.setText(kdecore.i18n(_fromUtf8("My Smolt Page")))
        self.labelSystemSettings_2.setText(kdecore.i18n(_fromUtf8("Go to your Smolt page and rate your hardware components.")))
        self.label_3.setText(kdecore.i18n(_fromUtf8("System Settings")))
        self.labelSystemSettings.setText(kdecore.i18n(_fromUtf8("Configuration tools for Pardus such as the display, firewall, keyboard, user manager...")))
        self.buttonSystemSettings.setText(kdecore.i18n(_fromUtf8("System Settings")))
        self.label_4.setText(kdecore.i18n(_fromUtf8("Help and Support")))
        self.labelHelpPages.setText(kdecore.i18n(_fromUtf8("Pardus community, mailing lists, chat rooms, Wiki documents, help and support pages...")))
        self.buttonHelpPages.setText(kdecore.i18n(_fromUtf8("Help and Support")))

import kaptan.kaptan_rc
