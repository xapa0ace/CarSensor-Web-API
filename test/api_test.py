#!usr/bin/python
# -*- coding: utf-8 -*-
"""
CarSensor Web API
API-Test
"""
import sys
import os
import csapi
from csapi import parse

def main():
    API_KEY = '' #'< - You CarSensor Web API Key - >'
    if API_KEY == '':
        API_KEY = raw_input()

    do_api = csapi.main(API_KEY)
    print do_api
    KEYWORD = raw_input()
    do_api.keyword(KEYWORD)
    print (do_api.catalog_api())

if __name__ == '__main__':
    if len(sys.argv)==1:
        main()
    else:
        p = parse
        p.main(sys.argv[1:])
