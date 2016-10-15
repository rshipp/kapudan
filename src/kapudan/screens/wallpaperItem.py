# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtGui

from kapudan.screens.ui_wallpaperItem import Ui_ServiceItemWidget


class WallpaperItemWidget(QtWidgets.QWidget):

    def __init__(self, title, desc, pic, parent):
        QtWidgets.QWidget.__init__(self, parent)

        self.ui = Ui_ServiceItemWidget()
        self.ui.setupUi(self)

        self.ui.labelName.setText(title)
        self.ui.labelDesc.setText("by " + desc)

        try:
            self.ui.labelStatus.setPixmap(QtGui.QPixmap(pic))
        except:
            pass
