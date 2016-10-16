# -*- coding: utf-8 -*-

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QSize, QTranslator, QLocale, QStandardPaths
from PyQt5.QtWidgets import QFileDialog

#from PyQt5.QtCore import *
from PyQt5.QtCore import QCoreApplication
import os
import glob

from kapudan.screen import Screen
from kapudan.screens.ui_scrWallpaper import Ui_wallpaperWidget
from kapudan.screens.wallpaperItem import WallpaperItemWidget

from kapudan.tools.desktop_parser import DesktopParser


class Widget(QtWidgets.QWidget, Screen):
    screenSettings = {}
    screenSettings["hasChanged"] = False

    # title and description at the top of the dialog window
    title = QCoreApplication.translate("Widget", "Wallpaper")
    desc = QCoreApplication.translate("Widget", "Choose a Wallpaper")

    def __init__(self, *args):
        QtWidgets.QWidget.__init__(self, None)
        self.ui = Ui_wallpaperWidget()
        self.ui.setupUi(self)
        # Get system locale
        self.catLang = QLocale.system().name()

        # Get screen resolution
        # rect = QtGui.QDesktopWidget().screenGeometry() FIXME: where could
        # this be needed?

        # Get metadata.desktop files from shared wallpaper directory
        # FIXME use QStandardPaths.GenericConfigLocation + "wallpapers"

        for desktopFiles in glob.glob('/usr/share/wallpapers/**/*metadata.desktop', recursive=True):
            parser = DesktopParser()
            parser.read(str(desktopFiles))

            try:
                wallpaperTitle = parser.get_locale('Desktop Entry', 'Name[%s]' % self.catLang, '')
            except:
                wallpaperTitle = parser.get_locale('Desktop Entry', 'Name', '')

            try:
                wallpaperDesc = parser.get_locale('Desktop Entry', 'X-KDE-PluginInfo-Author', '')
            except:
                wallpaperDesc = "Unknown"

            # Get all files in the wallpaper's directory
            try:
                thumbFolder = os.listdir(os.path.join(os.path.split(str(desktopFiles))[0], "contents"))
            except OSError:
                thumbFolder = os.listdir(os.path.join(os.path.split(str(desktopFiles))[0], "content"))

            """
            Appearantly the thumbnail names doesn't have a standard.
            So we get the file list from the contents folder and
            choose the file which has a name that starts with "scre".

            File names I've seen so far;
            screenshot.jpg, screnshot.jpg, screenshot.png, screnshot.png
            """

            wallpaperThumb = ""

            for thumb in thumbFolder:
                if thumb.startswith('scre'):
                    wallpaperThumb = os.path.join(os.path.split(str(desktopFiles))[0], "contents/" + thumb)

            wallpaperFile = os.path.split(str(desktopFiles))[0]

            # Insert wallpapers to listWidget.
            item = QtWidgets.QListWidgetItem(self.ui.listWallpaper)
            # Each wallpaper item is a widget. Look at widgets.py for more information.
            widget = WallpaperItemWidget(wallpaperTitle, wallpaperDesc, wallpaperThumb, self.ui.listWallpaper)
            item.setSizeHint(QSize(120, 170))
            self.ui.listWallpaper.setItemWidget(item, widget)
            # Add a hidden value to each item for detecting selected wallpaper's path.
            item.setStatusTip(wallpaperFile)

        self.ui.listWallpaper.itemSelectionChanged.connect(self.setWallpaper)
        self.ui.checkBox.stateChanged.connect(self.disableWidgets)
        self.ui.buttonChooseWp.clicked.connect(self.selectWallpaper)

    def disableWidgets(self, state):
        if state:
            self.__class__.screenSettings["hasChanged"] = False
            self.ui.buttonChooseWp.setDisabled(True)
            self.ui.listWallpaper.setDisabled(True)
        else:
            self.__class__.screenSettings["hasChanged"] = True
            self.ui.buttonChooseWp.setDisabled(False)
            self.ui.listWallpaper.setDisabled(False)

    def setWallpaper(self):
        self.__class__.screenSettings["selectedWallpaper"] = self.ui.listWallpaper.currentItem().statusTip()
        self.__class__.screenSettings["hasChanged"] = True

    def selectWallpaper(self):
        selectedFile = QFileDialog.getOpenFileName(None, "Open Image", os.environ["HOME"], 'Image Files (*.png *.jpg *.bmp)')

        if selectedFile.isNull():
            return
        else:
            item = QtWidgets.QListWidgetItem(self.ui.listWallpaper)
            wallpaperName = os.path.splitext(os.path.split(str(selectedFile))[1])[0]
            widget = WallpaperItemWidget(wallpaperName, str("Unknown"), selectedFile,
                                         self.ui.listWallpaper)
            item.setSizeHint(QSize(120, 170))
            self.ui.listWallpaper.setItemWidget(item, widget)
            item.setStatusTip(selectedFile)
            self.ui.listWallpaper.setCurrentItem(item)
            self.resize(120, 170)

    def shown(self):
        pass

    def execute(self):
        return True
