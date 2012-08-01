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
    title = ki18n("Folders")
    desc = ki18n("Create folders in the home directory")

    def __init__(self, *args):
        QtGui.QWidget.__init__(self, None)
        self.ui = Ui_folderWidget()
        self.ui.setupUi(self)

        # read default settings
        self.folder_paths = dict()
        self.folder_paths["download"]  = os.path.expanduser("~/Downloads")
        self.folder_paths["documents"] = os.path.expanduser("~/Documents")
        self.folder_paths["video"]     = os.path.expanduser("~/Videos")
        self.folder_paths["music"]     = os.path.expanduser("~/Music")
        self.folder_paths["image"]     = os.path.expanduser("~/Images")

        self.folder = dict()
        self.folder["download"]  = os.path.isdir(self.folder_paths["download"])
        self.folder["documents"] = os.path.isdir(self.folder_paths["documents"])
        self.folder["video"]     = os.path.isdir(self.folder_paths["video"])
        self.folder["music"]     = os.path.isdir(self.folder_paths["music"])
        self.folder["image"]     = os.path.isdir(self.folder_paths["image"])

        self.folder2button = dict()
        self.folder2button["download"]  = self.ui.downloadFolderButton
        self.folder2button["documents"] = self.ui.documentsFolderButton
        self.folder2button["video"]     = self.ui.videoFolderButton
        self.folder2button["music"]     = self.ui.musicFolderButton
        self.folder2button["image"]     = self.ui.imageFolderButton

        for key, value in self.folder.iteritems():
            if value:
                self.folder2button[key].setChecked(True)

        # set signals
        self.connect(self.ui.documentsFolderButton, SIGNAL("toggled(bool)"), self.addFolder)
        self.connect(self.ui.downloadFolderButton, SIGNAL("toggled(bool)"), self.addFolder)
        self.connect(self.ui.imageFolderButton, SIGNAL("toggled(bool)"), self.addFolder)
        self.connect(self.ui.musicFolderButton, SIGNAL("toggled(bool)"), self.addFolder)
        self.connect(self.ui.videoFolderButton, SIGNAL("toggled(bool)"), self.addFolder)

    def addFolder(self, item):
        self.folder["download"]  = self.ui.downloadFolderButton.isChecked()
        self.folder["documents"] = self.ui.documentsFolderButton.isChecked()
        self.folder["video"]     = self.ui.imageFolderButton.isChecked()
        self.folder["music"]     = self.ui.musicFolderButton.isChecked()
        self.folder["image"]     = self.ui.videoFolderButton.isChecked()

    def shown(self):
        pass

    def execute(self):
        #self.__class__.screenSettings["summaryMessage"] = {}

        for key, value in self.folder.iteritems():
            try:
                if value:
                    os.mkdir(self.folder_paths[key])
                else:
                    os.rmdir(self.folder_paths[key])
            except OSError:
                # either the directory exists when we try to create it,
                # or it is not empty when we try to delete it
                pass

        return True
