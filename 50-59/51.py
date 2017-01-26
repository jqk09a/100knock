# -*- coding: utf-8 -*-
"""51"""

import sys, re

def main():
    for line in sys.stdin:
        words = line.split()
        for word in words:
            print re.sub(r'[.;:?!,"")(]', '', word)
        print ''

if __name__ == "__main__":
    main()

"""
$ python 50.py < nlp.txt | python 51.py
Natural
language
processing
NLP
...
and
human
natural
languages

As
such
NLP
...
"""
