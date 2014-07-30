#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil
import subprocess


class KSuperKey():

    def __init__(self):
        self.bin = '/usr/bin/ksuperkey'
        self.stopbin = ['/usr/bin/killall', 'ksuperkey']
        self.autostartfile = os.path.expanduser('~/.config/autostart/ksuperkey.desktop')
        self.desktopfile = '/usr/share/kde4/apps/kapudan/kapudan/ksuperkey.desktop'

    def isEnabled(self):
        return os.path.isfile(self.autostartfile)

    def enable(self):
        if not self.isEnabled():
            self._enableStartup()
            self._start()

    def disable(self):
        if self.isEnabled():
            self._disableStartup()
            self._stop()

    def _enableStartup(self):
        shutil.copy(self.desktopfile, self.autostartfile)

    def _disableStartup(self):
        os.remove(self.autostartfile)

    def _start(self):
        subprocess.call(self.bin)

    def _stop(self):
        subprocess.call(self.stopbin)
