#!/usr/bin/python
# -*- coding: utf-8 -*-

import os


class RCDaemon():

    def isEnabled(self, daemon):
        with open("/etc/rc.conf", "r") as f:
            for line in f:
                if line.startswith("DAEMONS=("):
                #FIXME: work when DAEMONS is split over multiple lines
                    return daemon in line

    def isInstalled(self, daemon):
        return os.path.isfile("/etc/rc.d/" + daemon)
