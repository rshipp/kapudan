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

import os
from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyKDE4.kdecore import ki18n

from kapudan.screen import Screen
from kapudan.screens.ui_scrFolder import Ui_folderWidget


class Widget(QtGui.QWidget, Screen):
    screenSettings = {}
    screenSettings["hasChanged"] = False

    # title and description at the top of the dialog window
    title = ki18n("Folder")
    desc = ki18n("Create folders in the home directory")

    def __init__(self, *args):
        QtGui.QWidget.__init__(self, None)
        self.ui = Ui_folderWidget()
        self.ui.setupUi(self)

        # read default settings
        self.download_path  = os.path.expanduser("~/Downloads")
        self.documents_path = os.path.expanduser("~/Documents")
        self.video_path     = os.path.expanduser("~/Video")
        self.music_path     = os.path.expanduser("~/Music")
        self.image_path     = os.path.expanduser("~/Images")

        self.download  = os.path.isdir(self.download_path)
        self.documents = os.path.isdir(self.download_path)
        self.video     = os.path.isdir(self.download_path)
        self.music     = os.path.isdir(self.download_path)
        self.image     = os.path.isdir(self.download_path)

        # set signals
        self.connect(self.ui.documentsFolderButton, SIGNAL("toggled(bool)"), self.addFolder)
        self.connect(self.ui.downloadFolderButton, SIGNAL("toggled(bool)"), self.addFolder)
        self.connect(self.ui.imageFolderButton, SIGNAL("toggled(bool)"), self.addFolder)
        self.connect(self.ui.musicFolderButton, SIGNAL("toggled(bool)"), self.addFolder)
        self.connect(self.ui.videoFolderButton, SIGNAL("toggled(bool)"), self.addFolder)

    def addFolder(self, item):
        self.download  = self.ui.downloadFolderButton.isChecked()
        self.image     = self.ui.imageFolderButton.isChecked()
        self.documents = self.ui.documentsFolderButton.isChecked()
        self.music     = self.ui.musicFolderButton.isChecked()
        self.video     = self.ui.videoFolderButton.isChecked()

    def shown(self):
        pass

    def execute(self):
        #self.__class__.screenSettings["summaryMessage"] = {}

        #self.__class__.screenSettings["summaryMessage"].update({"selectedMouse": ki18n("Left Handed") if self.__class__.screenSettings["selectedMouse"] == "LeftHanded" else ki18n("Right Handed")})
        #self.__class__.screenSettings["summaryMessage"].update({"clickBehavior": ki18n("Single Click ") if self.clickBehavior else ki18n("Double Click")})

        return True
