# -*- coding: utf-8 -*-
"""92"""

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
    with open('questions-words.txt.85-92', 'w') as fo85:
        for line in data:
            tokens = line.strip().split(' ')
            try:
                i1 = list(words).index(tokens[0])
                i2 = list(words).index(tokens[1])
                i3 = list(words).index(tokens[2])
            except:
                #print 'UNKNOW VOCAB'
                continue
            vec = X_pca[i3] - X_pca[i1] + X_pca[i2]
            sims = cosine_similarity(vec, X_pca)[0]
            i = np.argsort(sims)[-1]
            fo85.write('{}\t{}\t{}\t{}\t{}\t{}\n'.format(tokens[0], tokens[1], tokens[2], tokens[3], words[i], sims[i]))

def ex90(data):
    model = word2vec.Word2Vec.load('w2v.model')
    with open('questions-words.txt.90-92', 'w') as fo90:
        for line in data:
            tokens = line.strip().split(' ')
            try:
                result = model.most_similar(positive=[tokens[1],tokens[2]], negative=[tokens[0]], topn=1)[0]
            except:
                #print 'UNKNOW VOCAB'
                continue
            fo90.write('{}\t{}\t{}\t{}\t{}\t{}\n'.format(tokens[0], tokens[1], tokens[2], tokens[3], result[0], result[1]))


if __name__ == '__main__':
    data = open('91_questions-words.txt')
    ex85(data)
    data.seek(0)
    ex90(data)

"""
python 92.py < enwiki-20150112-400-r100-10576.txt.clean.pretreatment.pair.tsv.pkl.pca
"""
