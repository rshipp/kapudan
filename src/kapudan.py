#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets

from kapudan.screens.ui_kapudan import Ui_kapudan

from kapudan.tools import tools
from kapudan.tools.progress_pie import DrawPie
from kapudan.tools.kapudan_menu import Menu
import kapudan.kapudan_rc


class Kapudan(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.initializeGlobals()
        self.initializeUI()
        self.signalHandler()

    def initializeGlobals(self):
        """Initialize global variables"""
        self.screenData = None
        self.moveInc = 1
        self.menuText = ""
        self.titles = []
        self.descriptions = []
        self.currentDir = os.path.dirname(os.path.realpath(__file__))
        self.screensPath = self.currentDir + "/kapudan/screens/scr*py"

    def signalHandler(self):
        """Connect signals to slots"""
        self.ui.buttonNext.clicked.connect(self.slotNext)
        self.ui.buttonApply.clicked.connect(self.slotNext)
        self.ui.buttonBack.clicked.connect(self.slotBack)
        self.ui.buttonFinish.clicked.connect(self.slotCleanup)
        self.ui.buttonCancel.clicked.connect(QtCore.QCoreApplication.exit)

    def initializeUI(self):
        """Initialize the human interface"""
        self.ui = Ui_kapudan()
        self.ui.setupUi(self)

        # load screens
        tools.loadScreens(self.screensPath, globals())

        # kapudan screen settings
        self.headScreens = [scrWelcome, scrFolder, scrMouse, scrMenu, scrWallpaper]
        self.tailScreens = [scrSummary, scrGoodbye]
        self.screens = self.screenOrganizer(self.headScreens, self.tailScreens)

        # Add screens to StackWidget
        self.createWidgets(self.screens)

        # Get Screen Titles
        for screen in self.screens:
            title = screen.Widget.title
            self.titles.append(title)

        # draw progress pie
        self.countScreens = len(self.screens)
        self.pie = DrawPie(self.countScreens, self.ui.labelProgress)

        # Initialize Menu
        self.menu = Menu(self.titles, self.ui.labelMenu)
        self.menu.start()

    def screenOrganizer(self, headScreens, tailScreens):
        """Append unsorted screens to the list"""
        screens = []

        allScreens = [value for key, value in globals().items() if key.startswith("scr")]

        otherScreens = list((set(allScreens) - set(headScreens)) - set(tailScreens))
        otherScreens.remove(scrPackage)
        otherScreens.remove(scrServices)
        otherScreens.remove(scrSecurity)

        screens.extend(headScreens)
        screens.extend(otherScreens)

        screens.append(scrPackage)

        screens.append(scrServices)
        screens.append(scrSecurity)

        screens.extend(tailScreens)

        return screens

    def getCur(self, d):
        """Return the id of current stack"""
        new = self.ui.mainStack.currentIndex() + d
        total = self.ui.mainStack.count()
        if new < 0:
            new = 0
        if new > total:
            new = total
        return new

    def setCurrent(self, id=None):
        """Move to the given step"""
        if id:
            self.stackMove(id)

    def slotNext(self, dryRun=False):
        """Execute the next step"""
        self.menuText = ""
        curIndex = self.ui.mainStack.currentIndex() + 1

        # update pie progress
        self.pie.updatePie(curIndex)

        # animate menu
        self.menu.next()

        _w = self.ui.mainStack.currentWidget()

        ret = _w.execute()
        if ret:
            self.stackMove(self.getCur(self.moveInc))
            self.moveInc = 1

    def slotBack(self):
        """Execute the previous step"""
        self.menuText = ""
        curIndex = self.ui.mainStack.currentIndex()

        # update pie progress
        self.pie.updatePie(curIndex - 1)

        # animate menu
        self.menu.prev()

        _w = self.ui.mainStack.currentWidget()

        _w.backCheck()
        self.stackMove(self.getCur(self.moveInc * -1))
        self.moveInc = 1

    def stackMove(self, id):
        """Move to the given stack"""
        if not id == self.ui.mainStack.currentIndex() or id == 0:
            self.ui.mainStack.setCurrentIndex(id)

            # Set screen title
            self.ui.screenTitle.setText(self.descriptions[id])

            _w = self.ui.mainStack.currentWidget()
            _w.update()
            _w.shown()

        if self.ui.mainStack.currentIndex() == len(self.screens) - 3:
            self.ui.buttonNext.show()
            self.ui.buttonApply.hide()
            self.ui.buttonFinish.hide()

        if self.ui.mainStack.currentIndex() == len(self.screens) - 2:
            self.ui.buttonNext.hide()
            self.ui.buttonApply.show()
            self.ui.buttonFinish.hide()

        if self.ui.mainStack.currentIndex() == len(self.screens) - 1:
            self.ui.buttonApply.hide()
            self.ui.buttonFinish.show()

        if self.ui.mainStack.currentIndex() == 0:
            self.ui.buttonBack.hide()
            self.ui.buttonFinish.hide()
            self.ui.buttonApply.hide()
        else:
            self.ui.buttonBack.show()

    def createWidgets(self, screens=[]):
        """Create all widgets and add them to the stack"""
        self.ui.mainStack.removeWidget(self.ui.page)
        for screen in screens:
            _scr = screen.Widget()

            # Append screen descriptions to list
            self.descriptions.append(_scr.desc)

            # Append screens to stack widget
            self.ui.mainStack.addWidget(_scr)

        self.stackMove(0)

    def disableNext(self):
        self.buttonNext.setEnabled(False)

    def disableBack(self):
        self.buttonBack.setEnabled(False)

    def enableNext(self):
        self.buttonNext.setEnabled(True)

    def enableBack(self):
        self.buttonBack.setEnabled(True)

    def isNextEnabled(self):
        return self.buttonNext.isEnabled()

    def isBackEnabled(self):
        return self.buttonBack.isEnabled()

    def slotCleanup(self):
        _w = self.ui.mainStack.currentWidget()
        if _w.execute():
            self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # attach dbus to main loop
    tools.DBus()

    kapudan = Kapudan()
    kapudan.show()
    tools.centerWindow(kapudan)
    app.exec_()
