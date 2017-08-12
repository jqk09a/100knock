# -*- coding: utf-8 -*-
"""98"""

import sys
import cPickle
import seaborn
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

def main():
    names,vecs = cPickle.load(open('country_vec.pkl', 'r'))
    Z_ward = linkage(vecs, method='ward')
    plt.figure(figsize=(12, 10))
    dendrogram(Z_ward,
        orientation="right",
        leaf_font_size=2,
        labels=[name for name in names])
    plt.title("Ward' clusterig")
    plt.xlabel('distance')
    plt.ylabel('word')
    # plt.show()
    plt.savefig('98.pdf')

if __name__ == '__main__':
    main()


"""
dendrogram: http://www.cl.ecei.tohoku.ac.jp/~reina.a/nlp100/98.pdf
"""
