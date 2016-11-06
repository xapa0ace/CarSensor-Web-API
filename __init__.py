#!usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
import os
import glob
import sys
import json
import urllib2
import re

class main(object):
    global URL, FORMAT, API_KEY, KEYWORD
    """
    Car Sensor Web API
    """

    """
    ERROR CODEs
    1000：サーバ障害エラー (Server Error.)
    2000：APIキーまたはIPアドレスの認証エラー (API or IPAddress Authentication Error.)
    3000：パラメータ不正エラー (Parameters fraud.)
    """

    URL = 'https://webservice.recruit.co.jp/carsensor/'
    FORMAT = 'json'
    def __init__(self, API_KEY):
        self.URL = URL
        self.API_KEY = API_KEY
        self.FORMAT = FORMAT

    def keyword(self, KEYWORD):
        self.KEYWORD = KEYWORD
        return self

    def catalog_api(self):
        self.URL += 'catalog/v1/'
        self.URL += '?key=%s' % (self.API_KEY)
        self.URL += '&keyword=%s' % (self.KEYWORD)
    	self.URL += '&format=%s' % (self.FORMAT)
        response = urllib2.urlopen(self.URL)
        html = response.read()

        return html

    def usedcar_api(self):
        self.URL += 'usedcar/v1/'
        self.URL += '?key=%s' % (self.API_KEY)
        self.URL += '&keyword=%s' % (self.KEYWORD)
    	self.URL += '&format=%s' % (self.FORMAT)
        response = urllib2.urlopen(self.URL)
        html = response.read()

        return html
