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
from PyQt4.QtCore import *

from PyKDE4.kdecore import ki18n, KConfig

#from PyKDE4 import kdeui

from kapudan.screen import Screen
from kapudan.screens.ui_scrServices import Ui_servicesWidget
from kapudan.tools.rcconf import RCDaemon

import subprocess
import os

isUpdateOn = False

class Widget(QtGui.QWidget, Screen):
    title = ki18n("Services")
    desc = ki18n("Enable / Disable Services (Daemons)")

    screenSettings = {}
    screenSettings["hasChanged"] = False

    def __init__(self, *args):
        QtGui.QWidget.__init__(self, None)
        self.ui = Ui_servicesWidget()
        self.ui.setupUi(self)

        # set up self.config
        self.config = RCDaemon()

        # set initial states
        self.ui.enableCups.setChecked(self.config.isEnabled("cups"))
        self.ui.enableBluetooth.setChecked(self.config.isEnabled("bluetooth"))
        self.ui.enableCups.setEnabled(self.config.isInstalled("cups"))
        self.ui.enableBluetooth.setEnabled(self.config.isInstalled("bluetooth"))

    def applySettings(self):
        if self.ui.enableCups.isChecked():
            self.__class__.screenSettings["enableCups"] = True
            if not self.config.isEnabled("cups"):
                self.__class__.screenSettings["hasChanged"] = True

        else:
            self.__class__.screenSettings["enableCups"] = False
            if self.config.isEnabled("cups"):
                self.__class__.screenSettings["hasChanged"] = True

        if self.ui.enableBluetooth.isChecked():
            self.__class__.screenSettings["enableBluetooth"] = True
            if not self.config.isEnabled("bluetooth"):
                self.__class__.screenSettings["hasChanged"] = True

        else:
            self.__class__.screenSettings["enableBluetooth"] = False
            if self.config.isEnabled("bluetooth"):
                self.__class__.screenSettings["hasChanged"] = True


    def shown(self):
        pass

    def execute(self):
        self.applySettings()
        return True
