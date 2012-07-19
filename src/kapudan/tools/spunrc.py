#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

class spunrc():

    def _min2sec(minutes):
        return minutes * 60

    def creat():
        os.system("/bin/cp /etc/spun.conf ~/.spunrc")

    def setaudio(state):
        if state == True:
            os.system("/bin/sed -i 's/^#playwith=/playwith=/' ~/.spunrc")
        else if state == False:
            os.system("/bin/sed -i 's/^#audio=/audio=/' ~/.spunrc")

    def setwaittime(time):
        os.system("/bin/sed -i 's/^waittime=.*/waittime=" + _min2sec(time) + "' ~/.spunrc")
