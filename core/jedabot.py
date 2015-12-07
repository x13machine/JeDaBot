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
import os
import signal
import sys
import time
import urllib.request, urllib.parse
from .logger import print
from .version import __bot__, __botw__, __version__, __cversion__, __api__
from .framework import Framework as f
from .config import Config as c
from .database import Database as d

class JeDaBot:
    def __init__(self):
        self.starttime = time.time()
        fi = open("misc/{}.log".format(__bot__.lower()), "a")
        fi.write("----------{} log----------\n".format(time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())))
        fi.close()
        print("{} {} - Started at {}".format(__bot__, __version__, time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())))
        print("The smart people are the ones who fails. Without fails, people are morons.\n")
        self.updater()
        self.config = c(__bot__.lower())
        if not self.config.loaded:
            print("Creating default configuration.")
            cfg = open("misc/{}.cfg".format(__bot__.lower()), "w")
            cfg.write(""";JeDaBot
;Copyright 2015 Jesús "JeDa" Hernández & Worldev

;This program is free software; you can redistribute it and/or modify
;it under the terms of the GNU General Public License as published by
;the Free Software Foundation; either version 2 of the License, or
;(at your option) any later version.

;This program is distributed in the hope that it will be useful,
;but WITHOUT ANY WARRANTY; without even the implied warranty of
;MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
;GNU General Public License for more details.

;You should have received a copy of the GNU General Public License along
;with this program; if not, write to the Free Software Foundation, Inc.,
;51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

[{}]
Name = JeDaBot
Owner = JeDa
Frameworks = irc,wa
IAmConfigured = False
""".format(__bot__))
            cfg.close()
            print("Please edit misc/{}.cfg then start {}.".format(__bot__.lower(), __bot__))
            self.handlestop()
        if not __bot__ in self.config.sections:
            print("Cannot find {} section in config. Please fix it or remove misc/{}.cfg for regenerating the config file.".format(__bot__, __bot__.lower()))
            self.handlestop()
        if self.config.getstring(__bot__, "IAmConfigured") == "False":
            print("Please configure {} correctly.".format(__bot__))
            self.handlestop()
        if self.config.getstring(__bot__, "Frameworks") == "":
            print("Please load any framework in the config before starting {}.".format(__bot__))
            self.handlestop()
        print("Loading frameworks...")
        self.frame = f(self, self.config.getstring(__bot__, "Frameworks").split(","))
        if self.frame.loaded == 0:
            print("Looks like no framework was loaded. Please install working frameworks then restart {}.".format(__bot__))
            self.handlestop()
        self.dontkeep = False
        print("Done! {} is now running since {}. Took {} {} to start.".format(__bot__, time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()), str(time.time() - self.starttime).split(".")[0], ("second" if str(time.time() - self.starttime).split(".")[0] == "1" else "seconds")))

    def serve_forever(self):
        while True:
            if self.dontkeep:
                break
            if (time.time() - self.lastchecku) >= 43200:
                self.updater()
            for fw in self.frame.frameworks:
                try:
                    self.frame.frameworks[fw].serve()
                except:
                    pass
            time.sleep(0.1) # prevent lots of CPU usage

    def pastebin(self, message, caller="a module"):
        return str(urllib.request.urlopen('http://pastebin.com/api/api_post.php', bytes(urllib.parse.urlencode({'api_dev_key': '57fe1369d02477a235057557cbeabaa1','api_option': 'paste', 'api_paste_code': "{}\n\n~~~Uploaded by JeDaBot Pastebin Function as request of {}~~~".format(message, caller)}), "utf-8")).read(), "utf-8")

    def updater(self):
        print("Checking updates...", "UPDATE", "lightblue")
        self.lastchecku = time.time()
        try:
            c = urllib.request.urlopen("{}cversion".format(__api__)).read()
        except Exception as err:
            print("Error trying to connect to {} ({}). Skipping updates.".format(__botw__.split("/")[2], err), "UPDATE", "lightred")
            return
        if int(c) > __cversion__:
            print("A update is available!", "UPDATE", "lightgreen")
            try:
                b = urllib.request.urlopen("{}bot".format(__api__)).read()
                v = urllib.request.urlopen("{}version".format(__api__)).read()
                print("{} {} is available for download.".format(b, v), "UPDATE", "lightgreen")
            except:
                print("Error trying to connect to {} for getting bot data ({}).".format(__botw__.split("/")[2], err), "UPDATE", "lightred")
                b = __bot__
            try:
                u = urllib.request.urlopen("{}/downloads/latest.zip".format(__botw__)) 
            except Exception as err:
                print("Error trying to open connection for download the update ({}). Skipping updates.".format(err), "UPDATE", "lightred")
                return
            headers = dict(re.findall(r"(?P<name>.*?): (?P<value>.*?)\n", str(u.info())))
            filesize = int(headers["Content-length"]) 
            filesizedl = 0 
            filename = "{}-update-{}.zip".format(b.lower(), time.time())
            f = open(filename, 'wb')
            print("Downloading update...", "UPDATE", "lightgreen")
            while True:
                buffer = u.read(8192)
                if not buffer: 
                    break 
                filesizedl += len(buffer) 
                f.write(buffer) 
                print("Progress: {}".format(()), "UPDATE")
            f.close()
            if filesize == filesizedl:
                print("Updating...", "UPDATE", "lightgreen")
            else:
                print("The download failed!", "UPDATE", "lightred")
                return
        else:
            print("No updates available!", "UPDATE", "lightred")
    
    def handlestop(self, exitid=1):
        self.dontkeep = True
        try:
            for fw in self.frame.frameworks:
                try:
                    self.frame.frameworks[fw].stop()
                except:
                    pass
        except: # probably not frameworks loaded
            pass
        print("Exiting at {} --- Uptime: {} {}".format(time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()), str(time.time() - self.starttime).split(".")[0], ("second" if str(time.time() - self.starttime).split(".")[0] == "1" else "seconds")))
        fi = open("misc/{}.log".format(__bot__.lower()), "a")
        fi.write("---------/{} log\---------\n\n".format(time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())))
        fi.close()
        os._exit(exitid)

    def signal_handler(self, signum, frame):
        signals = dict((getattr(signal, n), n) for n in dir(signal) if n.startswith('SIG') and '_' not in n )
        print('Received {}'.format(signals[signum]), "CORE", "lightred")
        self.handlestop(0)
