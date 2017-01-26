# -*- coding: utf-8 -*-
"""87"""

import sys
import cPickle
from sklearn.metrics.pairwise import cosine_similarity
#from scipy.spatial.distance import cosine

#/home/reina.a/.pyenv/versions/2.7.12/lib/python2.7/site-packages/sklearn/utils/validation.py:395: DeprecationWarning: Passing 1d arrays as data is deprecated in 0.17 and will raise ValueError in 0.19. Reshape your data either usingX.reshape(-1, 1) if your data has a single feature or X.reshape(1, -1) if it contains a single sample.  DeprecationWarning)
#dataを1次元配列として渡すのver0.17から廃止?でver0.19だとエラー? ->...うるさいからさよなら
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


word1 = 'French'
word2 = 'Spanish'

def main():
    words, X_pca = cPickle.load(sys.stdin)
    i1 = list(words).index(word1)
    i2 = list(words).index(word2)
    print cosine_similarity(X_pca[i1,:], X_pca[i2,:])[0,0]
    #print cosine(X_pca[i1,:], X_pca[i2,:])

if __name__ == '__main__':
    main()
