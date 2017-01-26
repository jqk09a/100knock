# -*- coding: utf-8 -*-
"""94"""

import sys
import cPickle
import numpy as np
from gensim.models import word2vec
from sklearn.metrics.pairwise import cosine_similarity

#/home/reina.a/.pyenv/versions/2.7.12/lib/python2.7/site-packages/sklearn/utils/validation.py:395: DeprecationWarning: Passing 1d arrays as data is deprecated in 0.17 and will raise ValueError in 0.19. Reshape your data either usingX.reshape(-1, 1) if your data has a single feature or X.reshape(1, -1) if it contains a single sample.  DeprecationWarning)
#dataを1次元配列として渡すのver0.17から廃止?でver0.19だとエラー? ->...うるさいからさよなら
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def ex85(data):
    words, X_pca = cPickle.load(sys.stdin)
    with open('combined.csv.85-94', 'w') as fo85:
        for line in data:
            tokens = line.strip().split(',')
            try:
                i1 = list(words).index(tokens[0])
                i2 = list(words).index(tokens[1])
            except:
                continue
            fo85.write('{},{}\n'.format(line.strip(), cosine_similarity(X_pca[i1,:],X_pca[i2,:])[0,0]))
            #print '{},{}'.format(line.strip(), cosine_similarity(X_pca[i1],X_pca[i2])[0][0])

def ex90(data):
    model = word2vec.Word2Vec.load('w2v.model')
    with open('combined.csv.90-94', 'w') as fo90:
        for line in data:
            tokens = line.strip().split(',')
            try:
                print tokens[0],
                print tokens[1],
                result = model.similarity(tokens[0],tokens[1])
                print result
            except:
                continue
            fo90.write('{},{}\n'.format(line.strip(), result))
            #print '{},{}'.format(line.strip(), result)

if __name__ == '__main__':
    data = open('combined.csv', 'r')
    ex85(data)
    data.seek(0)
    ex90(data)

"""
$ python 94.py < enwiki-20150112-400-r100-10576.txt.clean.pretreatment.pair.tsv.pkl.pca
$ less combined.csv.85-94
love,sex,6.77,0.213673056935
tiger,cat,7.35,0.2234475764
tiger,tiger,10.00,1.0
book,paper,7.46,0.44376506092
...
$ less combined.csv.90-94
love,sex,6.77,0.372529843649
tiger,cat,7.35,0.657317760026
tiger,tiger,10.00,1.0
book,paper,7.46,0.414281766351
...
"""
