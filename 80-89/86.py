# -*- coding: utf-8 -*-
"""86"""

import sys
import cPickle

word = 'United_States'

def main():
    words, X_pca = cPickle.load(sys.stdin)
    i = list(words).index(word)
    print X_pca[i,:]

if __name__ == '__main__':
    main()
