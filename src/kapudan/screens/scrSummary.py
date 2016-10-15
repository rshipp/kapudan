# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QCoreApplication, QSettings

import subprocess
import os
import dbus
import time

from kapudan.screen import Screen
from kapudan.screens.ui_scrSummary import Ui_summaryWidget

# import other widgets to get the latest configuration
#import kapudan.screens.scrFolder as folderWidget
import kapudan.screens.scrWallpaper as wallpaperWidget
import kapudan.screens.scrMouse as mouseWidget
import kapudan.screens.scrMenu as menuWidget
import kapudan.screens.scrPackage as packageWidget
import kapudan.screens.scrServices as servicesWidget
import kapudan.screens.scrSecurity as securityWidget

#from kapudan.tools import tools
from kapudan.tools.daemon import Daemon


class Widget(QtWidgets.QWidget, Screen):
    title = QCoreApplication.translate("kapudan", "Summary")
    desc = QCoreApplication.translate("kapudan", "Save Your Settings")

    def __init__(self, *args):
        QtWidgets.QWidget.__init__(self, None)
        self.ui = Ui_summaryWidget()
        self.ui.setupUi(self)

    def shown(self):
        self.wallpaperSettings = wallpaperWidget.Widget.screenSettings
        self.mouseSettings = mouseWidget.Widget.screenSettings
        self.menuSettings = menuWidget.Widget.screenSettings
        self.packageSettings = packageWidget.Widget.screenSettings
        self.servicesSettings = servicesWidget.Widget.screenSettings
        self.securitySettings = securityWidget.Widget.screenSettings

        subject = "<p><li><b>%s</b></li><ul>"
        item = "<li>%s</li>"
        end = "</ul></p>"
        content = ""

        content += """<html><body><ul>"""

        # Mouse Settings
        content += subject % QCoreApplication.translate("kapudan", "Mouse Settings")

        content += (item % QCoreApplication.translate("kapudan", "Selected Mouse configuration: <b>%s</b>") % self.mouseSettings["summaryMessage"]["selectedMouse"])
        content += (item % QCoreApplication.translate("kapudan", "Selected clicking behavior: <b>%s</b>") % self.mouseSettings["summaryMessage"]["singleClick"])
        content += end

        # Menu Settings
        content += (subject % QCoreApplication.translate("kapudan", "Menu Settings"))
        content += (item % QCoreApplication.translate("kapudan", "Selected Menu: <b>%s</b>") % self.menuSettings["summaryMessage"])
        content += end

        # Wallpaper Settings
        content += (subject % QCoreApplication.translate("kapudan", "Wallpaper Settings"))
        if not self.wallpaperSettings["hasChanged"]:
            content += (item % QCoreApplication.translate("kapudan", "You haven't selected any wallpaper."))
        else:
            content += (item % QCoreApplication.translate("kapudan", "Selected Wallpaper: <b>%s</b>") % os.path.basename(str(self.wallpaperSettings["selectedWallpaper"])))
        content += end

        # Notifier Settings
        if self.packageSettings["hasChanged"]:
            content += (subject % QCoreApplication.translate("kapudan", "Package Management Settings"))
            content += (item % QCoreApplication.translate("kapudan", "You have enabled or disabled octopi-notifier."))

            content += end

        # Services Settings
        if self.servicesSettings["hasChanged"]:
            self.daemon = Daemon()
            self.svctext = QCoreApplication.translate("kapudan", "You have: ")
            self.svcissset = False
            content += (subject % QCoreApplication.translate("kapudan", "Services Settings"))

            if self.servicesSettings["enableCups"] and not self.daemon.isEnabled("org.cups.cupsd"):
                self.svctext += QCoreApplication.translate("kapudan", "enabled cups; ")
                self.svcisset = True
            elif not self.servicesSettings["enableCups"] and self.daemon.isEnabled("org.cups.cupsd"):
                self.svctext += QCoreApplication.translate("kapudan", "disabled cups; ")
                self.svcisset = True
            if self.servicesSettings["enableBluetooth"] and not self.daemon.isEnabled("bluetooth"):
                self.svctext += QCoreApplication.translate("kapudan", "enabled bluetooth; ")
                self.svcisset = True
            elif not self.servicesSettings["enableBluetooth"] and self.daemon.isEnabled("bluetooth"):
                self.svctext += QCoreApplication.translate("kapudan", "disabled bluetooth; ")
                self.svcisset = True

            #FIXME: when can this ever happen?
            if not self.svcisset:
                self.svctext = QCoreApplication.translate("kapudan", "You have made no changes.")
                self.servicesSettings["hasChanged"] = False

            content += (item % QCoreApplication.translate("kapudan", self.svctext))

            content += end

        # Security Settings
        if self.securitySettings["hasChanged"]:
            self.daemon = Daemon()
            self.sectext = QCoreApplication.translate("kapudan", "You have: ")
            self.secisset = False
            content += (subject % QCoreApplication.translate("kapudan", "Security Settings"))

            if self.securitySettings["enableClam"] and not self.daemon.isEnabled("clamd"):
                self.sectext += QCoreApplication.translate("kapudan", "enabled ClamAV; ")
                self.secisset = True
            elif not self.securitySettings["enableClam"] and self.daemon.isEnabled("clamd"):
                self.sectext += QCoreApplication.translate("kapudan", "disabled ClamAV; ")
                self.secisset = True
            if self.securitySettings["enableFire"] and not self.daemon.isEnabled("ufw"):
                self.sectext += QCoreApplication.translate("kapudan", "enabled the firewall; ")
                self.secisset = True
            elif not self.securitySettings["enableFire"] and self.daemon.isEnabled("ufw"):
                self.sectext += QCoreApplication.translate("kapudan", "disabled the firewall; ")
                self.secisset = True

            if not self.secisset:
                self.sectext = QCoreApplication.translate("kapudan", "You have made no changes.")
                self.securitySettings["hasChanged"] = False

            content += (item % QCoreApplication.translate("kapudan", self.sectext))

            content += end

        self.ui.textSummary.setText(content)

    def killPlasma(self):
        try:
            p = subprocess.Popen(["kquitapp", "plasma-desktop"], stdout=subprocess.PIPE)
            out, err = p.communicate()
            time.sleep(1)
            self.startPlasma()

        except:
            QMessageBox.critical(self, QCoreApplication.translate("kapudan", "Error"), QCoreApplication.translate("kapudan", "Cannot restart plasma-desktop. Kapudan will now shut down."))
            #kdeui.KApplication.kApplication().quit()
            exit()

    def startPlasma(self):
        subprocess.Popen(["plasma-desktop"], stdout=subprocess.PIPE)

    def execute(self):
        hasChanged = False
        rootActions = ""

        # Wallpaper Settings
        if self.wallpaperSettings["hasChanged"]:
            hasChanged = True

        # Menu Settings
        if self.menuSettings["hasChanged"]:
            hasChanged = True

        # Notifier Settings
        if self.packageSettings["hasChanged"]:
            if self.packageSettings["enabled"]:
                rootActions += "disable_notifier "
            else:
                rootActions += "enable_notifier "

        # Services Settings
        if self.servicesSettings["hasChanged"]:
            if self.servicesSettings["enableCups"] and not self.daemon.isEnabled("org.cups.cupsd"):
                rootActions += "enable_cups "
            elif not self.servicesSettings["enableCups"] and self.daemon.isEnabled("org.cups.cupsd"):
                rootActions += "disable_cups "
            if self.servicesSettings["enableBluetooth"] and not self.daemon.isEnabled("bluetooth"):
                rootActions += "enable_blue "
            elif not self.servicesSettings["enableBluetooth"] and self.daemon.isEnabled("bluetooth"):
                rootActions += "disable_blue "

        # Security Settings
        if self.securitySettings["hasChanged"]:
            if self.securitySettings["enableClam"] and not self.daemon.isEnabled("clamd"):
                rootActions += "enable_clam "
            elif not self.securitySettings["enableClam"] and self.daemon.isEnabled("clamd"):
                rootActions += "disable_clam "
            if self.securitySettings["enableFire"] and not self.daemon.isEnabled("ufw"):
                rootActions += "enable_fire "
            elif not self.securitySettings["enableFire"] and self.daemon.isEnabled("ufw"):
                rootActions += "disable_fire "

        if hasChanged:
            self.killPlasma()

        if not rootActions == "":
            os.system("kdesu konsole -e kapudan-rootactions " + rootActions)

        return True
