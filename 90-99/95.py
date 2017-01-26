# -*- coding: utf-8 -*-
"""95"""

import sys
import numpy as np
from scipy.stats import spearmanr

def calc_spearman(data):
    human_scores = []
    similarities = []
    for line in data:
        tokens = line.strip().split(',')
        human_scores.append(float(tokens[2]))
        similarities.append(float(tokens[3]))
    return spearmanr(human_scores, similarities).correlation

if __name__ == '__main__':
    pca = open('combined.csv.85-94')
    w2v = open('combined.csv.90-94')
    print 'pca: {}'.format(calc_spearman(pca))
    print 'w2v: {}'.format(calc_spearman(w2v))

"""
$ python 95.py
pca: 0.361753352927
w2v: 0.620349023624
"""
