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
import kapudan.screens.scrStyle as styleWidget
import kapudan.screens.scrMenu as menuWidget
import kapudan.screens.scrPackage as packageWidget
import kapudan.screens.scrServices as servicesWidget
import kapudan.screens.scrSecurity as securityWidget
import kapudan.screens.scrExtra as extraWidget

#from kapudan.tools import tools
from kapudan.tools.daemon import Daemon
from kapudan.tools.repos import Repos


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
        self.styleSettings = styleWidget.Widget.screenSettings
        self.packageSettings = packageWidget.Widget.screenSettings
        self.servicesSettings = servicesWidget.Widget.screenSettings
        self.securitySettings = securityWidget.Widget.screenSettings
        self.extraSettings = extraWidget.Widget.screenSettings

        subject = "<p><li><b>%s</b></li><ul>"
        item = "<li>%s</li>"
        end = "</ul></p>"
        content = ""

        content += """<html><body><ul>"""

        # Mouse Settings
        content += subject % QCoreApplication.translate("kapudan", "Mouse Settings")

        content += (item % QCoreApplication.translate("kapudan", "Selected Mouse configuration: <b>%s</b>") % self.mouseSettings["summaryMessage"]["selectedMouse"])
        content += (item % QCoreApplication.translate("kapudan", "Selected clicking behavior: <b>%s</b>") % self.mouseSettings["summaryMessage"]["clickBehavior"])
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

        # Style Settings
        content += (subject % QCoreApplication.translate("kapudan", "Style Settings"))

        if not self.styleSettings["hasChanged"]:
            content += (item % QCoreApplication.translate("kapudan", "You haven't selected any style."))
        else:
            content += (item % QCoreApplication.translate("kapudan", "Selected Style: <b>%s</b>") % str(self.styleSettings["summaryMessage"]))

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

        # Extra Settings
        if self.extraSettings["hasChanged"]:
            self.repos = Repos()
            self.extratext = QCoreApplication.translate("kapudan", "You have: ")
            self.extraisset = False
            content += (subject % QCoreApplication.translate("kapudan", "Extra Settings"))

            if self.extraSettings["enableExtra"] and not self.repos.extraIsEnabled():
                self.extratext += QCoreApplication.translate("kapudan", "enabled the [extra] repo; ")
                self.extraisset = True
            elif not self.extraSettings["enableExtra"] and self.repos.extraIsEnabled():
                self.extratext += QCoreApplication.translate("kapudan", "disabled the [extra] repo; ")
                self.extraisset = True

            if not self.extraisset:
                self.extratext = QCoreApplication.translate("kapudan", "You have made no changes.")
                self.extraSettings["hasChanged"] = False

            content += (item % QCoreApplication.translate("kapudan", self.extratext))

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
            if self.wallpaperSettings["selectedWallpaper"]:
                config = QSettings("plasma-desktop-appletsrc")
                # FIXME:
                #group = config.group("Containments")
                #for each in list(group.groupList()):
                #    subgroup = group.group(each)
                #    subcomponent = subgroup.readEntry('plugin')
                #    if subcomponent == 'desktop' or subcomponent == 'folderview':
                #        subg = subgroup.group('Wallpaper')
                #        subg_2 = subg.group('image')
                #        subg_2.writeEntry("wallpaper", self.wallpaperSettings["selectedWallpaper"])

        # Menu Settings
        if self.menuSettings["hasChanged"]:
            hasChanged = True
            config = QSettings("plasma-desktop-appletsrc")
            # FIXME
            #group = config.group("Containments")

            #for each in list(group.groupList()):
            #    subgroup = group.group(each)
            #    subcomponent = subgroup.readEntry('plugin')
            #    if subcomponent == 'panel':
            #        subg = subgroup.group('Applets')
            #        for i in list(subg.groupList()):
            #            subg2 = subg.group(i)
            #            launcher = subg2.readEntry('plugin')
            #            if str(launcher).find('launcher') >= 0:
            #                subg2.writeEntry('plugin', self.menuSettings["selectedMenu"])

        def removeFolderViewWidget():
            config = QSettings("plasma-desktop-appletsrc")

            # FIXME
            #sub_lvl_0 = config.group("Containments")

            #for sub in list(sub_lvl_0.groupList()):
            #    sub_lvl_1 = sub_lvl_0.group(sub)

            #    if sub_lvl_1.hasGroup("Applets"):
            #        sub_lvl_2 = sub_lvl_1.group("Applets")

            #        for sub2 in list(sub_lvl_2.groupList()):
            #            sub_lvl_3 = sub_lvl_2.group(sub2)
            #            plugin = sub_lvl_3.readEntry('plugin')

            #            if plugin == 'folderview':
            #                sub_lvl_3.deleteGroup()

        # Desktop Type
        if self.styleSettings["hasChangedDesktopType"]:
            hasChanged = True
            config = QSettings("plasma-desktop-appletsrc")
            # FIXME
            #group = config.group("Containments")

            #for each in list(group.groupList()):
            #    subgroup = group.group(each)
            #    subcomponent = subgroup.readEntry('plugin')
            #    subcomponent2 = subgroup.readEntry('screen')
            #    if subcomponent == 'desktop' or subcomponent == 'folderview':
            #        if int(subcomponent2) == 0:
            #            subgroup.writeEntry('plugin', self.styleSettings["desktopType"])

            # Remove folder widget - normally this would be done over dbus but thanks to improper naming of the plasma interface
            # this is not possible
            # ValueError: Invalid interface or error name 'org.kde.plasma-desktop': contains invalid character '-'
            #
            # Related Bug:
            # Bug 240358 - Invalid D-BUS interface name 'org.kde.plasma-desktop.PlasmaApp' found while parsing introspection
            # https://bugs.kde.org/show_bug.cgi?id=240358

            if self.styleSettings["desktopType"] == "folderview":
                removeFolderViewWidget()

            config.sync()

        # Number of Desktops
        if self.styleSettings["hasChangedDesktopNumber"]:
            hasChanged = True
            config = QSettings("kwinrc")
            # FIXME
            #group = config.group("Desktops")
            #group.writeEntry('Number', self.styleSettings["desktopNumber"])
            #group.sync()

            # FIXME: 
            #info = kdeui.NETRootInfo(QtGui.QX11Info.display(), kdeui.NET.NumberOfDesktops | kdeui.NET.DesktopNames)
            #info.setNumberOfDesktops(int(self.styleSettings["desktopNumber"]))
            #info.activate()

            session = dbus.SessionBus()

            try:
                proxy = session.get_object('org.kde.kwin', '/KWin')
                proxy.reconfigure()
            except dbus.DBusException:
                pass

            config.sync()

        def deleteIconCache():
            try:
                os.remove("/var/tmp/kdecache-%s/icon-cache.kcache" % os.environ.get("USER"))
            except:
                pass

            # FIXME:
            #for i in range(kdeui.KIconLoader.LastGroup):
            #    kdeui.KGlobalSettings.self().emitChange(kdeui.KGlobalSettings.IconChanged, i)

        # Theme Settings
        if self.styleSettings["hasChanged"]:
#            if self.styleSettings["iconChanged"]:
#                hasChanged = True
#                configKdeGlobals = QSettings("kdeglobals")
#                group = configKdeGlobals.group("General")
#
#                groupIconTheme = configKdeGlobals.group("Icons")
#                groupIconTheme.writeEntry("Theme", self.styleSettings["iconTheme"])
#
#                configKdeGlobals.sync()
#
#                # Change Icon theme
#                kdeui.KIconTheme.reconfigure()
#                kdeui.KIconCache.deleteCache()
#                deleteIconCache()

            if self.styleSettings["styleChanged"]:
                hasChanged = True
                configKdeGlobals = QSettings("kdeglobals")
                # FIXME
                #group = configKdeGlobals.group("General")
                #group.writeEntry("widgetStyle", self.styleSettings["styleDetails"][str(self.styleSettings["styleName"])]["widgetStyle"])

                #groupIconTheme = configKdeGlobals.group("Icons")
                #groupIconTheme.writeEntry("Theme", self.styleSettings["iconTheme"])
                #groupIconTheme.writeEntry("Theme", self.styleSettings["styleDetails"][str(self.styleSettings["styleName"])]["iconTheme"])

                configKdeGlobals.sync()

                # FIXME:
                # Change Icon theme
                #kdeui.KIconTheme.reconfigure()
                #kdeui.KIconCache.deleteCache()
                deleteIconCache()

                #for i in range(kdeui.KIconLoader.LastGroup):
                #    kdeui.KGlobalSettings.self().emitChange(kdeui.KGlobalSettings.IconChanged, i)

                # Change widget style & color
                for key, value in self.styleSettings["styleDetails"][str(self.styleSettings["styleName"])]["colorScheme"].items():
                    colorGroup = configKdeGlobals.group(key)
                    for key2, value2 in value.items():
                            colorGroup.writeEntry(str(key2), str(value2))

                configKdeGlobals.sync()
                #kdeui.KGlobalSettings.self().emitChange(kdeui.KGlobalSettings.StyleChanged)

                configPlasmaRc = QSettings("plasmarc")
                # FIXME
                #groupDesktopTheme = configPlasmaRc.group("Theme")
                #groupDesktopTheme.writeEntry("name", self.styleSettings["styleDetails"][str(self.styleSettings["styleName"])]["desktopTheme"])
                configPlasmaRc.sync()

                configPlasmaApplet = QSettings("plasma-desktop-appletsrc")
                # FIXME
                #group = configPlasmaApplet.group("Containments")
                #for each in list(group.groupList()):
                #    subgroup = group.group(each)
                #    subcomponent = subgroup.readEntry('plugin')
                #    if subcomponent == 'panel':
                #        #print subcomponent
                #        subgroup.writeEntry('location', self.styleSettings["styleDetails"][str(self.styleSettings["styleName"])]["panelPosition"])

                configPlasmaApplet.sync()

                configKwinRc = QSettings("kwinrc")
                # FIXME
                #groupWindowDecoration = configKwinRc.group("Style")
                #groupWindowDecoration.writeEntry("PluginLib", self.styleSettings["styleDetails"][str(self.styleSettings["styleName"])]["windowDecoration"])
                configKwinRc.sync()

            session = dbus.SessionBus()

            try:
                proxy = session.get_object('org.kde.kwin', '/KWin')
                proxy.reconfigure()
            except dbus.DBusException:
                pass

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

        # Extra Settings
        if self.extraSettings["hasChanged"]:
            if self.extraSettings["enableExtra"]:
                rootActions += "enable_extra "
            else:
                rootActions += "disable_extra "

        if hasChanged:
            self.killPlasma()

        if not rootActions == "":
            os.system("kdesu konsole -e kapudan-rootactions " + rootActions)

        return True
