# -*- coding: utf-8 -*-
"""93"""

import sys

def main():
    correct=0
    for i,line in enumerate(sys.stdin, start=1):
        tokens = line.strip().split('\t')
        if tokens[3]==tokens[4]:
            correct += 1
    print 'accuracy: {:.3f}'.format(correct*1.0/i)


if __name__ == '__main__':
    main()

"""
$ python 93.py < questions-words.txt.85-92
accuracy: 0.035
$ python 93.py < questions-words.txt.90-92
accuracy: 0.500
"""
