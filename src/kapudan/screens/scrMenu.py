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
from PyKDE4.kdecore import i18n, KConfig

from kapudan.screen import Screen
from kapudan.screens.ui_scrMenu import Ui_menuWidget


class Widget(QtGui.QWidget, Screen):
    screenSettings = {}
    screenSettings["hasChanged"] = False

    # Set title and description for the information widget
    title = i18n("Menu")
    desc = i18n("Choose a Menu Style")

    def __init__(self, *args):
        QtGui.QWidget.__init__(self, None)
        self.ui = Ui_menuWidget()
        self.ui.setupUi(self)

        # read default menu style first
        config = KConfig("plasma-desktop-appletsrc")
        group = config.group("Containments")

        self.menuNames = {}
        self.menuNames["launcher"] = {
            "menuIndex": 0,
            "summaryMessage": i18n("Kick-off Menu"),
            "image": QtGui.QPixmap(':/raw/pixmap/kickoff.png'),
            "description": i18n("Kick-off menu is the default menu of Chakra.<br><br>The program shortcuts are easy to access and well organized.")
        }
        self.menuNames["simplelauncher"] = {
            "menuIndex": 1,
            "summaryMessage": i18n("Simple Menu"),
            "image": QtGui.QPixmap(':/raw/pixmap/simple.png'),
            "description": i18n("Simple menu is an old style menu from KDE 3.<br><br>It is a very lightweight menu thus it is recommended for slower PC's.")
        }
        self.menuNames["lancelot_launcher"] = {
            "menuIndex": 2,
            "summaryMessage": i18n("Lancelot Menu"),
            "image": QtGui.QPixmap(':/raw/pixmap/lancelot.png'),
            "description": i18n("Lancelot is an advanced and highly customizable menu for Chakra.<br><br>The program shortcuts are easy to access and well organized.")
        }
        self.menuNames["homerun_launcher"] = {
            "menuIndex": 3,
            "summaryMessage": i18n("Homerun Menu"),
            "image": QtGui.QPixmap(':/raw/pixmap/homerun.png'),
            "description": i18n("Homerun is a full screen launcher with content organized in tabs.")
        }
        self.menuNames["appmenu_launcher"] = {
            "menuIndex": 4,
            "summaryMessage": i18n("AppMenu QML"),
            "image": QtGui.QPixmap(':/raw/pixmap/appmenu-qml.png'),
            "description": i18n("This plasmoid shows a menu of the installed applications, similar to Lancelot but much simpler")
        }

        for each in list(group.groupList()):
            subgroup = group.group(each)
            subcomponent = subgroup.readEntry('plugin')
            if subcomponent == 'panel':
                subg = subgroup.group('Applets')
                for i in list(subg.groupList()):
                    subg2 = subg.group(i)
                    launcher = subg2.readEntry('plugin')
                    if str(launcher).find('launcher') >= 0:
                        self.__class__.screenSettings["selectedMenu"] = subg2.readEntry('plugin')

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
            self.__class__.screenSettings["selectedMenu"] = 'homerun_launcher'

            self.ui.pictureMenuStyles.setPixmap(self.menuNames["homerun_launcher"]["image"])
            self.ui.labelMenuDescription.setText(self.menuNames["homerun_launcher"]["description"])
        elif currentIndex == 4:
            self.__class__.screenSettings["selectedMenu"] = "appmenu_launcher"

            self.ui.pictureMenuStyles.setPixmap(self.menuNames["appmenu_launcher"]["image"])
            self.ui.labelMenuDescription.setText(self.menuNames["appmenu_launcher"]["description"])

    def shown(self):
        pass

    def execute(self):
        self.__class__.screenSettings["summaryMessage"] = self.menuNames[str(self.__class__.screenSettings["selectedMenu"])]["summaryMessage"]
        return True
