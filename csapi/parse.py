#!usr/bin/python
# -*- coding: utf-8 -*-
"""
CarSensor Web API For Python
"""
__version__ = '0.2.3'

from argparse import ArgumentParser
import os
import sys
import json
import csapi
import csapi

def main(args):
    ap = ArgumentParser()
    # ap.add_argument('CarSensor Web API KEY ', nargs='?', help='-ak [CarSensor Web API_KEY] .')
    ap.add_argument('-v', '--version', action='store_true', help='CarSensor Web API For Python Version.')
    ap.add_argument('-c', '--catalog', action='store_true', help='[-c or --catalog] CATALOG API.')
    ap.add_argument('-u', '--usedcar', action='store_true', help='[-u or --usedcar] USEDCAR API.')

    ns = ap.parse_args(args)
    API_KEY = ''

    if ns.version:
        print __version__

    if ns.catalog:
        if API_KEY == '':
            API_KEY = raw_input()
        else:
            pass

        do_api = csapi.main(API_KEY)
        KEYWORD = raw_input()
        do_api.keyword(KEYWORD)
        print do_api.catalog_api()
    if ns.usedcar:
        if API_KEY == '':
            API_KEY = raw_input()
        else:
            pass

        do_api = csapi.main(API_KEY)
        KEYWORD = raw_input()
        do_api.keyword(KEYWORD)
        print do_api.usedcar_api()


if __name__ == '__main__':
    if len(sys.argv)==0:
        sys.argv=sys.argv+['-h']
    else:
        main(sys.argv[1:])
