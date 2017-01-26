# -*- coding: utf-8 -*-
"""82"""

import sys, random

def main():
    for line in sys.stdin:
        words = line.rstrip().split(' ')
        for idx_t in range(len(words)):
            c_range = random.randint(1,5)
            for idx_c in range(idx_t-c_range, idx_t+c_range):
                if idx_c!=idx_t and 0<=idx_c<=len(words)-1:
                    print '{}\t{}'.format(words[idx_t], words[idx_c])


if __name__ == '__main__':
    main()
