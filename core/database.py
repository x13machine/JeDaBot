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
import sqlite3

class Database:
    def __init__(self, database):
        self.sql = sqlite3.connect('misc/{}.db'.format(database))
        self.sql3 = self.sql.cursor()

    def query(self, query, *kwargs):
        self.sql3.execute(query, kwargs)
        self.sql.commit()

    def close(self):
        self.sql.close()
        del self.sql
        del self.sql3
