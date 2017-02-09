# -*- coding: utf-8 -*-
"""84"""

import sys
import numpy as np
import pandas as pd
import cPickle

#N = 56804931(uniq)
def calc_ppmi():
    df = pd.read_csv(sys.stdin, delimiter='\t')
    N = df['f(t,c)'].sum()
    df = df[df['f(t,c)'] >= 10].sort_values(by='f(t,c)', ascending=False)
    df['PPMI'] = pd.DataFrame(np.maximum(np.log2((N*df['f(t,c)'])/(df['f(t,*)']*df['f(*,c)'])), 0))
    df = df[df['PPMI'] > 0]
    df = df.reset_index(drop = True)
    #df.to_csv(sys.stdout, sep='\t')
    return df

def make_X(df):
    df2 = df.pivot_table('PPMI', index=['t'], columns=['c'], fill_value=0)
    words = df2.index
    vec = df2.as_matrix()
    cPickle.dump((words,vec), sys.stdout)
    return vec

if __name__ == '__main__':
    df = calc_ppmi()

    X = make_X(df)
    #print 'shape of X: ', X.shape
    #print 'X =\n', X

"""
$ python 84.py < enwiki-20150112-400-r100-10576.txt.clean.pretreatment.pair.tsv > enwiki-20150112-400-r100-10576.txt.clean.pretreatment.pair.tsv.ppmi
$ less enwiki-20150112-400-r100-10576.txt.clean.pretreatment.pair.tsv.ppmi
        t       c       f(t,c)  f(t,*)  f(*,c)  PPMI
0       of      the     243412  2006568 3693584 0.899665026929
1       the     of      241867  3695421 2000191 0.894353609712
2       the     in      115779  3695421 1376912 0.370214679903
3       in      the     103710  1388997 3693584 0.199506307622
4       the     to      95581   3695421 1292416 0.185002687547
5       to      the     84183   1293273 3693584 0.00156876091451
...
380062  must    ball    10      12818   3888    3.5107448705
380063  Trials  and     10      248     1744531 0.392836814725
380064  debut   scored  10      7496    7915    3.25916205594
380065  in      Tallinn 10      1388997 153     1.41844103327
380066  with    chances 10      431520  605     1.12158169534
380067  Getty   Paul    10      175     7507    8.75620904913

$ python 84.py < enwiki-20150112-400-r100-10576.txt.clean.pretreatment.pair.tsv
shape of X:  (29139, 28527)
X =
[[  0.           0.           0.         ...,   0.           0.           0.        ]
 [  0.           0.           0.         ...,   0.           0.           0.        ]
 [  0.           0.           0.         ...,   0.           0.           0.        ]
 ...,
 [  0.           0.           0.         ...,  12.89726293   0.           0.        ]
 [  0.           0.           0.         ...,   0.          14.32332184   0.        ]
 [  0.           0.           0.         ...,   0.           0.           0.        ]]
"""
