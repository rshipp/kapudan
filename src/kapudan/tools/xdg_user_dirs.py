#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import subprocess


class UserDirs():

    def __init__(self):
        home = os.path.expanduser('~')
        xdg_dirs = ['DESKTOP', 'DOWNLOAD', 'TEMPLATES', 'PUBLICSHARE',
                    'DOCUMENTS', 'MUSIC', 'PICTURES', 'VIDEOS']

        if not os.path.exists(home + '/.config/user-dirs.locale'):
            # Only continue if xdg-user-dirs-update has never been run.
            # Record the user's initial configuration.
            original_dirs = []
            for file in os.listdir(home):
                if os.path.isdir(file) and not file.startswith('.'):
                    original_dirs += file
            # Call xdg-user-dirs-update, which creates all the folders. :(
            subprocess.call('xdg-user-dirs-update')
            # Reset the user's home directory to the initial state,
            # keeping only the config files written by
            # xdg-user-dirs-update.
            for file in os.listdir(home):
                if os.path.isdir(file) and not file.startswith('.'):
                    if file not in original_dirs:
                        # Delete non-empty dirs.
                        try:
                            os.rmdir(file)
                        except OSError:
                            pass

    def get(self, directory):
        """directory must be one of the XDG directory names, all
           caps.
        """
        return subprocess.check_output(['xdg-user-dir',
                directory]).replace('\n', '')
