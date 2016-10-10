import os

from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication, QSettings

from kapudan.screen import Screen
from kapudan.screens.ui_scrMouse import Ui_mouseWidget

RIGHT_HANDED = "RightHanded"
LEFT_HANDED = "LeftHanded"


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

        # read default settings
        self.kcminputrc = QSettings(os.path.join(os.path.expanduser("~"), ".config", "kcminputrc"), QSettings.IniFormat)
        self.kdeglobals = QSettings(os.path.join(os.path.expanduser("~"), ".config", "kdeglobals"), QSettings.IniFormat)

        self.handedness = self.kcminputrc.value("Mouse/MouseButtonMapping", RIGHT_HANDED)
        self.reverseScroll = False if self.kcminputrc.value("Mouse/ReverseScrollPolarity", "false").lower() == "false" else True
        self.singleClick = True if self.kdeglobals.value("KDE/SingleClick", "true").lower() == "true" else False
        print(self.kdeglobals.value("KDE/SingleClick", "true").lower())

        if self.handedness == LEFT_HANDED:
            self.ui.radioButtonLeftHand.setChecked(True)

        # set ui defaults
        self.ui.singleClick.setChecked(self.singleClick)
        self.ui.doubleClick.setChecked(not self.singleClick)
        self.ui.checkReverse.setChecked(self.reverseScroll)

        # set signals
        self.ui.radioButtonRightHand.toggled.connect(self.updateHandedness)
        self.ui.checkReverse.toggled.connect(self.updateHandedness)
        self.ui.singleClick.clicked.connect(self.updateClickBehavior)
        self.ui.doubleClick.clicked.connect(self.updateClickBehavior)


    # Class properties
    @property
    def handedness(self):
        """defaultL right handed"""
        return self.__class__.screenSettings.get("handedness", RIGHT_HANDED)

    @handedness.setter
    def handedness(self, value):
        self.__class__.screenSettings["handedness"] = value

    @property
    def singleClick(self):
        """default: true"""
        return self.__class__.screenSettings.get("singleClick", True)

    @singleClick.setter
    def singleClick(self, value):
        self.__class__.screenSettings["singleClick"] = value

    @property
    def reverseScroll(self):
        """default: false"""
        return self.__class__.screenSettings.get("reverseScroll", False)

    @reverseScroll.setter
    def reverseScroll(self, value):
        self.__class__.screenSettings["reverseScroll"] = value

    # UI methods
    def updateClickBehavior(self):
        """True is Single Click, False is Double Click"""
        self.singleClick = self.ui.singleClick.isChecked()

    def updateHandedness(self):
        self.handedness = RIGHT_HANDED if self.ui.radioButtonRightHand.isChecked() else LEFT_HANDED
        self.reverseScroll = self.ui.checkReverse.isChecked()

    # Screen methods
    def shown(self):
        pass

    def execute(self):
        # KDE settings
        self.kcminputrc.setValue("Mouse/MouseButtonMapping", self.handedness)
        self.kcminputrc.setValue("Mouse/ReverseScrollPolarity", self.reverseScroll)
        self.kcminputrc.sync()

        self.kdeglobals.setValue("KDE/SingleClick", self.singleClick)
        self.kdeglobals.sync()

        # Summary text
        self.__class__.screenSettings["summaryMessage"] = {}

        self.__class__.screenSettings["summaryMessage"].update({
            "selectedMouse": QCoreApplication.translate("kapudan", "Left Handed") if self.handedness == LEFT_HANDED else QCoreApplication.translate("kapudan", "Right Handed")
        })
        self.__class__.screenSettings["summaryMessage"].update({
            "singleClick": QCoreApplication.translate("kapudan", "Single Click") if self.singleClick else QCoreApplication.translate("kapudan", "Double Click")
        })

        return True
