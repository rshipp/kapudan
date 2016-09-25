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
from PyQt5.QtCore import QCoreApplication, QSettings

from kapudan.screen import Screen
from kapudan.screens.ui_scrMenu import Ui_menuWidget


class Widget(QtWidgets.QWidget, Screen):
    screenSettings = {}
    screenSettings["hasChanged"] = False

    # Set title and description for the information widget
    title = QCoreApplication.translate("kapudan", "Menu")
    desc = QCoreApplication.translate("kapudan", "Choose a Menu Style")

    def __init__(self, *args):
        QtWidgets.QWidget.__init__(self, None)
        self.ui = Ui_menuWidget()
        self.ui.setupUi(self)

        # read default menu style first
        config = QSettings("plasma-desktop-appletsrc")
        # FIXME
        #group = config.group("Containments")

        self.menuNames = {}
        self.menuNames["launcher"] = {
            "menuIndex": 0,
            "summaryMessage": QCoreApplication.translate("kapudan", "Kick-off Menu"),
            "image": QtWidgets.QPixmap(':/raw/pixmap/kickoff.png'),
            "description": QCoreApplication.translate("kapudan", "Kick-off menu is the default menu of Chakra.<br><br>The program shortcuts are easy to access and well organized.")
        }
        self.menuNames["simplelauncher"] = {
            "menuIndex": 1,
            "summaryMessage": QCoreApplication.translate("kapudan", "Simple Menu"),
            "image": QtWidgets.QPixmap(':/raw/pixmap/simple.png'),
            "description": QCoreApplication.translate("kapudan", "Simple menu is an old style menu from KDE 3.<br><br>It is a very lightweight menu thus it is recommended for slower PC's.")
        }
        self.menuNames["lancelot_launcher"] = {
            "menuIndex": 2,
            "summaryMessage": QCoreApplication.translate("kapudan", "Lancelot Menu"),
            "image": QtWidgets.QPixmap(':/raw/pixmap/lancelot.png'),
            "description": QCoreApplication.translate("kapudan", "Lancelot is an advanced and highly customizable menu for Chakra.<br><br>The program shortcuts are easy to access and well organized.")
        }
        self.menuNames["homerunlauncher"] = {
            "menuIndex": 3,
            "summaryMessage": QCoreApplication.translate("kapudan", "Homerun Menu"),
            "image": QtWidgets.QPixmap(':/raw/pixmap/homerun.png'),
            "description": QCoreApplication.translate("kapudan", "Homerun is a full screen launcher with content organized in tabs.")
        }
        self.menuNames["appmenu-qml"] = {
            "menuIndex": 4,
            "summaryMessage": QCoreApplication.translate("kapudan", "AppMenu QML"),
            "image": QtWidgets.QPixmap(':/raw/pixmap/appmenu-qml.png'),
            "description": QCoreApplication.translate("kapudan", "This plasmoid shows a menu of the installed applications, similar to Lancelot but much simpler")
        }
        self.menuNames["org.kde.homerun-kicker"] = {
            "menuIndex": 5,
            "summaryMessage": QCoreApplication.translate("kapudan", "Homerun Kicker"),
            "image": QtWidgets.QPixmap(':/raw/pixmap/homerun-kicker.png'),
            "description": QCoreApplication.translate("kapudan", "A non-fullscreen version of Homerun.")
        }

        # FIXME:
        #for each in list(group.groupList()):
        #    subgroup = group.group(each)
        #    subcomponent = subgroup.readEntry('plugin')
        #    if subcomponent == 'panel':
        #        subg = subgroup.group('Applets')
        #        for i in list(subg.groupList()):
        #            subg2 = subg.group(i)
        #            launcher = subg2.readEntry('plugin')
        #            if str(launcher).find('launcher') >= 0:
        #                self.__class__.screenSettings["selectedMenu"] = subg2.readEntry('plugin')

        # set menu preview to default menu
        # if default menu could not found, default to kickoff
        if "selectedMenu" not in self.__class__.screenSettings:
            self.__class__.screenSettings["selectedMenu"] = "launcher"

        self.ui.pictureMenuStyles.setPixmap(self.menuNames[str(self.__class__.screenSettings["selectedMenu"])]["image"])
        self.ui.labelMenuDescription.setText(self.menuNames[str(self.__class__.screenSettings["selectedMenu"])]["description"])
        self.ui.menuStyles.setCurrentIndex(self.menuNames[str(self.__class__.screenSettings["selectedMenu"])]["menuIndex"])

        self.ui.menuStyles.activated.connect(self.setMenuStyle)

    def setMenuStyle(self, enee):
        self.__class__.screenSettings["hasChanged"] = True
        currentIndex = self.ui.menuStyles.currentIndex()

        if currentIndex == 0:
            self.__class__.screenSettings["selectedMenu"] = 'launcher'

            self.ui.pictureMenuStyles.setPixmap(self.menuNames["launcher"]["image"])
            self.ui.labelMenuDescription.setText(self.menuNames["launcher"]["description"])
        elif currentIndex == 1:
            self.__class__.screenSettings["selectedMenu"] = 'simplelauncher'

            self.ui.pictureMenuStyles.setPixmap(self.menuNames["simplelauncher"]["image"])
            self.ui.labelMenuDescription.setText(self.menuNames["simplelauncher"]["description"])

        elif currentIndex == 2:
            self.__class__.screenSettings["selectedMenu"] = 'lancelot_launcher'

            self.ui.pictureMenuStyles.setPixmap(self.menuNames["lancelot_launcher"]["image"])
            self.ui.labelMenuDescription.setText(self.menuNames["lancelot_launcher"]["description"])
        elif currentIndex == 3:
            self.__class__.screenSettings["selectedMenu"] = 'homerunlauncher'

            self.ui.pictureMenuStyles.setPixmap(self.menuNames["homerunlauncher"]["image"])
            self.ui.labelMenuDescription.setText(self.menuNames["homerunlauncher"]["description"])
        elif currentIndex == 4:
            self.__class__.screenSettings["selectedMenu"] = "appmenu-qml"

            self.ui.pictureMenuStyles.setPixmap(self.menuNames["appmenu-qml"]["image"])
            self.ui.labelMenuDescription.setText(self.menuNames["appmenu-qml"]["description"])
        elif currentIndex == 5:
            self.__class__.screenSettings["selectedMenu"] = 'org.kde.homerun-kicker'

            self.ui.pictureMenuStyles.setPixmap(self.menuNames["org.kde.homerun-kicker"]["image"])
            self.ui.labelMenuDescription.setText(self.menuNames["org.kde.homerun-kicker"]["description"])

    def shown(self):
        pass

    def execute(self):
        self.__class__.screenSettings["summaryMessage"] = self.menuNames[str(self.__class__.screenSettings["selectedMenu"])]["summaryMessage"]
        return True
