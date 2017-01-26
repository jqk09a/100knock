# -*- coding: utf-8 -*-
"""89"""

import sys
import cPickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def main():
    words, X_pca = cPickle.load(sys.stdin)
    i_Spain = list(words).index('Spain')
    i_Madrid = list(words).index('Madrid')
    i_Athens = list(words).index('Athens')
    vec = X_pca[i_Spain,:] - X_pca[i_Madrid,:] + X_pca[i_Athens]
    sims = cosine_similarity(vec, X_pca)[0]
    for j,k in enumerate(np.argsort(sims)[:-11:-1], start=1):
        print '{}\t{}\t{}'.format(j, words[k], sims[k])

if __name__ == '__main__':
    main()
    
