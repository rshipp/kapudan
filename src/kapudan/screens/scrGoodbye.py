# -*- coding: utf-8 -*-
#
# Copyright (C) 2012-2015, The Chakra Developers
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

from PyQt5 import QtWidgets
from PyQt5.QtCore import QProcess  # get rid of QProcess
from PyQt5.QtCore import QCoreApplication

import os
import shutil

from kapudan.screen import Screen
from kapudan.screens.ui_scrGoodbye import Ui_goodbyeWidget


class Widget(QtWidgets.QWidget, Screen):
    title = QCoreApplication.translate("kapudan", "More")
    desc = QCoreApplication.translate("kapudan", "Congratulations!")

    def __init__(self, *args):
        QtWidgets.QWidget.__init__(self, None)
        self.ui = Ui_goodbyeWidget()
        self.ui.setupUi(self)

        self.remove_autostart = True

        lang = 'en_US' #KGlobal.locale().language()
        if lang in ["de", "el", "es", "it", "uz"]:
            self.helpPageUrl = "http://chakraos.org/wiki/index.php?title=Help/" + lang
        else:
            self.helpPageUrl = "http://chakraos.org/wiki/index.php?title=Help"
        if lang in ["de", "es", "eu", "fr", "it", "pl", "pt-br", "sv", "ru", "uz", "zh-hant"]:
            self.beginnersGuideUrl = "http://chakraos.org/wiki/index.php?title=Beginner's_Guide/" + lang
        else:
            self.beginnersGuideUrl = "http://chakraos.org/wiki/index.php?title=Beginner's_Guide"

        self.autofile = os.path.expanduser("~/.config/autostart/kapudan.desktop")
        self.gautofile = "/usr/share/kde4/apps/kapudan/kapudan/kapudan-autostart.desktop"

        self.ui.autostart.setChecked(False)

    def on_autostart_toggled(self):
        # Remove/set autostart entry
        self.remove_autostart = not self.remove_autostart

    def on_buttonSystemSettings_clicked(self):
        self.procSettings = QProcess()
        self.procSettings.start("systemsettings")

    def on_buttonHelpPages_clicked(self):
        self.procSettings = QProcess()
        command = "xdg-open " + self.helpPageUrl
        self.procSettings.start(command)

    def on_buttonBeginnersGuide_clicked(self):
        self.procSettings = QProcess()
        command = "xdg-open " + self.beginnersGuideUrl
        self.procSettings.start(command)

    def execute(self):
        if self.remove_autostart:
            try:
                os.remove(self.autofile)
            except OSError:
                pass
        else:
            if not os.path.isfile(self.autofile):
                shutil.copyfile(self.gautofile, self.autofile)
        return True
