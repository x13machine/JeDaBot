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
import configparser
from .print import print
import os.path

class Config:
    def __init__(self, config):
        self.cfg = configparser.ConfigParser()
        self.loaded = False
        self.name = config
        print("Loading configuration file {}.cfg...".format(config), "CONFIG", "lightblue")
        if os.path.isfile('misc/{}.cfg'.format(config)):
            self.cfg.read('misc/{}.cfg'.format(config))
        else:
            print("{}.cfg configuration file doesn't exists!".format(config), "CONFIG", "lightred")
            return
        self.loaded = True
        self.sections = self.cfg.sections()
        print("Configuration file {}.cfg successfully loaded.".format(config), "CONFIG", "lightgreen")
   
    def setstring(self, section, name, string):
        self.cfg[section][name] = string # wow, very simple

    def getstring(self, section, name):
        if name in self.cfg[section]:
            return self.cfg[section][name]
        else:
            return ""
            
    def savecfg(self):
        self.cfg.write(open('misc/{}.cfg'.format(self.name), "w")) # wowverysimple
        
    def reloadcfg(self):
        del self.cfg
        self.cfg = configparser.ConfigParser()
        self.cfg.read('misc/{}.cfg'.format(self.name)) # wownotsoverysimple
