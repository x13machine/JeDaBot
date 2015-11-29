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
import imp
import os, os.path
from .print import print

class Framework:
    def __init__(self, core, frameworks):
        self.core = core
        self.loaded = 0
        self.frameworks = {}
        for fw in frameworks:
            if os.path.isfile("framework/" + fw + "/" + fw + ".py"):
                self.loadfw(fw)
            else:
                print("Tried to load framework {}, but it wasn't found.".format(fw), "FRAMEWORK", "lightred")

    def loadfw(self, fw):
        print("Loading {} framework...".format(fw), "FRAMEWORK", "lightblue")
        try:
            self.frameworks[fw]
            print("{} framework is already loaded!".format(fw), "FRAMEWORK", "lightred")
            return
        except KeyError:
            pass
        try:
            framework = imp.reload(sys.modules['framework.' + fw + '.' + fw])
        except:
            try:
                framework = importer('framework.' + fw + '.' + fw)
            except ImportError as q:
                print("{} framework cannot be loaded: {}".format(fw, q), "FRAMEWORK", "lightred")
                return
        try:
            self.frameworks[fw] = getattr(framework, fw)(self.core, self)
        except Exception as q:
            if str(q) == "'module' object has no attribute '" + fw + \
                    "'":
                print("{} framework cannot be loaded due the main class is not found.".format(fw, q), "FRAMEWORK", "lightred")
                return
            else:
                print("{} framework cannot be loaded due to a __init__ error: {}".format(fw, q), "FRAMEWORK", "lightred")
            return
        self.loaded += 1
        print("Framework {} successfully loaded.".format(fw), "CONFIG", "lightgreen")

def importer(cl):
        d = cl.rfind(".")
        classname = cl[d + 1:len(cl)]
        m = __import__(cl[0:d], globals(), locals(), [classname])
        return getattr(m, classname)
