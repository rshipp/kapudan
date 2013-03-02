#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import dbus
import glob
import re
from PyQt4.QtGui import QDesktopWidget


def DBus():
    if not dbus.get_default_main_loop():
        from dbus.mainloop.qt import DBusQtMainLoop
        DBusQtMainLoop(set_as_default=True)


def importScreen(screenName):
    ''' imports a screen by name '''
    screen = __import__(screenName)
    for s in screenName.split('.')[1:]:
        screen = getattr(screen, s)
    return screen


def loadScreens(screensPath, globals):
    ''' imports all screens in the specified directory '''
    screens = glob.glob(screensPath)
    for screen in screens:
        screenName = screen.split("/")[-1].split(".")[0]
        globals[screenName] = importScreen("kapudan.screens." + screenName)


def isLiveCD():
    return os.path.exists('/var/run/pardus/livemedia')


def getRelease():
    # we parse /etc/lsb_release manually instead of calling lsb_release
    release_info = "Chakra"
    with open("/etc/lsb-release", "r") as f:
        text = f.read()
        id = re.search('DISTRIB_ID="(?P<id>\w+)"', text).group("id")
        release = re.search('DISTRIB_RELEASE="(?P<release>[0-9.]+)"', text).group("release")
        codename = re.search('DISTRIB_CODENAME="(?P<codename>\w+)"', text).group("codename")
        release_info = " ".join(id, codename, release)
    return release_info


def centerWindow(window):
    rect = QDesktopWidget().screenGeometry()
    width = 0
    height = 0

    if rect.width <= 640:
        width = 620
    elif rect.width <= 800:
        width = 720
    else:
        width = 960

    if rect.height <= 480:
        height = 450
    elif rect.height <= 600:
        height = 520
    else:
        height = 680

    window.resize(width, height)
    window.move(rect.width() / 2 - window.width() / 2, rect.height() / 2 - window.height() / 2)
