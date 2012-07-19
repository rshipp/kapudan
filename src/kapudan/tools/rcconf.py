#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

class RCDaemons():

    def status(daemon):
        os.system("grep ^DAEMONS=\( /etc/rc.conf | 
                   grep \"[( ]" + daemon + "[ )]\"")

    def add(daemon):
        if status(daemon) == True:
            return True
        else:
            # Add the Daemon

    def delete(daemon):
        if status(daemon) == True:
            # Delete the daemon
        else:
            return True
