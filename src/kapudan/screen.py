# -*- coding: utf-8 -*-

class Screen:
    """Abstract class for screen widgets"""

    title = ""
    desc = ""
    help = ""
    icon = None

    def shown(self):
        pass

    def execute(self):
        return True

    def backCheck(self):
        return False
