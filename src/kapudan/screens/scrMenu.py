import os

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication, QSettings

from kapudan.screen import Screen
from kapudan.screens.ui_scrMenu import Ui_menuWidget
from kapudan.tools.config import Parser

MENU_KICKOFF = "org.kde.plasma.kickoff"
MENU_KICKER = "org.kde.plasma.kicker"
MENU_KICKERDASH = "org.kde.plasma.kickerdash"


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

        self.menuNames = {}
        self.menuNames[MENU_KICKOFF] = {
            "menuIndex": 0,
            "summaryMessage": QCoreApplication.translate("kapudan", "Application Launcher"),
            "image": QtGui.QPixmap(':/raw/pixmap/kickoff.png'),
            "description": QCoreApplication.translate("kapudan", "Application Launcher is the default menu in Chakra.<br><br>The program shortcuts are easy to access and well organized.")
        }
        self.menuNames[MENU_KICKER] = {
            "menuIndex": 1,
            "summaryMessage": QCoreApplication.translate("kapudan", "Application Menu"),
            "image": QtGui.QPixmap(':/raw/pixmap/simple.png'),
            "description": QCoreApplication.translate("kapudan", "Application Menu is an old style menu from KDE 3.<br><br>It is a very lightweight menu thus it is recommended for slower PC's.")
        }
        self.menuNames[MENU_KICKERDASH] = {
            "menuIndex": 2,
            "summaryMessage": QCoreApplication.translate("kapudan", "Application Dashboard"),
            "image": QtGui.QPixmap(':/raw/pixmap/homerun-kicker.png'),
            "description": QCoreApplication.translate("kapudan", "Application Dashboard is a fullscreen menu.<br><br>The program shortcuts are easy to access and well organized.")
        }

        self.ui.pictureMenuStyles.setPixmap(self.menuNames[self.selectedMenu]["image"])
        self.ui.labelMenuDescription.setText(self.menuNames[self.selectedMenu]["description"])
        self.ui.menuStyles.setCurrentIndex(self.menuNames[self.selectedMenu]["menuIndex"])

        self.ui.menuStyles.activated.connect(self.setMenuStyle)

    # Class properties
    @property
    def selectedMenu(self):
        return self.__class__.screenSettings.get("selectedMenu", MENU_KICKOFF)

    @selectedMenu.setter
    def selectedMenu(self, value):
        self.__class__.screenSettings["selectedMenu"] = value

    # UI methods
    def setMenuStyle(self, enee):
        self.__class__.screenSettings["hasChanged"] = True
        currentIndex = self.ui.menuStyles.currentIndex()

        if currentIndex == 0:
            self.setMenu(MENU_KICKOFF)
        elif currentIndex == 1:
            self.setMenu(MENU_KICKER)
        elif currentIndex == 2:
            self.setMenu(MENU_KICKERDASH)

    def setMenu(self, menu):
        self.selectedMenu = menu

        self.ui.pictureMenuStyles.setPixmap(self.menuNames[menu]["image"])
        self.ui.labelMenuDescription.setText(self.menuNames[menu]["description"])

    # Screen methods
    def shown(self):
        pass

    def execute(self):
        self.__class__.screenSettings["summaryMessage"] = self.menuNames[self.selectedMenu]["summaryMessage"]

        configFile = os.path.join(os.path.expanduser("~"), ".config",
            "plasma-org.kde.plasma.desktop-appletsrc")
        parser = Parser(configFile)
        parser.setMenuStyleOrCreate(self.selectedMenu)

        return True
