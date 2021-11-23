#!/usr/bin/env python3
#coding: utf-8

import sys

import logging
logging.basicConfig(
    format='%(asctime)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO)

# after these words usually only rubbish comes
# so if there is anything interesting anywhere, it is BEFORE these words
# (i.e. stop searching once you reach these)
stopwords = {"and", ",", ".", "the", "for", "in", "of", "a", "to", "'s",
        "with", "(", ")", "at", "through", "by", "of"}

words = list()

filename=sys.argv[1]

with open(filename) as infile:
    for line in infile:
        word, pmi = line.split()
        if word in stopwords:
            break
        else:
            words.append(word)

# if words:
name = filename.split('/')[-1]
component = name.split('.')[0]
print(component, *words)


