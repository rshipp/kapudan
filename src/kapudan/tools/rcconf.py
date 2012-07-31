#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

class RCDaemon():

    def isEnabled(self, daemon):
        state = os.system("grep ^DAEMONS=\( /etc/rc.conf | grep -q \"[( @]" + daemon + "[ )]\"")
        if state == 0:
            return True
        else:
            return False

    def isInstalled(self, daemon):
        return os.path.isfile("/etc/rc.d/" + daemon)

