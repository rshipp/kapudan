# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
#from PyQt5.QtCore import

from PyQt5.QtCore import QCoreApplication


from kapudan.screen import Screen
from kapudan.screens.ui_scrServices import Ui_servicesWidget
from kapudan.tools.daemon import Daemon

isUpdateOn = False


class Widget(QtWidgets.QWidget, Screen):
    title = QCoreApplication.translate("kapudan", "Services")
    desc = QCoreApplication.translate("kapudan", "Enable / Disable Services (Daemons)")

    screenSettings = {}
    screenSettings["hasChanged"] = False

    def __init__(self, *args):
        QtWidgets.QWidget.__init__(self, None)
        self.ui = Ui_servicesWidget()
        self.ui.setupUi(self)

        # set up self.config
        self.__class__.screenSettings["daemons"] = []
        self.services = ["org.cups.cupsd", "bluetooth"]
        self.daemons = {}
        for service in self.services:
            self.daemons[service] = Daemon(service)

        # set initial states
        # TODO: avoid the code dublication here
        self.ui.enableCups.setChecked(self.daemons["org.cups.cupsd"].is_enabled())
        self.ui.enableBluetooth.setChecked(self.daemons["bluetooth"].is_enabled())
        self.ui.enableCups.setEnabled(self.daemons["org.cups.cupsd"].is_installed())
        self.ui.enableBluetooth.setEnabled(self.daemons["bluetooth"].is_installed())

    def applySettings(self):
        if self.ui.enableCups.isChecked():
            self.__class__.screenSettings["enableCups"] = True
            if not self.daemons["org.cups.cupsd"].is_enabled():
                self.daemons["org.cups.cupsd"].has_changed = True
                self.__class__.screenSettings["daemons"].append(self.daemons["org.cups.cupsd"])
        else:
            self.__class__.screenSettings["enableCups"] = False
            if self.daemons["org.cups.cupsd"].is_enabled():
                self.daemons["org.cups.cupsd"].has_changed = True
                self.__class__.screenSettings["daemons"].append(self.daemons["org.cups.cupsd"])

        if self.ui.enableBluetooth.isChecked():
            self.__class__.screenSettings["enableBluetooth"] = True
            if not self.daemons["bluetooth"].is_enabled():
                self.daemons["bluetooth"].has_changed = True
                self.__class__.screenSettings["daemons"].append(self.daemons["bluetooth"])
        else:
            self.__class__.screenSettings["enableBluetooth"] = False
            if self.daemons["bluetooth"].is_enabled():
                self.__class__.screenSettings["hasChanged"] = True
                self.daemons["bluetooth"].has_changed = True
        self.__class__.screenSettings["hasChanged"] = self.daemons["org.cups.cupsd"].has_changed or self.daemons["bluetooth"].has_changed

    def shown(self):
        pass

    def execute(self):
        self.applySettings()
        return True
