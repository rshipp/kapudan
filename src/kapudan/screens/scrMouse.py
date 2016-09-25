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
from kapudan.screens.ui_scrMouse import Ui_mouseWidget

from Xlib import display
RIGHT_HANDED, LEFT_HANDED = range(2)


class Widget(QtWidgets.QWidget, Screen):
    screenSettings = {}
    screenSettings["hasChanged"] = False

    # title and description at the top of the dialog window
    title = QCoreApplication.translate("kapudan", "Mouse")
    desc = QCoreApplication.translate("kapudan", "Setup Mouse Behavior")

    def __init__(self, *args):
        QtWidgets.QWidget.__init__(self, None)
        self.ui = Ui_mouseWidget()
        self.ui.setupUi(self)

        # Our default click behavior is single click. So make SingleClick = true (kdeglobals)
        self.clickBehavior = True

        # read default settings
        try:
            config = QSettings("kcminputrc")
            group = config.group("Mouse")
            self.__class__.screenSettings["selectedMouse"] = group.readEntry("MouseButtonMapping")

            config = QSettings("kdeglobals")
            group = config.group("KDE")

            self.__class__.screenSettings["selectedBehavior"] = str(group.readEntry("SingleClick"))
            # TODO: change this, put single click on top in the ui
            self.ui.singleClick.setChecked(True)

            self.ui.singleClick.setChecked(self.str2bool(self.__class__.screenSettings["selectedBehavior"]))
            self.clickBehavior = self.str2bool(self.__class__.screenSettings["selectedBehavior"])

            if self.__class__.screenSettings["selectedMouse"] == "LeftHanded":
                self.ui.radioButtonLeftHand.setChecked(True)

        except:
            pass

        # set signals
        self.ui.radioButtonRightHand.toggled.connect(self.setHandedness)
        self.ui.checkReverse.toggled.connect(self.setHandedness)
        self.ui.singleClick.clicked.connect(self.clickBehaviorToggle)
        self.ui.DoubleClick.clicked.connect(self.clickBehaviorToggle)

    def str2bool(self, s):
        return bool(eval(s).capitalize())

    def clickBehaviorToggle(self):
        self.clickBehavior = self.ui.singleClick.isChecked()

    def getMouseMap(self):
        self.mapMouse = {}

        if self.ui.radioButtonRightHand.isChecked():
            self.handed = RIGHT_HANDED

        else:
            self.handed = LEFT_HANDED

        self.mapMouse = display.Display().get_pointer_mapping()
        self.num_buttons = len(self.mapMouse)

    def setHandedness(self, item):
        self.getMouseMap()

        # mouse has 1 button
        if self.num_buttons == 1:
            self.mapMouse[0] = 1

        # mouse has 2 buttons
        elif self.num_buttons == 2:
            if self.handed == RIGHT_HANDED:
                self.mapMouse[0], self.mapMouse[1] = 1, 3
            else:
                self.mapMouse[0], self.mapMouse[1] = 3, 1

        # mouse has 3 or more buttons
        else:
            if self.handed == RIGHT_HANDED:
                self.mapMouse[0], self.mapMouse[2] = 1, 3
            else:
                self.mapMouse[0], self.mapMouse[2] = 3, 1

            if self.num_buttons >= 5:
                # get wheel position
                for pos in range(0, self.num_buttons):
                    if self.mapMouse[pos] in (4, 5):
                        break

                if pos < self.num_buttons - 1:
                    if self.ui.checkReverse.isChecked():
                        self.mapMouse[pos], self.mapMouse[pos + 1] = 5, 4
                    else:
                        self.mapMouse[pos], self.mapMouse[pos + 1] = 4, 5

        display.Display().set_pointer_mapping(self.mapMouse)

        config = QSettings("kcminputrc")
        group = config.group("Mouse")

        if self.handed == RIGHT_HANDED:
            group.writeEntry("MouseButtonMapping", "RightHanded")
            self.__class__.screenSettings["selectedMouse"] = "RightHanded"
        else:
            group.writeEntry("MouseButtonMapping", "LeftHanded")
            self.__class__.screenSettings["selectedMouse"] = "LeftHanded"

        group.writeEntry("ReverseScrollPolarity", str(self.ui.checkReverse.isChecked()))
        config.sync()

        #KGlobalSettings.self().emitChange(KGlobalSettings.SettingsChanged, KGlobalSettings.SETTINGS_MOUSE)

    def shown(self):
        pass

    def execute(self):
        self.__class__.screenSettings["summaryMessage"] = {}

        self.__class__.screenSettings["summaryMessage"].update({"selectedMouse": QCoreApplication.translate("kapudan", "Left Handed") if self.__class__.screenSettings["selectedMouse"] == "LeftHanded" else QCoreApplication.translate("kapudan", "Right Handed")})
        self.__class__.screenSettings["summaryMessage"].update({"clickBehavior": QCoreApplication.translate("kapudan", "Single Click ") if self.clickBehavior else QCoreApplication.translate("kapudan", "Double Click")})

        config = QSettings("kdeglobals")
        group = config.group("KDE")
        group.writeEntry("SingleClick", str(self.clickBehavior))

        config.sync()
        #KGlobalSettings.self().emitChange(KGlobalSettings.SettingsChanged, KGlobalSettings.SETTINGS_MOUSE)

        return True
