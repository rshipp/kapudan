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

from PyQt4 import QtGui
#from PyQt4.QtCore import

from PyKDE4.kdecore import i18n

#from PyKDE4 import kdeui

from kapudan.screen import Screen
from kapudan.screens.ui_scrKsuperkey import Ui_ksuperkeyWidget
from kapudan.tools.ksuperkey import KSuperKey

isUpdateOn = False


class Widget(QtGui.QWidget, Screen):
    title = i18n("KSuperKey")
    desc = i18n("Enable / Disable KSuperKey")

    screenSettings = {}
    screenSettings["hasChanged"] = False

    def __init__(self, *args):
        QtGui.QWidget.__init__(self, None)
        self.ui = Ui_ksuperkeyWidget()
        self.ui.setupUi(self)
        self.ksuperkey = KSuperKey()

        # set initial states
        self.ui.enableKsuperkey.setEnabled(self.ksuperkey.isEnabled())

    def applySettings(self):
        if self.ui.enableKsuperkey.isChecked():
            self.ksuperkey.enable()
        else:
            self.ksuperkey.disable()

    def shown(self):
        pass

    def execute(self):
        self.applySettings()
        return True
