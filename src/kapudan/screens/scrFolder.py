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
from PyQt4.QtCore import *
from PyKDE4.kdecore import ki18n

from kapudan.screen import Screen
from kapudan.screens.ui_scrFolder import Ui_folderWidget


class Widget(QtGui.QWidget, Screen):
    screenSettings = {}
    screenSettings["hasChanged"] = False

    # title and description at the top of the dialog window
    title = ki18n("Mouse")
    desc = ki18n("Setup Mouse Behavior")

    def __init__(self, *args):
        QtGui.QWidget.__init__(self, None)
        self.ui = Ui_folderWidget()
        self.ui.setupUi(self)

        # read default settings

        # set signals
        #self.connect(self.ui.radioButtonRightHand, SIGNAL("toggled(bool)"), self.setHandedness)
        #self.connect(self.ui.checkReverse, SIGNAL("toggled(bool)"), self.setHandedness)
        #self.connect(self.ui.singleClick, SIGNAL("clicked()"), self.clickBehaviorToggle)
        #self.connect(self.ui.DoubleClick, SIGNAL("clicked()"), self.clickBehaviorToggle)

    def shown(self):
        pass

    def execute(self):
        #self.__class__.screenSettings["summaryMessage"] = {}

        #self.__class__.screenSettings["summaryMessage"].update({"selectedMouse": ki18n("Left Handed") if self.__class__.screenSettings["selectedMouse"] == "LeftHanded" else ki18n("Right Handed")})
        #self.__class__.screenSettings["summaryMessage"].update({"clickBehavior": ki18n("Single Click ") if self.clickBehavior else ki18n("Double Click")})

        return True
