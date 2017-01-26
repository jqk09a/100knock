# -*- coding: utf-8 -*-
"""70"""

import sys, random

def main():
    with open('./rt-polaritydata/rt-polaritydata/rt-polarity.pos','r') as pos, \
         open('./rt-polaritydata/rt-polaritydata/rt-polarity.neg','r') as neg, \
         open('sentiment.txt', 'w') as fo:

        l_list = []
        for line in pos:
            l_list.append('+1 '+line.rstrip())
        for line in neg:
            l_list.append('-1 '+line.rstrip())
        random.shuffle(l_list)

        for line in l_list:
            fo.write(line)

if __name__ == '__main__':
    main()


"""
$  python 70.py
$  less sentiment.txt
-1 the latest vapid ...
-1 everyone connected to ...
+1 a cultural wildcard ...
+1 grant gets to display ...
-1 there aren't many laughs ...
+1 fantastic !
...

▶正例負例の数確認
$  grep -c -G "^+1" sentiment.txt
5331
$  grep -c -G "^-1" sentiment.txt
5331
"""
