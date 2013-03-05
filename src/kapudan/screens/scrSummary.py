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
from PyQt4.QtDBus import QDBusInterface
from PyQt4.QtGui import QMessageBox
from PyKDE4.kdecore import i18n, KConfig, KToolInvocation

import os
import time
import dbus

from kapudan.screen import Screen
from kapudan.screens.ui_scrSummary import Ui_summaryWidget
from PyKDE4 import kdeui

# import other widgets to get the latest configuration
#import kapudan.screens.scrFolder as folderWidget
import kapudan.screens.scrWallpaper as wallpaperWidget
import kapudan.screens.scrMouse as mouseWidget
import kapudan.screens.scrStyle as styleWidget
import kapudan.screens.scrMenu as menuWidget
import kapudan.screens.scrAvatar as avatarWidget
import kapudan.screens.scrPackage as packageWidget
import kapudan.screens.scrServices as servicesWidget
import kapudan.screens.scrSecurity as securityWidget

#from kapudan.tools import tools
from kapudan.tools.spunrc import SpunRC


class Widget(QtGui.QWidget, Screen):
    title = i18n("Summary")
    desc = i18n("Save Your Settings")

    def __init__(self, *args):
        QtGui.QWidget.__init__(self, None)
        self.ui = Ui_summaryWidget()
        self.ui.setupUi(self)
        self.plasma_app = "plasma-desktop"
        service = "org.kde." + self.plasma_app
        path = "/MainApplication"
        self.plasma_interface = QDBusInterface(service, path)
        if __debug__:
            assert(self.plasma_interface.isValid())

    def shown(self):
        self.wallpaperSettings = wallpaperWidget.Widget.screenSettings
        self.mouseSettings = mouseWidget.Widget.screenSettings
        self.menuSettings = menuWidget.Widget.screenSettings
        self.styleSettings = styleWidget.Widget.screenSettings
        self.avatarSettings = avatarWidget.Widget.screenSettings
        self.packageSettings = packageWidget.Widget.screenSettings
        self.servicesSettings = servicesWidget.Widget.screenSettings
        self.securitySettings = securityWidget.Widget.screenSettings

        # TODO: make the text generation a bit less cumbersome by putting it
        # into a class (maybe a context manager, so that end is always appended)
        subject = "<p><li><b>%s</b></li><ul>"
        item = "<li>%s</li>"
        end = "</ul></p>"
        content = ""

        content += """<html><body><ul>"""

        # Mouse Settings
        content += (subject % i18n("Mouse Settings"))

        content += (item % i18n("Selected Mouse configuration: <b>%s</b>") % self.mouseSettings["summaryMessage"]["selectedMouse"])
        content += (item % i18n("Selected clicking behavior: <b>%s</b>") % self.mouseSettings["summaryMessage"]["clickBehavior"])
        content += (end)

        # Menu Settings
        content += (subject % i18n("Menu Settings"))
        content += (item % i18n("Selected Menu: <b>%s</b>") % self.menuSettings["summaryMessage"])
        content += (end)

        # Wallpaper Settings
        content += (subject % i18n("Wallpaper Settings"))
        if not self.wallpaperSettings["hasChanged"]:
            content += (item % i18n("You haven't selected any wallpaper."))
        else:
            content += (item % i18n("Selected Wallpaper: <b>%s</b>") % os.path.basename(str(self.wallpaperSettings["selectedWallpaper"])))
        content += (end)

        # Style Settings
        content += (subject % i18n("Style Settings"))

        if not self.styleSettings["hasChanged"]:
            content += (item % i18n("You haven't selected any style."))
        else:
            content += (item % i18n("Selected Style: <b>%s</b>") % unicode(self.styleSettings["summaryMessage"]))

        content += (end)

        # Spun Settings
        if self.packageSettings["hasChanged"]:
            content += (subject % i18n("Package Management Settings"))
            content += (item % i18n("You have enabled or disabled spun."))

            content += (end)

        # Services Settings
        if self.servicesSettings["hasChanged"]:
            svctext = i18n("You have: ")
            content += (subject % i18n("Services Settings"))
            for daemon in self.servicesSettings["daemons"]:
                svctext += daemon.report() + ";"
            content += item % i18n(svctext)
            content += end

        # Security Settings
        if self.securitySettings["hasChanged"]:
            sectext = i18n("You have: ")
            content += (subject % i18n("Security Settings"))
            for daemon in self.securitySettings["daemons"]:
                sectext += daemon.report() + ";"
            content += item % sectext
            content += end

        self.ui.textSummary.setText(content)

    def killPlasma(self):
        try:
            self.plasma_interface.call("quit")
            time.sleep(1)  # TODO get rid of this...
            self.startPlasma()

        except:  # TODO: what exceptions can happen here?
            QMessageBox.critical(self, i18n("Error"), i18n("Cannot restart plasma-desktop. Kapudan will now shut down."))
            kdeui.KApplication.kApplication().quit()

    def startPlasma(self):
        # FIXME: avoid the hardcoding. And maybe even KToolInvocation
        KToolInvocation.startServiceByDesktopPath("/usr/share/autostart/plasma-desktop.desktop")

    def execute(self):
        hasChanged = False
        rootActions = ""

        # Wallpaper Settings
        if self.wallpaperSettings["hasChanged"]:
            hasChanged = True
            if self.wallpaperSettings["selectedWallpaper"]:
                config = KConfig("plasma-desktop-appletsrc")
                group = config.group("Containments")
                for each in list(group.groupList()):
                    subgroup = group.group(each)
                    subcomponent = subgroup.readEntry('plugin')
                    if subcomponent == 'desktop' or subcomponent == 'folderview':
                        subg = subgroup.group('Wallpaper')
                        subg_2 = subg.group('image')
                        subg_2.writeEntry("wallpaper", self.wallpaperSettings["selectedWallpaper"])

        # Menu Settings
        if self.menuSettings["hasChanged"]:
            hasChanged = True
            config = KConfig("plasma-desktop-appletsrc")
            group = config.group("Containments")

            for each in list(group.groupList()):
                subgroup = group.group(each)
                subcomponent = subgroup.readEntry('plugin')
                if subcomponent == 'panel':
                    subg = subgroup.group('Applets')
                    for i in list(subg.groupList()):
                        subg2 = subg.group(i)
                        launcher = subg2.readEntry('plugin')
                        if str(launcher).find('launcher') >= 0:
                            subg2.writeEntry('plugin', self.menuSettings["selectedMenu"])

        def removeFolderViewWidget():
            config = KConfig("plasma-desktop-appletsrc")

            sub_lvl_0 = config.group("Containments")

            for sub in list(sub_lvl_0.groupList()):
                sub_lvl_1 = sub_lvl_0.group(sub)

                if sub_lvl_1.hasGroup("Applets"):
                    sub_lvl_2 = sub_lvl_1.group("Applets")

                    for sub2 in list(sub_lvl_2.groupList()):
                        sub_lvl_3 = sub_lvl_2.group(sub2)
                        plugin = sub_lvl_3.readEntry('plugin')

                        if plugin == 'folderview':
                            sub_lvl_3.deleteGroup()

        # Desktop Type
        if self.styleSettings["hasChangedDesktopType"]:
            hasChanged = True
            config = KConfig("plasma-desktop-appletsrc")
            group = config.group("Containments")

            for each in list(group.groupList()):
                subgroup = group.group(each)
                subcomponent = subgroup.readEntry('plugin')
                subcomponent2 = subgroup.readEntry('screen')
                if subcomponent == 'desktop' or subcomponent == 'folderview':
                    if int(subcomponent2) == 0:
                        subgroup.writeEntry('plugin', self.styleSettings["desktopType"])

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
            config = KConfig("kwinrc")
            group = config.group("Desktops")
            group.writeEntry('Number', self.styleSettings["desktopNumber"])
            group.sync()

            info = kdeui.NETRootInfo(QtGui.QX11Info.display(), kdeui.NET.NumberOfDesktops | kdeui.NET.DesktopNames)
            info.setNumberOfDesktops(int(self.styleSettings["desktopNumber"]))
            info.activate()

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

            for i in range(kdeui.KIconLoader.LastGroup):
                kdeui.KGlobalSettings.self().emitChange(kdeui.KGlobalSettings.IconChanged, i)

        # Theme Settings
        if self.styleSettings["hasChanged"]:
#            if self.styleSettings["iconChanged"]:
#                hasChanged = True
#                configKdeGlobals = KConfig("kdeglobals")
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
                configKdeGlobals = KConfig("kdeglobals")
                group = configKdeGlobals.group("General")
                group.writeEntry("widgetStyle", self.styleSettings["styleDetails"][unicode(self.styleSettings["styleName"])]["widgetStyle"])

                #groupIconTheme = configKdeGlobals.group("Icons")
                #groupIconTheme.writeEntry("Theme", self.styleSettings["iconTheme"])
                #groupIconTheme.writeEntry("Theme", self.styleSettings["styleDetails"][unicode(self.styleSettings["styleName"])]["iconTheme"])

                configKdeGlobals.sync()

                # Change Icon theme
                kdeui.KIconTheme.reconfigure()
                kdeui.KIconCache.deleteCache()
                deleteIconCache()

                for i in range(kdeui.KIconLoader.LastGroup):
                    kdeui.KGlobalSettings.self().emitChange(kdeui.KGlobalSettings.IconChanged, i)

                # Change widget style & color
                for key, value in self.styleSettings["styleDetails"][unicode(self.styleSettings["styleName"])]["colorScheme"].items():
                    colorGroup = configKdeGlobals.group(key)
                    for key2, value2 in value.items():
                            colorGroup.writeEntry(str(key2), str(value2))

                configKdeGlobals.sync()
                kdeui.KGlobalSettings.self().emitChange(kdeui.KGlobalSettings.StyleChanged)

                configPlasmaRc = KConfig("plasmarc")
                groupDesktopTheme = configPlasmaRc.group("Theme")
                groupDesktopTheme.writeEntry("name", self.styleSettings["styleDetails"][unicode(self.styleSettings["styleName"])]["desktopTheme"])
                configPlasmaRc.sync()

                configPlasmaApplet = KConfig("plasma-desktop-appletsrc")
                group = configPlasmaApplet.group("Containments")
                for each in list(group.groupList()):
                    subgroup = group.group(each)
                    subcomponent = subgroup.readEntry('plugin')
                    if subcomponent == 'panel':
                        #print subcomponent
                        subgroup.writeEntry('location', self.styleSettings["styleDetails"][unicode(self.styleSettings["styleName"])]["panelPosition"])

                configPlasmaApplet.sync()

                configKwinRc = KConfig("kwinrc")
                groupWindowDecoration = configKwinRc.group("Style")
                groupWindowDecoration.writeEntry("PluginLib", self.styleSettings["styleDetails"][unicode(self.styleSettings["styleName"])]["windowDecoration"])
                configKwinRc.sync()

            session = dbus.SessionBus()

            try:
                proxy = session.get_object('org.kde.kwin', '/KWin')
                proxy.reconfigure()
            except dbus.DBusException:
                pass

        # Avatar Settings
        if self.avatarSettings["hasChanged"]:
            hasChanged = True

        # Spun Settings
        if self.packageSettings["hasChanged"]:
            spun = SpunRC()
            if spun.isEnabled():
                rootActions += "disable_spun "
            else:
                rootActions += "enable_spun "

        # Services Settings
        for daemon in self.servicesSettings["daemons"]:
            daemon.apply_changes()

        # Security Settings
        for daemon in self.securitySettings["daemons"]:
            daemon.apply_changes()

        if hasChanged:
            self.killPlasma()

        if not rootActions == "":
            os.system("kdesu konsole -e kapudan-rootactions " + rootActions)

        return True
