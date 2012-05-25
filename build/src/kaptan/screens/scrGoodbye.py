# -*- coding: utf-8 -*-
#
# Copyright (C) 2012, The Chakra Developers
#
# This is a fork of Pardus' Kaptan, which is
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
from PyKDE4.kdecore import ki18n, KGlobal, KConfig

import subprocess, sys

from kaptan.screen import Screen
from kaptan.screens.ui_scrGoodbye import Ui_goodbyeWidget

class Widget(QtGui.QWidget, Screen):
    title = ki18n("More")
    desc = ki18n("Congratulations!")

    def __init__(self, *args):
        QtGui.QWidget.__init__(self,None)
        self.ui = Ui_goodbyeWidget()
        self.ui.setupUi(self)

        lang = KGlobal.locale().language()
        if lang in ["de", "el", "es", "it", "uz"]:
            self.helpPageUrl = "http://chakra-linux.org/wiki/index.php/Help/" + lang
        else:
            self.helpPageUrl = "http://chakra-linux.org/wiki/index.php/Help"

    def on_buttonSystemSettings_clicked(self):
        self.procSettings = QProcess()
        self.procSettings.start("systemsettings")

    def on_buttonHelpPages_clicked(self):
        self.procSettings = QProcess()
        command = "kfmclient openURL " + self.helpPageUrl
        self.procSettings.start(command)

    def execute(self):
       return True

