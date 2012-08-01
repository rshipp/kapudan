#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil

class SpunRC():

    def __init__(self):
        self.mintime = 5
        self.maxtime = 10080
        self.spun = "/usr/bin/spun"
        self.spunrc = os.getenv("HOME") + "/.spunrc"
        self.spunconf = "/etc/spun.conf"
        self.spunstart = "/usr/share/autostart/spun.desktop"
        self._create()

    def _create(self):
        if os.path.isfile(self.spunrc):
            return True
        else:
            try:
                shutil.copyfile(self.spunconf, self.spunrc)
                return True
            except IOError as e:
                print e
                return False

    def isInstalled(self):
        return os.path.isfile(self.spun)

    def isEnabled(self):
        state = os.path.getsize(self.spunstart)
        if state > 2:
            return True
        else:
            return False

    def getAudio(self):
        state = os.system("/bin/bash -c '. " + self.spunrc + " && [[ -n $audio && -n $playwith ]]'")
        if state == 0:
            return True
        else:
            return False

    def getWaitTime(self):
        time = os.system("/bin/bash -c '. " + self.spunrc + " && exit $waittime'") / 256
        if time < self.mintime:
            time = self.mintime
        elif time > self.maxtime:
            time = self.maxtime
        return int(time)

    def setAudio(self, state):
        if state == True:
            os.system("/bin/sed -i 's/^#playwith=/playwith=/' " + self.spunrc)
            os.system("/bin/sed -i 's/^#audio=/audio=/' " + self.spunrc)
        elif state == False:
            os.system("/bin/sed -i 's/^playwith=/#playwith=/' " + self.spunrc)
            os.system("/bin/sed -i 's/^audio=/#audio=/' " + self.spunrc)

    def setWaitTime(self, time):
        if time < self.mintime:
            time = self.mintime
        elif time > self.maxtime:
            time = self.maxtime
        os.system("/bin/sed -i 's/^waittime=.*$/waittime=" + str(time) + "/' " + self.spunrc)
