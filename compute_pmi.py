#!/usr/bin/env python3
#coding: utf-8

import sys
from collections import defaultdict, Counter
import math

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
ap.add_argument('-t', '--topn', type=int,
        help='number of top neighbours to list', default=10)
args = ap.parse_args()
 
def pmi(count_a, count_b, count_ab, count_total):
    return math.log(total_words * count_ab / count_a / count_b)


logging.info(f'Will compute PMI for words in {args.component} on first {args.number} lines from {args.filename} corpus')

logging.info(f'Reading in the component....')
component_words = set()
with open(args.component) as infile:
    words = infile.read()
    component_words = set(words.split())
# print(component_words)
logging.info(f'The component contains {len(component_words)} words.')


logging.info(f'Reading in the corpus and calculating word and word pair counts....')
total_words = 0
word_counts = Counter()
pair_counts = defaultdict(Counter)
lines_read = 0
with open(args.filename) as infile:
    for line in infile:
        lines_read += 1
        if lines_read > args.number:
            break
        words = line.split()
        word_counts.update(words)
        total_words += len(words)
        # if the line containes some of the component words...
        intersection = component_words.intersection(set(words))
        for word in intersection:
            # TODO only update with words in -10,+10 window?
            # TODO now also counting pair (word,word), probably wrong?
            pair_counts[word].update(words)
logging.info(f'We have read in {total_words} tokens, {len(word_counts)} unique words.')
logging.info(f'We have pairs for {len(pair_counts)} of the {len(component_words)} words of the component.')


logging.info(f'Calculating PMIs....')
pmis = defaultdict(lambda: defaultdict(float))
for word, neighbours in pair_counts.items():
    for neighbour, pair_count in neighbours.items():
        pmis[neighbour][word] = pmi(word_counts[word], word_counts[neighbour], pair_count, total_words)
logging.info(f'We have calculated PMI for {len(pmis)} candidate neighbouring words.')

#for neighbour, values in pmis.items():
    #print(neighbour, values)

logging.info(f'Averaging PMIs....')
avg_pmis = defaultdict(float)
for neighbour in pmis:
    for word in pair_counts:
        avg_pmis[neighbour] += pmis[neighbour][word]

logging.info(f'Sorting candidates by average PMIs....')
sorted_pmis = sorted(avg_pmis, key=avg_pmis.get, reverse=True)

logging.info(f'The best scoring candidate label is: "{sorted_pmis[0]}"')

logging.info(f'Printing out top {args.topn} candidates...')
for neighbour in sorted_pmis[:args.topn]:
    print(neighbour, avg_pmis[neighbour])


logging.info(f'Done')
