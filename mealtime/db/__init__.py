# -*- coding: utf-8 -*-

""" DB - init
"""

from __future__ import absolute_import, print_function, unicode_literals


from pymongo import MongoClient

import os
import logging


__all__ = ['db_gen',]


DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = int(os.environ.get('DB_PORT', 27017))
DB_USER = os.environ.get('DB_USER', '')
DB_PWD = os.environ.get('DB_PWD', '')
DB_NAME = os.environ.get('DB_NAME', 'mealtime')

logging.info("DB: %s@%s:%d/%s" % (DB_USER, DB_HOST, DB_PORT, DB_NAME))

def db_gen():
    db = MongoClient(host=DB_HOST, port=DB_PORT)[DB_NAME]
    if DB_USER != '':
        db.authenticate(DB_USER, DB_PWD)
    return db
