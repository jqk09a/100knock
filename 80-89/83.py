# -*- coding: utf-8 -*-
"""83"""

import sys, json
import pandas as pd
from collections import defaultdict

def main():
    tc_D = defaultdict(int)
    t_D = defaultdict(int)
    c_D = defaultdict(int)
    for line in sys.stdin:
        t,c = line.rstrip().split('\t')
        tc_T = tuple([t,c])
        tc_D[tc_T] += 1
        t_D[t] += 1
        c_D[c] += 1
    print 't\tc\tf(t,c)\tf(t,*)\tf(*,c)'
    for k,v in tc_D.items():
        print '{}\t{}\t{}\t{}\t{}'.format(k[0], k[1], v, t_D[k[0]], c_D[k[1]])

if __name__ == '__main__':
    main()
