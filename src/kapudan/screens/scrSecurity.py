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
from kapudan.screens.ui_scrSecurity import Ui_securityWidget
from kapudan.tools.rcconf import RCDaemon

import subprocess
import os

isUpdateOn = False

class Widget(QtGui.QWidget, Screen):
    title = ki18n("Security")
    desc = ki18n("Keep your system secure")

    screenSettings = {}
    screenSettings["hasChanged"] = False

    def __init__(self, *args):
        QtGui.QWidget.__init__(self, None)
        self.ui = Ui_securityWidget()
        self.ui.setupUi(self)

        # set up self.config
        self.config = RCDaemon()

        # set initial states
        self.ui.enableFire.setChecked(self.config.isEnabled("ufw"))
        self.ui.enableFire.setEnabled(self.config.isInstalled("ufw"))

        self.ui.enableClam.setEnabled(False)
        if self.config.isInstalled("clamav"):
            if not os.system("grep -q ^Example /etc/clamav/clamd.conf") == 0:
                if not os.system("grep -q ^Example /etc/clamav/freshclam.conf") == 0:
                    self.ui.enableClam.setEnabled(True)

        self.ui.enableClam.setChecked(self.config.isEnabled("clamav"))

    def applySettings(self):
        if self.ui.enableFire.isChecked():
            self.__class__.screenSettings["enableFire"] = True
            if not self.config.isEnabled("ufw"):
                self.__class__.screenSettings["hasChanged"] = True

        else:
            self.__class__.screenSettings["enableFire"] = False
            if self.config.isEnabled("ufw"):
                self.__class__.screenSettings["hasChanged"] = True

        if self.ui.enableClam.isChecked():
            self.__class__.screenSettings["enableClam"] = True
            if not self.config.isEnabled("clamav"):
                self.__class__.screenSettings["hasChanged"] = True

        else:
            self.__class__.screenSettings["enableClam"] = False
            if self.config.isEnabled("clamav"):
                self.__class__.screenSettings["hasChanged"] = True



    def on_buttonClam_clicked(self):
        self.procSettings = QProcess()
        command = "xdg-open http://www.chakra-linux.org/wiki/index.php/Anti-Malware#ClamAV"
        self.procSettings.start(command)

    def on_buttonTomoyo_clicked(self):
        self.procSettings = QProcess()
        command = "xdg-open http://www.chakra-linux.org/wiki/index.php/Using_tomoyo-tools_for_system_security"
        self.procSettings.start(command)

    def on_buttonKwallet_clicked(self):
        self.procSettings = QProcess()
        command = "xdg-open http://www.chakra-linux.org/wiki/index.php/KDE_Wallet_Manager"
        self.procSettings.start(command)

    def on_buttonRootkit_clicked(self):
        self.procSettings = QProcess()
        command = "xdg-open http://www.chakra-linux.org/wiki/index.php/Anti-Malware#chkrootkit_and_rkhunter"
        self.procSettings.start(command)

    def on_buttonTiger_clicked(self):
        self.procSettings = QProcess()
        command = "xdg-open http://www.nongnu.org/tiger/"
        self.procSettings.start(command)


    def shown(self):
        pass

    def execute(self):
        self.applySettings()
        return True
