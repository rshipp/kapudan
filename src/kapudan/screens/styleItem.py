#!/usr/bin/python

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *

from kapudan.screens.ui_scrStyleItem import Ui_StyleItemWidget

class StyleItemWidget(QtWidgets.QWidget):

    def __init__(self, title, desc, pic, parent):
        QtWidgets.QWidget.__init__(self, parent)

        self.ui = Ui_StyleItemWidget()
        self.ui.setupUi(self)

        self.ui.styleName.setText(title)
        self.ui.styleDesc.setText(desc)
        self.ui.stylePreview.setPixmap(QtGui.QPixmap(pic))

