#!/usr/bin/env python2
# coding=UTF-8
#
# Generated by pykdeuic4 from ui/ui_scrSearch.ui on Fri May 25 10:27:27 2012
#
# WARNING! All changes to this file will be lost.
from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_searchWidget(object):
    def setupUi(self, searchWidget):
        searchWidget.setObjectName(_fromUtf8("searchWidget"))
        searchWidget.resize(786, 513)
        searchWidget.setStyleSheet(_fromUtf8(""))
        self.gridLayout = QtGui.QGridLayout(searchWidget)
        self.gridLayout.setMargin(20)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(searchWidget)
        self.label.setMinimumSize(QtCore.QSize(64, 64))
        self.label.setMaximumSize(QtCore.QSize(64, 64))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/raw/pixmap/nepomuk.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.description = QtGui.QLabel(searchWidget)
        self.description.setMinimumSize(QtCore.QSize(350, 0))
        self.description.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        self.description.setFont(font)
        self.description.setStyleSheet(_fromUtf8(""))
        self.description.setFrameShadow(QtGui.QFrame.Raised)
        self.description.setWordWrap(True)
        self.description.setIndent(10)
        self.description.setObjectName(_fromUtf8("description"))
        self.gridLayout.addWidget(self.description, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 30, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 344, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 5, 0, 1, 1)
        self.groupBoxRepo = QtGui.QGroupBox(searchWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxRepo.setFont(font)
        self.groupBoxRepo.setStyleSheet(_fromUtf8("#groupBoxRepo{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(219, 219, 219, 100), stop:1 rgba(255, 255, 255, 100));\n"
"border: 1px solid rgba(255,255,255,50);\n"
"border-bottom-left-radius: 4px;\n"
"border-bottom-right-radius: 4px;\n"
"}"))
        self.groupBoxRepo.setTitle(_fromUtf8(""))
        self.groupBoxRepo.setFlat(True)
        self.groupBoxRepo.setObjectName(_fromUtf8("groupBoxRepo"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBoxRepo)
        self.verticalLayout_2.setMargin(10)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.checkBoxNepomuk = QtGui.QCheckBox(self.groupBoxRepo)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        self.checkBoxNepomuk.setFont(font)
        self.checkBoxNepomuk.setStyleSheet(_fromUtf8("color: rgb(30, 43, 51)"))
        self.checkBoxNepomuk.setChecked(False)
        self.checkBoxNepomuk.setObjectName(_fromUtf8("checkBoxNepomuk"))
        self.verticalLayout_2.addWidget(self.checkBoxNepomuk)
        self.gridLayout.addWidget(self.groupBoxRepo, 4, 0, 1, 2)
        self.label_2 = QtGui.QLabel(searchWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Gothic L"))
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(132, 132, 132, 255), stop:0.501481 rgba(70, 70, 70, 255), stop:0.503057 rgba(62, 62, 62, 255), stop:1 rgba(16, 16, 16, 255));\n"
"/*background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(219, 219, 219, 100), stop:1 rgba(255, 255, 255, 100));*/\n"
"border: 1px solid rgba(255,255,255,50);\n"
"color:white;\n"
"border-top-left-radius: 4px;\n"
"border-top-right-radius: 4px;"))
        self.label_2.setMargin(5)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 2)

        self.retranslateUi(searchWidget)
        QtCore.QMetaObject.connectSlotsByName(searchWidget)

    def retranslateUi(self, searchWidget):
        searchWidget.setWindowTitle(kdecore.i18n(_fromUtf8("Search")))
        self.description.setText(kdecore.i18n(_fromUtf8("Strigi Desktop Search indexes your frequently used files. This gives you very fast file search results. Strigi also can search for files based on their contents.")))
        self.checkBoxNepomuk.setText(kdecore.i18n(_fromUtf8("Allow Strigi to index my files")))
        self.label_2.setText(kdecore.i18n(_fromUtf8("Search Options")))

import kaptan.kaptan_rc
