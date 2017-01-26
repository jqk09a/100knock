# -*- coding: utf-8 -*-
"""85"""

import sys
import cPickle
from sklearn.decomposition import PCA

def main():
    words, X = cPickle.load(sys.stdin)
    pca = PCA(n_components=300)
    X_pca = pca.fit_transform(X)
    cPickle.dump((words,X_pca), sys.stdout)
    print X_pca.shape

if __name__ == '__main__':
    main()
