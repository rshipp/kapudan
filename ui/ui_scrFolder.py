#!/usr/bin/env python2
# coding=UTF-8
#
# Generated by pykdeuic4 from ui/ui_scrFolder.ui on Wed Aug  1 19:19:33 2012
#
# WARNING! All changes to this file will be lost.
from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_folderWidget(object):
    def setupUi(self, folderWidget):
        folderWidget.setObjectName(_fromUtf8("folderWidget"))
        folderWidget.resize(577, 505)
        folderWidget.setStyleSheet(_fromUtf8(""))
        self.gridLayout = QtGui.QGridLayout(folderWidget)
        self.gridLayout.setMargin(20)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBoxFolders = QtGui.QGroupBox(folderWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxFolders.sizePolicy().hasHeightForWidth())
        self.groupBoxFolders.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxFolders.setFont(font)
        self.groupBoxFolders.setAutoFillBackground(True)
        self.groupBoxFolders.setStyleSheet(_fromUtf8("#groupBoxUpdates{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(219, 219, 219, 100), stop:1 rgba(255, 255, 255, 100));\n"
"border: 1px solid rgba(255,255,255,50);\n"
"border-bottom-left-radius: 4px;\n"
"border-bottom-right-radius: 4px;\n"
"}"))
        self.groupBoxFolders.setTitle(_fromUtf8(""))
        self.groupBoxFolders.setFlat(True)
        self.groupBoxFolders.setObjectName(_fromUtf8("groupBoxFolders"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBoxFolders)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.downloadFolderButton = QtGui.QToolButton(self.groupBoxFolders)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("folder-downloads"))
        self.downloadFolderButton.setIcon(icon)
        self.downloadFolderButton.setIconSize(QtCore.QSize(64, 64))
        self.downloadFolderButton.setCheckable(True)
        self.downloadFolderButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.downloadFolderButton.setObjectName(_fromUtf8("downloadFolderButton"))
        self.horizontalLayout_3.addWidget(self.downloadFolderButton)
        self.documentsFolderButton = QtGui.QToolButton(self.groupBoxFolders)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("folder-documents"))
        self.documentsFolderButton.setIcon(icon)
        self.documentsFolderButton.setIconSize(QtCore.QSize(64, 64))
        self.documentsFolderButton.setCheckable(True)
        self.documentsFolderButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.documentsFolderButton.setObjectName(_fromUtf8("documentsFolderButton"))
        self.horizontalLayout_3.addWidget(self.documentsFolderButton)
        self.videoFolderButton = QtGui.QToolButton(self.groupBoxFolders)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("folder-video"))
        self.videoFolderButton.setIcon(icon)
        self.videoFolderButton.setIconSize(QtCore.QSize(64, 64))
        self.videoFolderButton.setCheckable(True)
        self.videoFolderButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.videoFolderButton.setObjectName(_fromUtf8("videoFolderButton"))
        self.horizontalLayout_3.addWidget(self.videoFolderButton)
        self.musicFolderButton = QtGui.QToolButton(self.groupBoxFolders)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("folder-sound"))
        self.musicFolderButton.setIcon(icon)
        self.musicFolderButton.setIconSize(QtCore.QSize(64, 64))
        self.musicFolderButton.setCheckable(True)
        self.musicFolderButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.musicFolderButton.setObjectName(_fromUtf8("musicFolderButton"))
        self.horizontalLayout_3.addWidget(self.musicFolderButton)
        self.imageFolderButton = QtGui.QToolButton(self.groupBoxFolders)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("folder-image"))
        self.imageFolderButton.setIcon(icon)
        self.imageFolderButton.setIconSize(QtCore.QSize(64, 64))
        self.imageFolderButton.setCheckable(True)
        self.imageFolderButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.imageFolderButton.setObjectName(_fromUtf8("imageFolderButton"))
        self.horizontalLayout_3.addWidget(self.imageFolderButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addWidget(self.groupBoxFolders)
        self.gridLayout.addLayout(self.verticalLayout_3, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_4 = QtGui.QLabel(folderWidget)
        self.label_4.setMinimumSize(QtCore.QSize(64, 64))
        self.label_4.setMaximumSize(QtCore.QSize(64, 64))
        self.label_4.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8(":/raw/pixmap/applications-other.png")))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.description = QtGui.QLabel(folderWidget)
        self.description.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        self.description.setFont(font)
        self.description.setStyleSheet(_fromUtf8(""))
        self.description.setFrameShadow(QtGui.QFrame.Raised)
        self.description.setWordWrap(True)
        self.description.setIndent(10)
        self.description.setObjectName(_fromUtf8("description"))
        self.horizontalLayout_2.addWidget(self.description)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 30, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        self.label = QtGui.QLabel(folderWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans"))
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(132, 132, 132, 255), stop:0.501481 rgba(70, 70, 70, 255), stop:0.503057 rgba(62, 62, 62, 255), stop:1 rgba(16, 16, 16, 255));\n"
"border: 1px solid rgba(255,255,255,50);\n"
"color:white;\n"
"border-top-left-radius: 4px;\n"
"border-top-right-radius: 4px;"))
        self.label.setMargin(5)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.retranslateUi(folderWidget)
        QtCore.QMetaObject.connectSlotsByName(folderWidget)

    def retranslateUi(self, folderWidget):
        folderWidget.setWindowTitle(kdecore.i18n(_fromUtf8("Home Folder")))
        self.downloadFolderButton.setText(kdecore.i18n(_fromUtf8("Downloads Folder")))
        self.documentsFolderButton.setText(kdecore.i18n(_fromUtf8("Documents Folder")))
        self.videoFolderButton.setText(kdecore.i18n(_fromUtf8("Videos Folder")))
        self.musicFolderButton.setText(kdecore.i18n(_fromUtf8("Music Folder")))
        self.imageFolderButton.setText(kdecore.i18n(_fromUtf8("Images Folder")))
        self.description.setText(kdecore.i18n(_fromUtf8("<html><head/><body><p>By default Chakra doesn\'t create any special folders in the user\'s home directory, as Chakra leaves these kind of choices up to the user. However, in this screen we give you the ability to create the most commonly used folders, as well as custom folders.</p></body></html>")))
        self.label.setText(kdecore.i18n(_fromUtf8("Folders")))

import kapudan_rc
