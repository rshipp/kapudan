#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re


class Repos():

    def __init__(self):
        self.config = "/etc/pacman.conf"
        self.re = "\n\[extra\]"

    def isEnabled(self):
        with open(self.config, "r") as config:
            return (re.search(self.re, config.read()) != None)

    def enableExtra(self):
        pass

    def disableExtra(self):
        pass
