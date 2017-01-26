# -*- coding: utf-8 -*-
"""99"""

import sys
import cPickle
import seaborn
from itertools import izip
from matplotlib import pyplot as plt
from sklearn.manifold import TSNE

def main():
    names,vecs = cPickle.load(open('country_vec.pkl', 'r'))
    # ## ValueError:array must not contain infs or NaNs -> はあ．
    # print np.isfinite(vecs).all() -> True
    # print np.isnan(vecs).all() -> False
    # print np.isinf(vecs).all() -> False
    result = TSNE(n_components=2).fit_transform(vecs)
    plt.figure(figsize=(15, 10))
    plt.plot(result[:,0], result[:,1], ' ')
    for i in izip(names, result):
        plt.text(i[1][0],i[1][1], i[0], size=6)
    plt.title('Visualize vector space using t-SNE')
    plt.xlabel('dim1')
    plt.ylabel('dim2')
    # plt.show()
    plt.savefig('99.pdf')

if __name__ == '__main__':
    main()

"""
@local

2Dplot byT-SNE: http://www.cl.ecei.tohoku.ac.jp/~reina.a/nlp100/99.pdf
"""





# 100本打ったぞ，やったぞ…！
