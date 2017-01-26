# -*- coding: utf-8 -*-
"""88"""

import sys
import cPickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


word = 'England'
#word = 'French'

def main():
    words, X_pca = cPickle.load(sys.stdin)
    i = list(words).index(word)
    sims = cosine_similarity(X_pca[i,:], X_pca)[0]
    for j,k in enumerate(np.argsort(sims)[:-11:-1], start=1):
        print '{}\t{}\t{}'.format(j, words[k], sims[k])

if __name__ == '__main__':
    main()
