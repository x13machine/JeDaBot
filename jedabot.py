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
from core.jedabot import JeDaBot
import signal

if __name__ == "__main__":
    bot = JeDaBot()
    signal.signal(signal.SIGTERM, bot.signal_handler)
    signal.signal(signal.SIGUSR1, bot.signal_handler)
    signal.signal(signal.SIGHUP, bot.signal_handler)
    signal.signal(signal.SIGINT, bot.signal_handler)
    bot.serve_forever()
