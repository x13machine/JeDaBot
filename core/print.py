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
from .version import __bot__
import sys

def print(text, mode="CORE", color="lightcyan"):
    colors = {"black": "0;30", "darkgray": "1;30", "blue": "0;34","lightblue": "1;34", "green": "0;32", "lightgreen": "1;32", "cyan": "0;36", "lightcyan": "1;36", "red": "0;31", "lightred": "1;31", "purple": "0;35", "lightpurple": "1;35", "brown": "0;33", "yellow": "1;33", "lightgray": "0;37", "white": "1;37"}
    try:
        colort = colors[color]
    except KeyError:
        colort = "1;36"
    sys.stdout.write("\033[1;33m[{}]\033[0m \033[{}m{}\033[0m\n".format(mode, colort, text))
    log = open("misc/{}.log".format(__bot__.lower()), "a")
    log.write("[{}] {}\n".format(mode, text))
    log.close()
