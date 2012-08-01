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
        self.folder_attributes = dict()
        self.folder_attributes["download"]  = (os.path.expanduser("~/Downloads"), "[Desktop Entry]\nIcon=folder-downloads")
        self.folder_attributes["documents"] = (os.path.expanduser("~/Documents"), "[Desktop Entry]\nIcon=folder-documents")
        self.folder_attributes["video"]     = (os.path.expanduser("~/Videos"), "[Desktop Entry]\nIcon=folder-video")
        self.folder_attributes["music"]     = (os.path.expanduser("~/Music"), "[Desktop Entry]\nIcon=folder-sound")
        self.folder_attributes["image"]     = (os.path.expanduser("~/Images"), "[Desktop Entry]\nIcon=folder-image")

        self.folder = dict()
        self.folder["download"]  = os.path.isdir(self.folder_attributes["download"][0])
        self.folder["documents"] = os.path.isdir(self.folder_attributes["documents"][0])
        self.folder["video"]     = os.path.isdir(self.folder_attributes["video"][0])
        self.folder["music"]     = os.path.isdir(self.folder_attributes["music"][0])
        self.folder["image"]     = os.path.isdir(self.folder_attributes["image"][0])

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
        self.folder["video"]     = self.ui.videoFolderButton.isChecked()
        self.folder["music"]     = self.ui.musicFolderButton.isChecked()
        self.folder["image"]     = self.ui.imageFolderButton.isChecked()

    def shown(self):
        pass

    def execute(self):
        #self.__class__.screenSettings["summaryMessage"] = {}

        for key, value in self.folder.iteritems():
            try:
                if value:
                    os.mkdir(self.folder_attributes[key][0])
                    with open(os.path.join(self.folder_attributes[key][0], ".directory"), "w") as f:
                        f.write(self.folder_attributes[key][1])
                else:
                    content = os.listdir(self.folder_attributes[key][0])
                    if (len(content) == 1) and (".directory" in content):
                        # only delete the directory if we created it
                        os.remove(os.path.join(self.folder_attributes[key][0], ".directory"))
                        os.rmdir(self.folder_attributes[key][0])
            except OSError:
                # either the directory exists when we try to create it,
                # or it is not empty when we try to delete it
                pass

        return True
