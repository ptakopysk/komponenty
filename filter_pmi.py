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
        "with", "(", ")", "at", "through", "by", "of",
        "into", "on", "who", "from", "an", ":", '"', "'",
        ";", "-"}

words = list()

filename=sys.argv[1]
componentfilename=sys.argv[2]

with open(filename) as infile:
    for line in infile:
        word, pmi = line.split()
        if word in stopwords:
            break
        else:
            words.append(word)

with open(componentfilename) as infile:
    sample = ' '.join(infile.read().split()[:7])

component = filename.split('/')[-1].split('.')[0]

if words:
    words = ' '.join(words)
    print(f'\n{component}:\t{words}\t({sample})\n')
else:
    print(f'{component}:\t                  \t({sample})')




