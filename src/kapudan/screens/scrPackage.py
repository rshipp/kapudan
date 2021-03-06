# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets

from PyQt5.QtCore import QCoreApplication, QSettings


from kapudan.screen import Screen
from kapudan.screens.ui_scrPackage import Ui_packageWidget

import subprocess
import os

isUpdateOn = False


class Widget(QtWidgets.QWidget, Screen):
    title = QCoreApplication.translate("Widget", "Packages")
    desc = QCoreApplication.translate("Widget", "Install / Remove Programs")

    screenSettings = {}
    screenSettings["hasChanged"] = False

    def __init__(self, *args):
        QtWidgets.QWidget.__init__(self, None)
        self.ui = Ui_packageWidget()
        self.ui.setupUi(self)

        # set up some variables
        notifier = '/usr/bin/octopi-notifier'
        desktop = '/usr/share/applications/octopi-notifier.desktop'
        autostart = '/usr/share/autostart/octopi-notifier.desktop' 
        self.notifier_enabled = os.path.exists(autostart)

        # set initial states
        self.ui.checkUpdate.setEnabled(os.path.exists(notifier))
        self.ui.checkUpdate.setChecked(self.notifier_enabled)

    def applySettings(self):
        self.__class__.screenSettings["enabled"] = self.notifier_enabled
        if self.ui.checkUpdate.isChecked():
            # checks if octopi-notifier is not in the output of ps -Af
            if "octopi-notifier" not in subprocess.Popen(
                    "ps -Af", shell=True, stdout=subprocess.PIPE).stdout.read():
                subprocess.Popen(["octopi-notifier"], stdout=subprocess.PIPE)

            # was octopi-notifier disabled before?
            if not self.notifier_enabled:
                self.__class__.screenSettings["hasChanged"] = True
            else:
                self.__class__.screenSettings["hasChanged"] = False

        else:
            # don't care if this fails
            os.system("killall octopi-notifier")

            # was octopi-notifier enabled to begin with?
            if self.notifier_enabled:
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
        self.config = QSettings(config)
        self.group = None

    def setValue(self, option, value):
        # FIXME:
        #self.group = self.config.group("General")
        #self.group.writeEntry(option, value)
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
