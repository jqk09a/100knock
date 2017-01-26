# -*- coding: utf-8 -*-
"""55"""

import sys
from lxml import etree

def main():
    root = etree.parse(sys.stdin)
    words = root.xpath('//word')
    ners = root.xpath('//NER')
    # print '{},{}'.format(len(words), len(ners)) -> all 1452
    for word, ner in zip(words, ners):
        if ner.text == 'PERSON':
            print word.text

if __name__ == "__main__":
    main()

"""
$ python 55.py < nlp.txt.out
Alan
Turing
Joseph
Weizenbaum
MARGIE
Schank
Wilensky
Meehan
Lehnert
Carbonell
Lehnert
Jabberwacky
Moore
"""
