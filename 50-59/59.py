# -*- coding: utf-8 -*-
"""59"""

import sys, re
from lxml import etree
from nltk.tree import Tree  # http://www.nltk.org/ <-楽になれます．

def main():
    root = etree.parse(sys.stdin)
    parses = root.xpath('//parse')
    for p in parses:
        tree = Tree.fromstring(p.text)
        for s in tree.subtrees():
            if s.label() == 'NP':
                print ' '.join(s.leaves())


if __name__ == "__main__":
    main()

"""
$ python 59.py < nlp.txt.out
atural language processing
Wikipedia
the free encyclopedia Natural language processing -LRB- NLP -RRB-
the free encyclopedia Natural language processing
NLP
a field of computer science , artificial intelligence , and linguistics concerned with the interactions between computers and human -LRB- natural -RRB- languages
a field of computer science
a field
computer science
artificial intelligence
linguistics concerned with the interactions between computers and human -LRB- natural -RRB- languages
linguistics
...
"""
