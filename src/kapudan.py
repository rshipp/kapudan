#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os

from PyQt4 import QtCore, QtGui
from PyKDE4 import kdeui
from PyKDE4.kdecore import ki18n, KAboutData, KCmdLineArgs, KConfig

from kapudan.screens.ui_kapudan import Ui_kapudan

from kapudan.tools import tools
from kapudan.tools.progress_pie import DrawPie
from kapudan.tools.kapudan_menu import Menu
import kapudan.kapudan_rc


class Kapudan(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.initializeGlobals()
        self.initializeUI()
        self.signalHandler()

    def initializeGlobals(self):
        ''' initializes global variables '''
        self.screenData = None
        self.moveInc = 1
        self.menuText = ""
        self.titles = []
        self.descriptions = []
        self.currentDir = os.path.dirname(os.path.realpath(__file__))
        self.screensPath = self.currentDir + "/kapudan/screens/scr*py"
        self.kapudanConfig = KConfig("kapudanrc")
        self.plasmaConfig = KConfig("plasma-desktop-appletsrc")

    def signalHandler(self):
        ''' connects signals to slots '''
        self.ui.buttonNext.clicked.connect(self.slotNext)
        self.ui.buttonApply.clicked.connect(self.slotNext)
        self.ui.buttonBack.clicked.connect(self.slotBack)
        self.ui.buttonFinish.clicked.connect(self.slotCleanup)
        self.ui.buttonCancel.clicked.connect(QtGui.qApp.quit)

    def initializeUI(self):
        ''' initializes the human interface '''
        self.ui = Ui_kapudan()
        self.ui.setupUi(self)

        # load screens
        tools.loadScreens(self.screensPath, globals())

        # kapudan screen settings
        self.headScreens = [scrWelcome, scrFolder, scrMouse, scrStyle, scrMenu, scrWallpaper]
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
        ''' appends unsorted screens to the list '''
        screens = []

        allScreens = [value for key, value in globals().iteritems() if key.startswith("scr")]

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
        ''' returns the id of current stack '''
        new = self.ui.mainStack.currentIndex() + d
        total = self.ui.mainStack.count()
        if new < 0:
            new = 0
        if new > total:
            new = total
        return new

    def setCurrent(self, id=None):
        ''' move to id numbered step '''
        if id:
            self.stackMove(id)

    def slotNext(self, dryRun=False):
        ''' execute next step '''
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
        ''' execute previous step '''
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
        ''' move to id numbered stack '''
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
        ''' create all widgets and add inside stack '''
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

    def __del__(self):
        group = self.kapudanConfig.group("General")
        group.writeEntry("RunOnStart", "False")

if __name__ == "__main__":
    appName = "kapudan"
    catalog = ""
    programName = ki18n("kapudan")
    version = "2013.02"
    description = ki18n("Kapudan lets you configure your Chakra installation at first boot.")
    license = KAboutData.License_GPL
    copyright = ki18n("(c) 2013 The Chakra Developers")
    text = ki18n("none")
    homePage = "http://gitorious.org/chakra/kapudan"
    bugEmail = "george@chakra-project.org"

    aboutData = KAboutData(appName, catalog, programName, version, description,
                           license, copyright, text, homePage, bugEmail)

    KCmdLineArgs.init(sys.argv, aboutData)
    app = kdeui.KApplication()

    # attach dbus to main loop
    tools.DBus()

    kapudan = Kapudan()
    kapudan.show()
    tools.centerWindow(kapudan)
    app.exec_()
