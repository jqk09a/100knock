# -*- coding: utf-8 -*-
"""73~79.py --base line """

import sys, random, re
import random
import numpy as np
import seaborn
from nltk.stem import PorterStemmer
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, precision_recall_curve, auc
from matplotlib import pyplot as plt


#dataを1次元配列として渡すのver0.17から廃止?でver0.19だとエラー? ->...うるさいからさよなら
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# 73
def make_train_vector(data):
    words = set()   #ユニーク14411語彙
    features = []
    labels = []
    for line in data:
        train = []
        label = line.split()[0]
        labels.append(label)
        for word in line.split()[1:]:
            words.add(word)
            train.append(word)
        features.append(train)
    features = np.array(features)
    words = list(words)
    train_vecs = []
    for feature in features:
        train_vec = np.zeros(len(words))
        for word in feature:
            index = words.index(word)
            train_vec[index] += 1
        train_vecs.append(train_vec)
    train_vecs = np.array(train_vecs)
    return features, words, train_vecs, labels


# 73
def train_model(train_vecs, labels):
    lr_model = LogisticRegression()
    lr_model.fit(train_vecs, labels)
    return lr_model

# 74, 76
def test(lr_model, sentence, words):
    #label = label.replace('+','')
    sentence = re.sub('[\.\,\:\;\'\"\(\)\[\]]', '', sentence)
    test_vec = np.zeros(len(words))
    for word in sentence.split():
        word = word.decode('utf-8','ignore')
        word = PorterStemmer().stem(word)
        if word in words:
            index = words.index(word)
            test_vec[index] += 1
        else:
            continue
    return lr_model.predict(test_vec)[0], lr_model.predict_proba(test_vec)[0]

# 75
def sort_weight(W, words):
    W_index = np.argsort(W)
    print '#high_weight top10'
    for i, h_i in enumerate(W_index[:-11:-1], start=1):
        print '{}.\tweight: {} \tword: {}'.format(i, W[h_i], words[h_i])
    print '#low_weight top10'
    for i, l_i in enumerate(W_index[:10], start=1):
        print '{}.\tweight: {} \tword: {}'.format(i, W[l_i], words[l_i])

# 78
def cross_valid(trains, labels):
    # 5分交差検定
    X_train, X_test, y_train, y_test = train_test_split(trains, labels, test_size=0.5, random_state=7)
    lr_model_c = LogisticRegression()
    lr_model_c.fit(X_train, y_train)
    y_pre = lr_model_c.predict(X_test)
    y_pro = lr_model_c.predict_proba(X_test)
    print '# varification \naccuracy: {}\tprecision: {}\trecall: {}\tF1-score: {}'.format(accuracy_score(y_test, y_pre), precision_score(y_test, y_pre, pos_label='+1'), recall_score(y_test, y_pre, pos_label='+1'), f1_score(y_test, y_pre, pos_label='+1'))
    return y_test, y_pro[:,0]


if __name__ == '__main__':

    ### 73 ###
    # 素性，下準備
    print '----- modeling(73) -----'
    print 'preparing... '
    features, words, train_vecs, labels = make_train_vector(sys.stdin)
    # モデルの作成，訓練
    print 'training...'
    lr_model = train_model(train_vecs, labels)
    print 'completed!'
    print '# parameters'
    b=lr_model.intercept_
    W=lr_model.coef_.ravel()
    print("intercept(bias):{} \ncoefficients(weight):{}".format(b, W))

    #### 74 ###
    # テスト
    print '\n----- test(74) -----'
    with open('sentiment.txt', 'r') as f:
        lines = random.sample(f.readlines(), 3)
    for i,line in enumerate(lines, start=1):
        label = line.split()[0]
        sentence = line.rstrip().replace('+1 ','').replace('-1 ', '')
        print '# {}\n{}'.format(i, sentence)
        p_lab, p_prob = test(lr_model, sentence, words)
        print 'label: {} \tpred_label: {} \tpred_probability: {}'.format(label, p_lab, p_prob)

    ### 75 ###
    # 重みtop10
    print '\n----- weight(75) -----'
    sort_weight(W, words)

    #### 76 ###
    # テスト
    print '\n----- test(76) -----'
    print 'label\tpred_label\tpred_probability'
    with open('sentiment.txt', 'r') as f:
        lines = random.sample(f.readlines(), 10)
        for line in lines:
            label = line.split()[0]
            sentence = line.rstrip().replace('+1 ','').replace('-1 ', '')
            p_label, p_prob = test(lr_model, sentence, words)
            print '{}\t{}\t\t{}'.format(label, p_label, p_prob)


    ### 77 ###
    # 正解率
    print '\n----- varification(77) -----'
    p_labels = lr_model.predict(train_vecs)
    print '# varification \naccuracy: {}\tprecision: {}\trecall: {}\tF1-score: {}'.format(accuracy_score(labels, p_labels), precision_score(labels, p_labels, pos_label='+1'), recall_score(labels, p_labels, pos_label='+1'), f1_score(labels, p_labels, pos_label='+1'))

    ### 78 ###
    print '\n----- cross validation(78) -----'
    y_test, y_pro = cross_valid(train_vecs, labels)

    ### 79 ###
    precision, recall, thresholds = precision_recall_curve(y_test, y_pro, pos_label='+1')
    area = auc(recall, precision)
    # output
    plt.plot(recall, precision)
    plt.xlabel('recall')
    plt.ylabel('precision')
    plt.title('#baseline precision_recall curve (AUC={})'.format(area))
    plt.show()


"""
$ python 73.py < sentiment.txt.train
----- modeling(73) -----
preparing...
training...
completed!
# parameters
intercept(bias):[ 0.31220568]
coefficients(weight):[ 0.9836167   0.20266432  0.18961963 ..., -0.80728764  0.12443659
 -0.29673781]

----- test(74) -----
# 1
rarely do films come along that are as intelligent , exuberant , and moving as monsoon wedding .
label: +1       pred_label: +1  pred_probability: [ 0.92666444  0.07333556]
# 2
brosnan's finest non-bondish performance yet fails to overcome the film's manipulative sentimentality and annoying stereotypes .
label: -1       pred_label: -1  pred_probability: [ 0.11093933  0.88906067]
# 3
a solid cast , assured direction and complete lack of modern day irony .
label: +1       pred_label: +1  pred_probability: [ 0.76860992  0.23139008]

----- weight(75) -----
# high_weight top10
1.      weight: 2.25724001893   word: bore
2.      weight: 1.94021338794   word: dull
3.      weight: 1.91499457124   word: fail
4.      weight: 1.86381857192   word: wast
5.      weight: 1.85342149191   word: mediocr
6.      weight: 1.7618947443    word: plod
7.      weight: 1.7590940871    word: routin
8.      weight: 1.69209717509   word: worst
9.      weight: 1.68965610531   word: badli
10.     weight: 1.68492641536   word: flat
# low_weight top10
1.      weight: -2.06485751976  word: engross
2.      weight: -1.91984702613  word: refresh
3.      weight: -1.88904120118  word: unexpect
4.      weight: -1.76058996596  word: wonder
5.      weight: -1.67760301095  word: resist
6.      weight: -1.66289778468  word: smarter
7.      weight: -1.6470086453   word: remark
8.      weight: -1.60926296528  word: beauti
9.      weight: -1.56939719452  word: examin
10.     weight: -1.54708575873  word: refreshingli

----- test(76) -----
label   pred_label      pred_probability
-1      -1              [ 0.46870091  0.53129909]
+1      +1              [ 0.98355771  0.01644229]
+1      +1              [ 0.51339238  0.48660762]
+1      +1              [  9.99831806e-01   1.68193895e-04]
-1      -1              [ 0.07414939  0.92585061]
-1      -1              [ 0.24712451  0.75287549]
+1      +1              [ 0.8744075  0.1255925]
+1      +1              [ 0.9314673  0.0685327]
+1      +1              [ 0.76356043  0.23643957]
+1      +1              [ 0.80602241  0.19397759]
1...

----- varification -----
# count
all: 10662
tp: 4663        tn: 5020        fp: 311 fn: 668
<type 'float'>
# varification
accuracy: 0.908178578128        precision: 0.93747486932        recall: 0.874695179141  F1-score: 0.904997573993
"""
