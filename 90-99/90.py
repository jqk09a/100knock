# -*- coding: utf-8 -*-
"""90"""

import sys
#import cPickle
from gensim.models import word2vec
from sklearn.metrics.pairwise import cosine_similarity

#エラーを華麗にスルー
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


def q86(model):
    print model['United_States']

def q87(model):
    print model.similarity('United_States', 'U.S')
    #print cosine_similarity(model['United_States'], model['U.S'])[0][0]

def q88(model):
    results = model.most_similar('United_States', topn=10)
    for i,result in enumerate(results, start=1):
        print '{}\t{}\t{}'.format(i,result[0], result[1])

def q89(model):
    #results = model.most_similar(positive=['king','woman'], negative=['man'], topn=10)
    # ->1位にqueen出た
    results = model.most_similar(positive=['Spain','Athens'], negative=['Madrid'], topn=10)
    for i,result in enumerate(results, start=1):
        print '{}\t{}\t{}'.format(i, result[0], result[1])


if __name__ == '__main__':
    model = word2vec.Word2Vec.load(sys.argv[1])
    print '## 86.py --Print word vector'
    q86(model)
    print '\n## 87.py --Calculate cosine similarity'
    q87(model)
    print '\n## 88.py --Find words most similar to some word'
    q88(model)
    print '\n## 89.py --Additive compositionality analogy'
    q89(model)


"""
下準備:
(だめ)
$ python
>>> from gensim.models import word2vec (ref:https://radimrehurek.com/gensim/models/word2vec.html)
>>> data = word2vec.LineSentence('enwiki-20150112-400-r100-10576.txt.clean.pretreatment')
>>> model = word2vec.Word2Vec(data, size=300, window=5, negative=0)
>>> model.save('w2v.model')
(できた)
>>>model5 = word2vec.Word2Vec(word2vec.LineSentence('enwiki-20150112-400-r100-10576.txt.clean.pretreatment'), size=100, window=5, min_count=5, workers=12,sg=1,iter=5)
>>> model5.save('w2v.model')

実行，結果:
$ python work/100/90.py ~/work/100/w2v.model
## 86.py --Print word vector
[  8.02254712e-04  -1.31929351e-03  -1.69764375e-04  -6.82853162e-04
  -1.55259704e-03  -5.87700575e-04  -5.21300128e-04   1.37633760e-05
  -7.78734218e-04  -4.24223108e-04  -1.34253397e-03   1.33678049e-03
  ...
  -7.88876903e-04  -1.11400150e-03  -1.02224387e-03  -1.03531510e-03
  -6.83515333e-04   1.17593573e-03   9.38043348e-04  -4.33834153e-04
   8.84132576e-04  -1.41776027e-03  -6.01642940e-04   1.62666652e-03]

## 87.py --Calculate cosine similarity
0.0644021

## 88.py --Find words most similar to some word
1       Documentary     0.269834965467
2       bypassing       0.244277149439
3       Composition     0.236411601305
4       CBE     0.227629780769
5       Uddin   0.226683348417
6       Bajar   0.222012072802
7       Aimee   0.219775974751
8       encounters      0.218191027641
9       Saint-Jacques   0.21622338891
10      Ellison 0.214766547084

## 89.py --Additive compositionality analogy
1       1988    0.266799807549
2       Puritans        0.231377780437
3       Campeche        0.230024248362
4       Sérgio  0.223577097058
5       Mwanawasa's     0.220115542412
6       1503    0.219586133957
7       alcoholic       0.21823862195
8       Lodge   0.217239335179
9       $350,000        0.215934664011
10      reversal        0.214099541306

結論:
だめ

[reina.a] vodka:~/work/100 $ python 90.py w2v.model
## 86.py --Print word vector
[-0.08806879 -0.35528564  0.20970564  0.05771584  0.2338648   0.2038838
 -0.51023513  0.20316473  0.50837523 -0.01055949 -0.24245973 -0.50064582
  0.41745812 -0.03501152 -0.13379499  0.29957101 -0.18683955 -0.44582918
  ．．．
  0.70689219  0.30690333 -0.28268206 -0.64483327  0.20714684 -0.13898177
 -0.24485029 -0.29838228 -0.2013483  -0.17999934 -0.02116738 -0.01182436
 -0.1299886   0.03788668  0.20194973  0.38239092]

## 87.py --Calculate cosine similarity
0.903982

## 88.py --Find words most similar to some word
1	U.S	0.903981745243
2	US	0.821593403816
3	United_Kingdom	0.70141762495
4	Canada	0.693663060665
5	Mexico	0.679928481579
6	USA	0.671962320805
7	Georgia	0.664916098118
8	Puerto_Rico	0.659888386726
9	Continental	0.656257271767
10	America	0.639110505581

## 89.py --Additive compositionality analogy
1	Greece	0.708501696587
2	Latvia	0.693568944931
3	Sweden	0.685412764549
4	Romania	0.67744165659
5	Austria	0.665382504463
6	Arabia	0.663772284985
7	Italy	0.662843585014
8	Scandinavia	0.654167175293
9	Denmark	0.649935185909
10	Germany	0.637897968292

結論：
できた
"""
