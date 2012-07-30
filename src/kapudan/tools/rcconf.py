#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

class RCDaemon():

    def isEnabled(daemon):
        state = os.system("grep ^DAEMONS=\( /etc/rc.conf | grep \"[( ]" + daemon + "[ )]\"")
        if state = 0:
            return True
        else:
            return False

    def isInstalled(daemon):
        return os.path.isfile("/etc/rc.d/" + daemon)

