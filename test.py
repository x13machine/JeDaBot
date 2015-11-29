#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
   JeDaBot
   Copyright 2015 Jesús "JeDa" Hernández & Worldev
   
   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2 of the License, or
   (at your option) any later version.
   
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   
   You should have received a copy of the GNU General Public License along
   with this program; if not, write to the Free Software Foundation, Inc.,
   51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

notworking = False

import os, os.path, subprocess

print("JeDaBot Testing Script")
print("~Sit back and wait meanly this is done~\n")

print("Step 1/2: Test core")
try:
    import core.jedabot
except:
    notworking = True
    print("Detected core.jedabot as not working!")
try:
    import core.framework
except:
    notworking = True
    print("Detected core.framework as not working!")
try:
    import core.config
except:
    notworking = True
    print("Detected core.config as not working!")
try:
    import core.print
except:
    notworking = True
    print("Detected core.print as not working!")
try:
    import core.version
except:
    notworking = True
    print("Detected core.version as not working!")
try:
    import core.database
except:
    notworking = True
    print("Detected core.database as not working!")
try:
    import jedabot
except:
    notworking = True
    print("Detected jedabot.py as not working!")
print("Step 1/2 completed.\n")

print("Step 2/2: Test frameworks")
def core():
    print("meh")
def importer(cl):
        d = cl.rfind(".")
        classname = cl[d + 1:len(cl)]
        m = __import__(cl[0:d], globals(), locals(), [classname])
        return getattr(m, classname)
for fw in os.listdir("framework"):
    try:
        framework = imp.reload(sys.modules['framework.' + fw + '.' + fw])
    except:
        try:
            framework = importer('framework.' + fw + '.' + fw)
        except ImportError as q:
            print("Detected {} framework as not working!".format(fw))
    try:
        getattr(framework, fw)(core, core)
    except Exception as q:
        print("Detected {} framework as not working!".format(fw))
    print("Tested: {} framework".format(fw))
print("Step 2/2 completed.")

print("All done!")
if notworking:
    os._exit(1)
os._exit(0)
