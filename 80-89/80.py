# -*- coding: utf-8 -*-
"""80.py"""

import sys

def main():
    for line in sys.stdin:
        words = line.rstrip().split(' ')
        words_1 = [word.strip('.,!?;:()[]\'\"') for word in words]
        words_2 = [word for word in words_1 if word]
        print ' '.join(words_2)

if __name__ == '__main__':
    main()
