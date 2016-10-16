# -*- coding: utf-8 -*-

import os

from PyQt5 import QtCore, QtWidgets
from kapudan.screen import Screen
from kapudan.screens.ui_scrWelcome import Ui_welcomeWidget
from kapudan.tools import tools


class Widget(QtWidgets.QWidget, Screen):

    title = QtCore.QCoreApplication.translate("Widget", "Welcome")
    desc = QtCore.QCoreApplication.translate("Widget", "Welcome to %s")

    def __init__(self, *args):
        QtWidgets.QWidget.__init__(self, None)
        self.ui = Ui_welcomeWidget()
        self.ui.setupUi(self)
        Widget.desc = str(Widget.desc) % tools.getRelease()

        self.autofile = os.path.expanduser("~/.config/autostart/kapudan.desktop")

    def shown(self):
        try:
            os.remove(self.autofile)
        except OSError:
            pass

    def execute(self):
        return True
