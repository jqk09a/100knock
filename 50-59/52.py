# -*- coding: utf-8 -*-
"""52"""

# stemming:語幹抽出
# porterとporter2はどっちが有能なんだろう

import sys
from stemming import porter,porter2

def main():
    for word in sys.stdin:
        word = word.strip()
        s_word = porter.stem(word)
        s2_word = porter2.stem(word)
        print "{}\t{}\t{}".format(word, s_word, s2_word)

if __name__ == "__main__":
    main()

"""
$ python 52.py < word.txt
Natural Natur   Natur
language        languag languag
processing      process process
NLP     NLP     NLP
...
generation      gener   generat
...
was     wa      was
...
increasingly    increasingli    increas
...
"""
