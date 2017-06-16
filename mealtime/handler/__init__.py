# -*- coding: utf-8 -*-

""" Handler - init.
"""

from __future__ import absolute_import, print_function, unicode_literals

from .base import BaseApiHandler
from .fbhook import FBWebHookHandler

__all__ = ['route']

class DefaultHandler(BaseApiHandler):
	def get(self):
		self.write_success({'message': 'hi!'})



route = [
        (r'/', DefaultHandler),
        (r'/fbhook', FBWebHookHandler)
    ]
