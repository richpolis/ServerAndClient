#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys


class MysqlManager(object):
    conn = None
    cursor = None
    sql = ""

    def conect(self):
        if self.conn is None:
            try:
                self.conn = mdb.connect('localhost', 'richpolis', 'D3m3s1s1', 'prueba')
            except mdb.Error, e:
                print "Error %d: %s" % (e.args[0], e.args[1])
                sys.exit(1)
        return self.conn

    def get_cursor(self):
        if self.conn is None:
            self.connect()
        if self.cursor:
            self.cursor = self.conn.cursor()
        return self.cursor

    def close(self):
        if self.conn:
            self.conn.close()
