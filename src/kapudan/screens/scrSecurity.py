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

from PyKDE4.kdecore import i18n, KToolInvocation

#from PyKDE4 import kdeui

from kapudan.screen import Screen
from kapudan.screens.ui_scrSecurity import Ui_securityWidget
from kapudan.tools.daemon import Daemon

import os

isUpdateOn = False


class Widget(QtGui.QWidget, Screen):
    title = i18n("Security")
    desc = i18n("Keep your system secure")

    screenSettings = {}
    screenSettings["hasChanged"] = False
    screenSettings["daemons"] = []

    def __init__(self, *args):
        QtGui.QWidget.__init__(self, None)
        self.ui = Ui_securityWidget()
        self.ui.setupUi(self)

        # set up the daemon handlers
        self.ufw_daemon = Daemon("ufw")
        self.clamd_daemon = Daemon("clamd")

        # set initial states
        self.ui.enableFire.setChecked(self.ufw_daemon.is_enabled())
        self.ui.enableFire.setEnabled(self.ufw_daemon.is_installed())

        self.ui.enableClam.setEnabled(False)
        if self.clamd_daemon.is_installed():
            # TODO: remove this!
            # FIXME: does it even work?
            if not os.system("grep -q ^Example /etc/clamav/clamd.conf") == 0:
                if not os.system("grep -q ^Example /etc/clamav/freshclam.conf") == 0:
                    self.ui.enableClam.setEnabled(True)
            self.ui.enableClam.setChecked(self.clamd_daemon.is_enabled())
        else:
            self.ui.enableClam.setChecked(False)

        # connect to the checkboxes' signal
        self.ui.enableFire.stateChanged.connect(self.ufw_daemon.toggle_enable)
        self.ui.enableClam.stateChanged.connect(self.clamd_daemon.toggle_enable)
        # connect to the buttons' clicked event, don't rely on connectByName
        self.ui.buttonClam.clicked.connect(self.clam_info)
        self.ui.buttonKwallet.clicked.connect(self.kwallet_info)
        self.ui.buttonTomoyo.clicked.connect(self.tomoyo_info)
        self.ui.buttonTiger.clicked.connect(self.tiger_info)
        self.ui.buttonRootkit.clicked.connect(self.rootkit_info)

    def applySettings(self):
        self.__class__.screenSettings["hasChanged"] = (
            self.ufw_daemon.enabled_changed or self.clamd_daemon.enabled_changed)
        for daemon in (self.ufw_daemon, self.clamd_daemon):
            if daemon.enabled_changed:
                self.__class__.screenSettings["daemons"].append(daemon)

    def clam_info(self):
        KToolInvocation.invokeBrowser("http://www.chakra-project.org/wiki/index.php?title=Anti-Malware#ClamAV")

    def tomoyo_info(self):
        KToolInvocation.invokeBrowser("http://www.chakra-project.org/wiki/index.php?title=Using_tomoyo-tools_for_system_security")

    def kwallet_info(self):
        KToolInvocation.invokeBrowser("http://www.chakra-project.org/wiki/index.php?title=KDE_Wallet_Manager")

    def rootkit_info(self):
        KToolInvocation.invokeBrowser("http://www.chakra-project.org/wiki/index.php?title=Anti-Malware#chkrootkit_and_rkhunter")

    def tiger_info(self):
        KToolInvocation.invokeBrowser("://www.nongnu.org/tiger/")

    def shown(self):
        pass

    def execute(self):
        self.applySettings()
        return True
