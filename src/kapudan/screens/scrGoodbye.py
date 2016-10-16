# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5.QtCore import QProcess  # get rid of QProcess
from PyQt5.QtCore import QCoreApplication

import os
import shutil

from kapudan.screen import Screen
from kapudan.screens.ui_scrGoodbye import Ui_goodbyeWidget


class Widget(QtWidgets.QWidget, Screen):
    title = QCoreApplication.translate("Widget", "More")
    desc = QCoreApplication.translate("Widget", "Congratulations!")

    def __init__(self, *args):
        QtWidgets.QWidget.__init__(self, None)
        self.ui = Ui_goodbyeWidget()
        self.ui.setupUi(self)

        self.remove_autostart = True

        lang = 'en_US' #KGlobal.locale().language()
        if lang in ["de", "el", "es", "it", "uz"]:
            self.helpPageUrl = "https://chakralinux.org/wiki/index.php?title=Help/" + lang
        else:
            self.helpPageUrl = "https://chakralinux.org/wiki/index.php?title=Help"
        if lang in ["de", "es", "eu", "fr", "it", "pl", "pt-br", "sv", "ru", "uz", "zh-hant"]:
            self.beginnersGuideUrl = "https://chakralinux.org/wiki/index.php?title=Beginner's_Guide/" + lang
        else:
            self.beginnersGuideUrl = "https://chakralinux.org/wiki/index.php?title=Beginner's_Guide"

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
