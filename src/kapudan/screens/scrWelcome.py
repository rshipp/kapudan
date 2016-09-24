# -*- coding: utf-8 -*-
#
# Copyright (C) 2012, The Chakra Developers
#
# This is a fork of Pardus's Kaptan, which is
# Copyright (C) 2005-2009, TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

import os

from PyQt5 import QtCore, QtGui
from kapudan.screen import Screen
from kapudan.screens.ui_scrWelcome import Ui_welcomeWidget
from kapudan.tools import tools


class Widget(QtGui.QWidget, Screen):

    title = QtCore.QCoreApplication.translate("kapudan", "Welcome")
    desc = QtCore.QCoreApplication.translate("kapudan", "Welcome to %s")

    def __init__(self, *args):
        QtGui.QWidget.__init__(self, None)
        self.ui = Ui_welcomeWidget()
        self.ui.setupUi(self)
        Widget.desc = unicode(Widget.desc) % tools.getRelease()

        self.autofile = os.path.expanduser("~/.config/autostart/kapudan.desktop")

    def shown(self):
        try:
            os.remove(self.autofile)
        except OSError:
            pass

    def execute(self):
        return True
