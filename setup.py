#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import glob
import shutil
import sys
import fnmatch

from distutils.core import setup
from distutils.cmd import Command
from distutils.command.build import build
from distutils.command.install import install

def update_messages():
    # Create empty directory
    shutil.rmtree(".tmp", True)
    os.makedirs(".tmp")

    # Collect UI files
    for filename in glob.glob1("ui", "*.ui"):
        os.system("pyuic5 -o .tmp/%s.py ui/%s" % (filename.split(".")[0], filename))

    # Collect Python files
    directories = ["src/kapudan",
                   "src/kapudan/screens",
                   "src/kapudan/tools"]

    for d in directories:
        for filename in glob.glob1(d, "*.py"):
            shutil.copy("%s/%s" % (d, filename), ".tmp")

    # Collect desktop files
    os.system("cp -R data/*.desktop.in .tmp/")

    # Generate headers for desktop files
    for filename in glob.glob(".tmp/*.desktop.in"):
        os.system("intltool-extract --type=gettext/ini %s" % filename)

    # Generate POT file
    os.system("find .tmp -name '*.py' -o -name '*.h' | "
              "xargs xgettext --default-domain=%s \
                        -k_ -kN_ -ki18n \
                        -ktranslate:1c,2 \
                        -k_translate:1c,2 \
                        -o po/%s.pot" % ("kapudan", "kapudan"))

    ## Update PO files
    for item in os.listdir("po"):
        if item.endswith(".po"):
            os.system("msgmerge --no-wrap --sort-by-file -q -o .tmp/temp.po po/%s po/%s.pot" % (item, "kapudan"))
            os.system("cp .tmp/temp.po po/%s" % item)

    # Remove temporary directory
    shutil.rmtree(".tmp")


def makeDirs(dir):
    try:
        os.makedirs(dir)
    except OSError:
        pass


class Build(build):
    def run(self):
        # Clear all
        os.system("rm -rf build")
        # Copy codes
        print("Copying PYs...")
        os.system("cp -R src build/")

        # Copy compiled UIs and RCs
        print("Generating UIs...")
        for filename in glob.glob1("ui", "*.ui"):
            #            if not "ui_scrFolder" in filename:
            #                os.system("pykdeuic4 -o build/kapudan/screens/%s.py ui/%s" % (filename.split(".")[0], filename))
            #            else:
            #                shutil.copy("ui/ui_scrFolder.py", "build/kapudan/screens/ui_scrFolder.py")
            os.system("pyuic5 -o build/kapudan/screens/%s.py ui/%s" % (filename.split(".")[0], filename))
            # ToDo: implement pylupdate5 function to extract translation to .ui files
            #os.system("pylupdate5 --noobsolete ui/%s build/kapudan/screens/%s.py ui/%s" % (filename.split(".")[0], filename))
        print("Generating RCs...")
        for filename in glob.glob1("data", "*.qrc"):
            os.system("python3 -m PyQt5.pyrcc_main data/%s -o build/kapudan/%s_rc.py" % (filename, filename.split(".")[0]))

        os.system("sed -i 's/kapudan_rc/kapudan.\kapudan_rc/g' build/kapudan/screens/ui_*")


class Install(install):
    def run(self):
        os.system("./setup.py build")
        if self.root:
            kde_dir = "%s/usr" % self.root
        else:
            kde_dir = "/usr"
        bin_dir = os.path.join(kde_dir, "bin")
        locale_dir = os.path.join(kde_dir, "share/locale")
        project_dir = os.path.join(kde_dir, "share/apps", "kapudan")

        # Make directories
        print("Making directories...")
        makeDirs(bin_dir)

        # makeDirs(locale_dir)
        makeDirs(project_dir)

        # Install desktop files
        print("Installing desktop files...")

        for filename in glob.glob("data/*.desktop.in"):
            os.system("intltool-merge -d po %s %s" % (filename, filename[:-3]))

        # Install codes
        print("Installing codes...")
        os.system("cp -R build/* %s/" % project_dir)

        # Install locales
        print("Installing locales...")
        for filename in glob.glob1("po", "*.po"):
            lang = filename.rsplit(".", 1)[0]
            os.system("msgfmt po/%s.po -o po/%s.mo" % (lang, lang))
            try:
                os.makedirs(os.path.join(locale_dir, "%s/LC_MESSAGES" % lang))
            except OSError:
                pass
            shutil.copy("po/%s.mo" % lang, os.path.join(locale_dir, "%s/LC_MESSAGES" % lang, "%s.mo" % "kapudan"))
        # Rename
        print("Renaming application.py...")
        #shutil.move(os.path.join(project_dir, "application.py"), os.path.join(project_dir, "%s.py" % "kapudan"))
        # Modes
        print("Changing file modes...")
        os.chmod(os.path.join(project_dir, "%s.py" % "kapudan"), 0o0755)
        # Symlink
        try:
            if self.root:
                os.symlink(os.path.join(project_dir.replace(self.root, ""), "%s.py" % "kapudan"),
                           os.path.join(bin_dir, "kapudan"))
            else:
                os.symlink(os.path.join(project_dir, "%s.py" % "kapudan"), os.path.join(bin_dir, "kapudan"))
        except OSError:
            pass


if "update_messages" in sys.argv:
    update_messages()
    sys.exit(0)

setup(
    name="Kapudan",
    version="2016.09.01",
    description="Chakra's desktop greeter, a fork of Pardus's Kaptan.",
    license="GPL",
    author="(c) 2016 The Chakra Developers",
    author_email="chakra-devel@googlegroups.com",
    url="https://chakralinux.org/code/kapudan.git/",
    packages=[''],
    package_dir={'': ''},
    data_files=[],
    cmdclass={
        'build': Build,
        'install': Install,
    }
)
