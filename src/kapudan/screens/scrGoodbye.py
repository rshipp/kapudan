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
from PyKDE4.kdecore import i18n, KGlobal, KToolInvocation

import os
import shutil

from kapudan.screen import Screen
from kapudan.screens.ui_scrGoodbye import Ui_goodbyeWidget


class Widget(QtGui.QWidget, Screen):
    title = i18n("More")
    desc = i18n("Congratulations!")

    def __init__(self, *args):
        QtGui.QWidget.__init__(self, None)
        self.ui = Ui_goodbyeWidget()
        self.ui.setupUi(self)

        self.remove_autostart = True

        lang = KGlobal.locale().language()
        if lang in ["de", "el", "es", "it", "uz"]:
            self.helpPageUrl = "http://chakra-project.org/wiki/index.php?title=Help/" + lang
        else:
            self.helpPageUrl = "http://chakra-project.org/wiki/index.php?title=Help"
        if lang in ["de", "es", "eu", "fr", "it", "pl", "pt-br", "sv", "ru", "uz", "zh-hant"]:
            self.beginnersGuideUrl = "http://chakra-project.org/wiki/index.php?title=Beginners_Guide/" + lang
        else:
            self.beginnersGuideUrl = "http://chakra-project.org/wiki/index.php?title=Beginners_Guide"

        self.autofile = os.path.expanduser("~/.config/autostart/kapudan.desktop")
        self.gautofile = "/usr/share/kde4/apps/kapudan/kapudan/kapudan-autostart.desktop"

        self.ui.autostart.setChecked(False)

    def on_autostart_toggled(self):
        # Remove/set autostart entry
        self.remove_autostart = not self.remove_autostart

    def on_buttonSystemSettings_clicked(self):
        KToolInvocation.startServiceByDesktopName("systemsettings")

    def on_buttonHelpPages_clicked(self):
        KToolInvocation.invokeBrowser(self.helpPageUrl)

    def on_buttonBeginnersGuide_clicked(self):
        KToolInvocation.invokeBrowser(self.beginnersGuideUrl)

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
