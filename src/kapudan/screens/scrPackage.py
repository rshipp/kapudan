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
from PyQt4.QtCore import SIGNAL, QVariant

from PyKDE4.kdecore import ki18n, KConfig

#from PyKDE4 import kdeui

from kapudan.screen import Screen
from kapudan.screens.ui_scrPackage import Ui_packageWidget
from kapudan.tools.spunrc import SpunRC

import subprocess
import os

isUpdateOn = False


class Widget(QtGui.QWidget, Screen):
    title = ki18n("Packages")
    desc = ki18n("Install / Remove Programs")

    screenSettings = {}
    screenSettings["hasChanged"] = False

    def __init__(self, *args):
        QtGui.QWidget.__init__(self, None)
        self.ui = Ui_packageWidget()
        self.ui.setupUi(self)

        # initialize the config object, set updateTime
        self.config = SpunRC()
        self.updateTime = self.config.getWaitTime()

        # set updateInterval
        self.ui.updateInterval.setValue(self.updateTime)

        # set initial states
        self.ui.checkUpdate.setChecked(self.config.isEnabled())
        self.ui.updateInterval.setEnabled(self.config.isEnabled())
        self.ui.playAudio.setEnabled(self.config.isEnabled())
        self.ui.playAudio.setChecked(self.config.getAudio())

        # set signals
        self.ui.checkUpdate.connect(self.ui.checkUpdate, SIGNAL("toggled(bool)"), self.updateSelected)

    def updateSelected(self):
        if self.ui.checkUpdate.isChecked():
            self.ui.updateInterval.setEnabled(True)
            self.ui.playAudio.setEnabled(True)
        else:
            self.ui.updateInterval.setEnabled(False)
            self.ui.playAudio.setEnabled(False)

    def applySettings(self):
        # write selected configurations to spunrc
        self.config.setWaitTime(self.ui.updateInterval.value())
        self.config.setAudio(QVariant(self.ui.playAudio.isChecked()))

        if self.ui.checkUpdate.isChecked():
            # checks if spun is not in the output of ps -Af
            if "spun" not in subprocess.Popen(
                    "ps -Af", shell=True, stdout=subprocess.PIPE).stdout.read():
                subprocess.Popen(["spun"], stdout=subprocess.PIPE)

            # was spun disabled before?
            if not self.config.isEnabled():
                self.__class__.screenSettings["hasChanged"] = True
            else:
                self.__class__.screenSettings["hasChanged"] = False

        else:
            # don't care if this fails
            os.system("killall spun")

            # was spun enabled to begin with?
            if self.config.isEnabled():
                self.__class__.screenSettings["hasChanged"] = True
            else:
                self.__class__.screenSettings["hasChanged"] = False

    def shown(self):
        pass

    def execute(self):
        self.applySettings()
        return True


class Config:
    def __init__(self, config):
        self.config = KConfig(config)
        self.group = None

    def setValue(self, option, value):
        self.group = self.config.group("General")
        self.group.writeEntry(option, QVariant(value))
        self.config.sync()


class PMConfig(Config):
    def __init__(self):
        Config.__init__(self, "package-managerrc")

    def setUpdateCheck(self, enabled):
        self.setValue("UpdateCheck", enabled)

    def setUpdateCheckInterval(self, value):
        self.setValue("UpdateCheckInterval", value)

    #def setAudio(self, enabled):
    #    self.setValue("SetAudio", enabled)
    # TODO: Find out what this ^ is for...
