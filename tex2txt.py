#!/usr/bin/env python3
#coding: utf-8

import sys

import logging
logging.basicConfig(
    format='%(asctime)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO)

directory = sys.argv[1]

komponenta = 0  # 1..512
smer = '+'  # or -
typ = 'konec'  # or nej


for line in sys.stdin:
    if not line.isspace():
        if line.startswith(r'\komp'):
            komponenta += 1
        elif line.startswith(r'\smer'):
            smer = '+' if '+' in line else '-'
        elif line.startswith(r'\typ'):
            typ = 'konec' if 'Konec' in line else 'nej'
        else:
            with open(f'{directory}/{komponenta}{smer}{typ}.txt', 'w') as outfile:
                print(line, file=outfile)

