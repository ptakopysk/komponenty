#!/usr/bin/env python3
#coding: utf-8

import sys

import logging
logging.basicConfig(
    format='%(asctime)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO)

import argparse
ap = argparse.ArgumentParser()
ap.add_argument('-f', '--filename',
        help='corpus file', default='billion.txt')
ap.add_argument('-c', '--component',
        help='component file', default='3-.konec.txt')
ap.add_argument('-n', '--number', type=int,
        help='number of lines to read from the corpus', default=100)
args = ap.parse_args()
 
logging.info(f'Will compute PMI for words in {args.component} on first {args.number} lines from {args.filename} corpus')




