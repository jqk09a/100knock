# -*- coding: utf-8 -*-
"""72"""

import sys, re
from nltk.stem import PorterStemmer
from nltk import word_tokenize
from nltk import pos_tag

# base line > sentiment.txt
def main():
    for line in sys.stdin:
        features = []
        for word in re.sub('[\.\,\:\;\'\"\(\)\[\]]', '', line).split():
            with open('stoplist.txt', 'r') as f:
                stoplist = [stopword.rstrip() for stopword in f]
                if word in stoplist:
                    continue
                else:
                    word = word.decode('utf-8','ignore')
                    features.append(PorterStemmer().stem(word))
        print ' '.join(features)

# +α > sentiment2.txt
def main2():
    for line in sys.stdin:
        features = []
        label = line[:2].split()[0]
        line = re.sub('[\.\,\:\;\'\"\(\)\[\]]', '', line[2:])
        pos_line = word_tokenize(line)
        #print pos_tag(pos_line)
        for pair in pos_tag(pos_line):
                word = pair[0].decode('utf-8','ignore')
                features.append((PorterStemmer().stem(word), pair[1]))
        print label,
        print ' '.join('{}**{}'.format(feature[0], feature[1]) for feature in features) # <-これじゃ読み込めない，+1 (u'aaa', 'NN') (,) ... の形に


if __name__ == '__main__':
    #main()
    main2()

"""
## main()
$ python 72.py < sentiment.txt > sentiment.txt.train
$ less sentiment.txt.train
-1 intrigu near-miss
+1 interest student enthusiast intern danc world music film design make viewer age cultur background rhythmic abil danc
+1 watch bettani strut stuff youll star
+1 light engross piec lux eighti great combin act narrat jewish grandmoth subject  take film part biographi part entertain part histori
-1 expect director michael apt enigma screenwrit nichola kazan revers fortun clich pileup
-1 tediou make forgiv fake dishonest entertain ultim percept moment bridget joness diari
+1 fabric hypnot mr mattei foster moment spontan intimaci
...

## main2()
$ python 72.py < sentiment.txt > sentiment.txt.train2
$ less sentiment.txt.train2
-1 an**DT intrigu**JJ near-miss**JJ
+1 though**IN of**IN particular**JJ interest**NN to**TO student**NNS and**CC enthusiast**NN of**IN intern**JJ danc**NN and**CC world**NN music**NN the**DT film**NN is**VBZ design**VBN to**TO make**VB viewer**NNS of**IN all**DT age**NNS cultur**JJ background**NNS and**CC rhythmic**JJ abil**NN want**VBP to**TO get**VB up**RP and**CC danc**NN
+1 just**RB watch**VB bettani**NN strut**VB hi**PRP$ stuff**NN youll**NN know**VBP a**DT star**NN when**WRB you**PRP see**VBP one**CD
...
"""
