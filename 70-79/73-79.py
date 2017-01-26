# -*- coding: utf-8 -*-
"""73~79.py --形容詞,動詞を重要視ver. """

import argparse
import sys, re, random
import numpy as np
import seaborn
from nltk import word_tokenize
from nltk import pos_tag
from nltk.stem import PorterStemmer
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, precision_recall_curve, auc
from matplotlib import pyplot as plt


#dataを1次元配列として渡すのver0.17から廃止?でver0.19だとエラー? ->...うるさいからさよなら
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# オプション
parser = argparse.ArgumentParser()
parser.add_argument("--margin", type=float, default=0.1)    # 0.0~0.5の範囲で最も良いaccuracy:0.1
args = parser.parse_args()

# 形容詞,動詞フィルター
fil = re.compile(r'[JJ.*|VB.*]')
# マージン
marg = args.margin


# 73
def make_train_vector2(data):
    words = set()   #ユニーク14411語彙
    features = []
    labels = []
    for line in data:
        train = []
        label = line.split()[0]
        labels.append(label)
        for word in line.split()[1:]:
            word,tag = word.split('**')
            words.add(word)
            train.append([word,tag])
        features.append(train)
    features = np.array(features)
    words = list(words)
    train_vecs = []
    for feature in features:
        train_vec = np.zeros(len(words))
        for pair in feature:
            index = words.index(pair[0])
            if re.match(fil, pair[1]):
                train_vec[index] += float(1+marg)
            else:
                train_vec[index] += float(1-marg)
        train_vecs.append(train_vec)
    train_vecs = np.array(train_vecs)
    return features, words, train_vecs, labels

# 73
def train_model(trains, labels):
    lr_model = LogisticRegression()
    lr_model.fit(trains, labels)
    return lr_model

# 74, 76
def test(lr_model, sentence, words):
    #label = label.replace('+','')
    sentence = re.sub('[\.\,\:\;\'\"\(\)\[\]]', '', sentence)
    pos_sentence = word_tokenize(sentence)
    test_vec = np.zeros(len(words))
    for pair in pos_tag(pos_sentence):
        word = pair[0].decode('utf-8','ignore')
        word = PorterStemmer().stem(word)
        if word in words:
            index = words.index(word)
            if re.match(fil, pair[1]):
                test_vec[index] += float(1+marg)
            else:
                test_vec[index] += float(1-marg)
        else:
            continue
    return lr_model.predict(test_vec)[0], lr_model.predict_proba(test_vec)[0]

# 75
def sort_weight(W, words):
    W_index = np.argsort(W)
    print '# high_weight top10'
    for i, h_i in enumerate(W_index[:-11:-1], start=1):
        print '{}.\tweight: {} \tword: {}'.format(i, W[h_i], words[h_i])
    print '# low_weight top10'
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
    return y_test, y_pro

if __name__ == '__main__':

    ### 73 ###
    # 素性，下準備
    print '----- modeling(73) -----'
    print 'preparing... '
    features, words, train_vecs, labels = make_train_vector2(sys.stdin)
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
    print "* margin:" + str(marg)

    ### 78 ###
    print '\n----- cross validation(78) -----'
    y_test, y_pro = cross_valid(train_vecs, labels)
    print "* margin:" + str(marg)

    ### 79 ###
    precision, recall, thresholds = precision_recall_curve(y_test, y_pro[:,0], pos_label='+1')
    area = auc(recall, precision)
    # output
    plt.plot(recall, precision)
    plt.xlabel('recall')
    plt.ylabel('precision')
    plt.title('#margin={} precision_recall curve (AUC={})'.format(marg, area))
    plt.show()


"""
$ python 77.py --margin 0.1 < sentiment.txt.train2
----- modeling(73) -----
preparing...
training...
completed!
# parameters
intercept(bias):[ 0.23361417]
coefficients(weight):[-0.28744163  1.04274555  0.19445095 ..., -0.62629791  0.15512897
  0.11886374]

----- test(74) -----
# 1
the world needs more filmmakers with passionate enthusiasms like martin scorsese . but it doesn't need gangs of new york .
label: -1       pred_label: -1  pred_probability: [ 0.3934472  0.6065528]
# 2
that rara avis : the intelligent romantic comedy with actual ideas on its mind .
label: +1       pred_label: +1  pred_probability: [ 0.82708714  0.17291286]
# 3
what sets this romantic comedy apart from most hollywood romantic comedies is its low-key way of tackling what seems like done-to-death material .
label: +1       pred_label: +1  pred_probability: [ 0.87399061  0.12600939]

----- weight(75) -----
# high_weight top10
1.      weight: 2.22761190694   word: bore
2.      weight: 1.92509645442   word: wast
3.      weight: 1.91903086483   word: dull
4.      weight: 1.84981249809   word: fail
5.      weight: 1.81167490496   word: unless
6.      weight: 1.79659079176   word: mediocr
7.      weight: 1.79238936172   word: appar
8.      weight: 1.76230665563   word: neither
9.      weight: 1.75681267956   word: worst
10.     weight: 1.75081913078   word: routin
# low_weight top10
1.      weight: -2.10596664199  word: engross
2.      weight: -1.82736223528  word: unexpect
3.      weight: -1.81677775401  word: refresh
4.      weight: -1.60993541737  word: remark
5.      weight: -1.52286718567  word: smarter
6.      weight: -1.51327290015  word: cinema
7.      weight: -1.49497172562  word: solid
8.      weight: -1.47323172861  word: awar
9.      weight: -1.44990403451  word: happi
10.     weight: -1.44374965332  word: beauti

----- test(76) -----
label   pred_label      pred_probability
-1      -1              [ 0.43144835  0.56855165]
+1      +1              [ 0.90030823  0.09969177]
-1      -1              [ 0.1515422  0.8484578]
+1      +1              [ 0.99087524  0.00912476]
-1      -1              [ 0.45549772  0.54450228]
+1      +1              [ 0.66555736  0.33444264]
-1      -1              [ 0.28990533  0.71009467]
+1      +1              [ 0.87185324  0.12814676]
+1      +1              [ 0.99875129  0.00124871]
-1      -1              [ 0.10147177  0.89852823]

----- varification(77) -----
# varification
accuracy: 0.953573438379        precision: 0.953632832955       recall: 0.953573438379  F1-score: 0.953571918661
* margin:0.1

----- cross validation(78) -----
# varification
accuracy: 0.749765522416        precision: 0.749767248036       recall: 0.749765522416  F1-score: 0.749766279696
* margin:0.1

----- precision_recall curve(79) -----
http://www.cl.ecei.tohoku.ac.jp/~reina.a/nlp100/77_margin0.1.png


####### base-line #######
----- varification(77) -----
# varification
accuracy: 0.944757081223        precision: 0.944794659283       recall: 0.944757081223  F1-score: 0.944755914412

----- cross validation(78) -----
# varification
accuracy: 0.725192271619        precision: 0.72518902132        recall: 0.725192271619  F1-score: 0.725177145797

----- precision_recall curve(79) -----
http://www.cl.ecei.tohoku.ac.jp/~reina.a/nlp100/73_base.png
"""
