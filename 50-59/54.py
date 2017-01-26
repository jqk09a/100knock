# -*- coding: utf-8 -*-
"""54"""

import sys
from lxml import etree

def main():
    root = etree.parse(sys.stdin)
    words = root.xpath('//word')
    lemmas = root.xpath('//lemma')
    poses = root.xpath('//POS')
    # print '{},{},{}'.format(len(words), len(lemmas), len(poses)) -> all 1452
    for word, lemma, poses in zip(words, lemmas, poses):
        print '{}\t{}\t{}'.format(word.text, lemma.text, poses.text)

if __name__ == "__main__":
    main()


"""
$ python 54.py < nlp.txt.out
Natural natural JJ
language        language        NN
processing      processing      NN
From    from    IN
Wikipedia       Wikipedia       NNP
,       ,       ,
the     the     DT
free    free    JJ
encyclopedia    encyclopedia    NN
Natural natural JJ
language        language        NN
processing      processing      NN
-LRB-   -lrb-   -LRB-
NLP     nlp     NN
-RRB-   -rrb-   -RRB-
is      be      VBZ
a       a       DT
...
"""

"""
・assert len(words) == len(lemmas) == len(poses) ->Trueならスルー，Falseならassertionエラー
・zip[びっくりするくらいメモリ食う]よりもizip(itertoolsモジュール)[まだまし]を使おう
"""
