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
from PyKDE4.kdecore import i18n

from kapudan.screen import Screen
from kapudan.screens.ui_scrFolder import Ui_folderWidget
from kapudan.tools.xdg_user_dirs import UserDirs


class Widget(QtGui.QWidget, Screen):
    screenSettings = {}
    screenSettings["hasChanged"] = False

    # title and description at the top of the dialog window
    title = i18n("Folders")
    desc = i18n("Create folders in the home directory")

    def __init__(self, *args):
        QtGui.QWidget.__init__(self, None)
        self.ui = Ui_folderWidget()
        self.ui.setupUi(self)

        userdirs = UserDirs()

        # read default settings
        self.folder_attributes = dict()
        self.folder_attributes["download"] = (userdirs.get('DOWNLOADS'),
                "[Desktop Entry]\nIcon=folder-downloads")
        self.folder_attributes["documents"] = (userdirs.get('DOCUMENTS'),
                "[Desktop Entry]\nIcon=folder-documents")
        self.folder_attributes["video"] = (userdirs.get('VIDEOS'),
                "[Desktop Entry]\nIcon=folder-video")
        self.folder_attributes["music"] = (userdirs.get('MUSIC'),
                "[Desktop Entry]\nIcon=folder-sound")
        self.folder_attributes["picture"] = (userdirs.get('PICTURES'),
                "[Desktop Entry]\nIcon=folder-image")

        # this sets up the old behavior, where folders are not created
        # by default. this behavior is overridden below.
        self.folder = dict()
        self.folder["download"] = os.path.isdir(self.folder_attributes["download"][0])
        self.folder["documents"] = os.path.isdir(self.folder_attributes["documents"][0])
        self.folder["video"] = os.path.isdir(self.folder_attributes["video"][0])
        self.folder["music"] = os.path.isdir(self.folder_attributes["music"][0])
        self.folder["picture"] = os.path.isdir(self.folder_attributes["picture"][0])
        # this tells Kapudan to create all folders by default, as
        # discussed here: https://www.loomio.org/discussions/8411
        for key, value in self.folder.iteritems():
            self.folder[key] = True

        self.folder2button = dict()
        self.folder2button["download"] = self.ui.downloadFolderButton
        self.folder2button["documents"] = self.ui.documentsFolderButton
        self.folder2button["video"] = self.ui.videoFolderButton
        self.folder2button["music"] = self.ui.musicFolderButton
        self.folder2button["picture"] = self.ui.pictureFolderButton

        for key in self.folder2button:
            self.folder2button[key].setStyleSheet("QToolButton:checked {background-color: rgb(120, 120, 120);}")

        for key, value in self.folder.iteritems():
            if value:
                self.folder2button[key].setChecked(True)

        # set signals
        self.ui.documentsFolderButton.toggled.connect(self.addFolder)
        self.ui.downloadFolderButton.toggled.connect(self.addFolder)
        self.ui.pictureFolderButton.toggled.connect(self.addFolder)
        self.ui.musicFolderButton.toggled.connect(self.addFolder)
        self.ui.videoFolderButton.toggled.connect(self.addFolder)

    def addFolder(self):
        for key in self.folder:
            self.folder[key] = self.folder2button[key].isChecked()

    def shown(self):
        pass

    def execute(self):
        for key, value in self.folder.iteritems():
            try:
                if value:
                    os.mkdir(self.folder_attributes[key][0])
                    with open(os.path.join(self.folder_attributes[key][0], ".directory"), "w") as f:
                        f.write(self.folder_attributes[key][1])
                else:
                    content = os.listdir(self.folder_attributes[key][0])
                    if (len(content) == 1) and (".directory" in content):
                        # only delete the directory if it contains
                        # nothing but the .directory file (which
                        # suggests that we created it)
                        os.remove(os.path.join(self.folder_attributes[key][0], ".directory"))
                        os.rmdir(self.folder_attributes[key][0])
            except OSError:
                # either the directory exists when we try to create it,
                # or it is not empty when we try to delete it
                pass

        self.__class__.screenSettings["summaryMessage"] = "Created folders in home directory"

        return True
